import streamlit as st
from src.utils.docx_prosessing import create_filled_doc, process_doc


def render_document_filling_UI() -> None:
    uploaded_file = st.session_state.get("uploaded_file")
    if uploaded_file:
        process_doc(uploaded_file)
        # Render the input forms
        for field, key in st.session_state["field_mappings"]:
            st.text_input(label=field, key=key)

        # Button for initial document creation
        if not st.session_state.get("submitted", None):
            if st.button("Submit", type="primary"):
                st.session_state["filled_document"] = create_filled_doc(uploaded_file, st.session_state["field_mappings"])
                st.session_state["submitted"] = True
                st.rerun()

        # Once created, present the download button and button to refresh the contents of the new doc
        if st.session_state.get("submitted", None):
            st.download_button(
                label="Download filled document",
                data=st.session_state["filled_document"],
                file_name="filled_document.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            if st.button("Refresh contents"):
                st.session_state["filled_document"] = create_filled_doc(uploaded_file, st.session_state["field_mappings"])
                st.info("Document content refreshed!")
                st.rerun()