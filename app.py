import streamlit as st
from model import get_doc_response
from deep_translator import GoogleTranslator
from pdf_reader import extract_text_from_pdf  # For reading the PDF file

t = GoogleTranslator(source='auto', target='hi')

# Set up Streamlit app title and page layout
st.set_page_config(
    page_title="Doc Cure",
    page_icon=":herb:",
)

# st.sidebar.success("SELECT THE PAGE FROM ABOVE")


# Set up Streamlit app title
st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 20px; border-radius: 10px; text-align: center;'>
        <h1 style='color: #333;'>🧬🩺</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Create a file uploader for the PDF file
uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

# Check if a PDF file has been uploaded
if uploaded_pdf is not None:
    # Extract the text from the uploaded PDF
    extracted_text = extract_text_from_pdf(uploaded_pdf)
    
    # Display the extracted text (optional)
    # st.write("Extracted Text:")
    # st.write(extracted_text)

    
    doc_cure = get_doc_response(extracted_text)
    
    st.write(doc_cure)

