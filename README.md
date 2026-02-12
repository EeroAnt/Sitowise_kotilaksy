# Sitowise Kotilaksy

A Streamlit app for filling in Word document templates. Upload a `.docx` file with `{{placeholder}}` fields, fill in the values through a web UI, and download the completed document.

## Features

- Upload `.docx` templates with `{{placeholder}}` syntax
- Automatically extracts placeholders from paragraphs and tables
- Handles duplicate placeholders (each gets its own input field)
- Download the filled document as `.docx`

## Requirements

- Python 3.11+
- uv (package manager)

## Installation
```powershell
uv sync
```

## Usage
```powershell
./main.ps1
```

Or alternatively on other systems, run the command inside it.

Then open `http://localhost:8501` in your browser.

## How it works

1. Upload a Word document containing `{{FIELD_NAME}}` placeholders
2. Fill in each field via the generated input form
3. Click Submit to generate the filled document
4. Click the download button to download it

## Project Structure
```
├── main.ps1                # Run command stored
├── main.py                 # Entry point
└── src/
    ├── components/         # Streamlit UI components
    │   ├── document_filling.py
    │   ├── file_upload.py
    │   ├── main_panel.py
    │   └── side_bar.py
    └── utils/              # Document processing
        ├── docx_prosessing.py
        └── field_mappings.py
```