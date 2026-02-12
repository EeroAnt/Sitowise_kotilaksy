import streamlit as st
from src.components.document_filling import render_document_filling_UI
from src.components.file_upload import render_file_upload


def render_main_panel():
    if not st.session_state.get("file_uploaded", None):
        render_file_upload()
    else:
        render_document_filling_UI()