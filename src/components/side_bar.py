import streamlit as st

def render_reset_button() -> None:
    with st.sidebar:
      if st.button("Reset session", type="primary"):
          keys_to_delete = ["uploaded_file", "file_uploaded", "field_mappings", "submitted", "filled_document"]

          for item in st.session_state.get("field_mappings", []):
              st.session_state.pop(item[1], None)
          
          for key in keys_to_delete:
              st.session_state.pop(key, None)
          
          st.rerun()