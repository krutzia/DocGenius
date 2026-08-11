import numpy as np
import streamlit as st
from PyPDF2 import PdfReader
import ollama

st.set_page_config(
    page_title="DocGenius",
    page_icon="📄"
)

st.title("DocGenius 📄")
st.write("Upload a PDF and ask questions about it.")

pdf = st.file_uploader("Upload your PDF", type="pdf")

if pdf is not None:

    reader = PdfReader(pdf)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    if not text.strip():
        st.error("Could not extract text from this PDF.")
        st.stop()

    # Split PDF text into chunks
    chunk_size = 3000

    chunks = [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]

    st.success(
        f"PDF loaded successfully — {len(chunks)} chunks created."
    )

    # Create local embeddings
    with st.spinner("Creating document embeddings..."):

        response = ollama.embed(
            model="nomic-embed-text",
            input=chunks
        )

        embeddings = np.array(response["embeddings"])

    question = st.text_input(
        "Ask a question about your PDF:"
    )

    if question:

        with st.spinner("Searching the document..."):

            question_response = ollama.embed(
                model="nomic-embed-text",
                input=question
            )

            question_embedding = np.array(
                question_response["embeddings"][0]
            )

            # Cosine similarity
            similarities = np.dot(
                embeddings,
                question_embedding
            ) / (
                np.linalg.norm(embeddings, axis=1)
                * np.linalg.norm(question_embedding)
                + 1e-10
            )

            # Get 5 most relevant chunks
            top_indices = np.argsort(similarities)[-5:][::-1]

            relevant_text = "\n\n".join(
                chunks[i] for i in top_indices
            )

        with st.spinner("Generating answer..."):

            prompt = f"""
You are a PDF question-answering assistant.

Answer the user's question using ONLY the information
contained in the provided document excerpts.

If the answer cannot be found in the document, say:
"I couldn't find that information in the PDF."

Do not use outside knowledge.

DOCUMENT EXCERPTS:
{relevant_text}

QUESTION:
{question}
"""

            response = ollama.chat(
                model="llama3.2:3b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            answer = response["message"]["content"]

            st.subheader("Answer")
            st.write(answer)