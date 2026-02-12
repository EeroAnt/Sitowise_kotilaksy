import streamlit as st
from src.utils.docx_prosessing import create_filled_doc, process_doc


def render_document_filling_UI() -> None:
    uploaded_file = st.session_state.get("uploaded_file")
    if uploaded_file:
        fields_to_fill = process_doc(uploaded_file)
        for field in fields_to_fill:
            st.text_input(label=field, key=field)
        if st.button("Submit", type="primary"):
            create_filled_doc(uploaded_file)