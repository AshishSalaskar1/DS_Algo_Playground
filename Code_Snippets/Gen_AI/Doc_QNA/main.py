import streamlit as st
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama, OllamaEmbeddings
import os
import chromadb.api

chromadb.api.client.SharedSystemClient.clear_system_cache()

embeddings = OllamaEmbeddings(model="llama3.2")
llm = ChatOllama(model="llama3.2")

# Sidebar for Configuration
with st.sidebar:
    st.header("Configuration")
    session_id = st.text_input("Session ID", value="default_session", help="Unique identifier for your session.")
    
    # File uploader
    uploaded_files = st.file_uploader("Upload PDF(s)", type="pdf", accept_multiple_files=True)
    if uploaded_files and "documents" not in st.session_state:
        st.session_state.documents = []
        for file in uploaded_files:
            file_name = file.name
            with open(f"./temp/{file_name}.pdf", "wb") as f:
                f.write(file.getvalue())
            loader = PyPDFLoader(f"./temp/{file_name}.pdf")
            doc = loader.load()
            st.session_state.documents.extend(doc)

# Chat Section
st.title("Chat with Your Documents")
st.write("You can ask questions about your uploaded documents.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process documents if available
if "documents" in st.session_state:
    documents = st.session_state.documents

    # Split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)

    # Create a vector store
    vector_db = Chroma.from_documents(splits, embeddings)
    retriever = vector_db.as_retriever()

    # Setup chains and prompts
    prompt_text = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. DO NOT answer the question; "
        "just reformulate it if needed; otherwise, return it as is."
    )

    context_qna_prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_text),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    history_aware_retriever = create_history_aware_retriever(llm, retriever, context_qna_prompt)

    # Answer question
    system_prompt = (
        "You are an assistant for question answering tasks. "
        "Use the following pieces of retrieved context to answer the questions. "
        "If you don't know the answer, just say that you don't know.\n\n"
        "Context: {context}"
    )

    qna_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    qa_chain = create_stuff_documents_chain(llm, qna_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)

    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in st.session_state:
            st.session_state[session_id] = ChatMessageHistory()
        return st.session_state[session_id]

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer"
    )

    # Chat Input
    user_input = st.chat_input("Your question: ")
    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        session_history = get_session_history(session_id)
        response = conversational_rag_chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )

        assistant_response = response["answer"]

        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
