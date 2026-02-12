import re
from docx import Document
from streamlit.runtime.uploaded_file_manager import UploadedFile

def process_doc(uploaded_file: UploadedFile) -> list[str]:
    doc = Document(uploaded_file)
    fields_to_fill = []

    # We're assuming that the placeholders are nice enough
    # so this is enough parsing
    
    pattern = r"\{\{(\w+)\}\}"
    
    for para in doc.paragraphs:
        matches = re.findall(pattern, para.text)
        fields_to_fill.extend(matches)
    
    return fields_to_fill