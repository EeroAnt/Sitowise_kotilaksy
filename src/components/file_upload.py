import streamlit as st

def render_file_upload():
    doc_to_upload = st.file_uploader(
        "Upload a document",
        type=["docx"],
        accept_multiple_files=False,
        help="Upload your .docx-document for filling in"
    )
    if doc_to_upload is not None:
        if st.button("Upload", type="primary"):
            st.session_state["file_uploaded"] = True