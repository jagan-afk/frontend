import streamlit as st
import requests

st.set_page_config(page_title="Document Q&A System", layout="centered")
st.title("📄 Document Q&A Upload and Indexing")

BASE_URL = "https://whats-production.up.railway.app"

st.header("Upload Document")
uploaded_file = st.file_uploader("Choose file (PDF, DOCX, Excel, CSV, TXT)", type=["pdf", "docx", "csv", "xlsx", "txt"])
category = st.text_input("Category Tag")
tenant_id = st.text_input("Tenant ID")

if st.button("Upload Document") and uploaded_file and tenant_id:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    data = {"category": category, "tenant_id": tenant_id}
    res = requests.post(f"{BASE_URL}/upload", files=files, data=data)
    st.success(res.json()["message"])

st.header("Add Q&A Pair")
question = st.text_input("Question")
answer = st.text_area("Answer")

if st.button("Add Q&A") and question and answer and tenant_id:
    data = {"question": question, "answer": answer, "category": category, "tenant_id": tenant_id}
    res = requests.post(f"{BASE_URL}/qa", data=data)
    st.success(res.json()["message"])
