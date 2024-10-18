
import io
import base64
import streamlit as st
import os
from together import Together
from PIL import Image
import requests
from io import BytesIO

# Set page config
st.set_page_config(page_title="TEX: TelecomAI Assistant", page_icon="📡", layout="wide")

# Custom CSS to improve the app's appearance
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .st-bw {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize the Together client
@st.cache_resource
def get_together_client():
    return Together(base_url="https://api.aimlapi.com/v1", api_key=st.secrets["AIML_API_KEY"])

client = get_together_client()

def process_text_query(query, model="meta-llama/Llama-3.2-3B-Instruct-Turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for telecommunication tasks."},
            {"role": "user", "content": query}
        ],
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message.content

def process_image_query(image_base64, query, model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an AI assistant specialized in analyzing telecommunications infrastructure and satellite imagery."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                ]
            },
        ],
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message.content

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


# Sidebar
with st.sidebar:
    
    st.title("TEX: TelecomAI Assistant")
    st.info("This AI-powered assistant helps with various telecommunication tasks, including text analysis, document processing, and image analysis.")
    st.markdown("---")
    st.write("Powered by Llama 3.2 models")

# Main content
st.title("Welcome to TEX, a TelecomAI Assistant App")

task_type = st.radio("Select Task Type", ["Text Query", "Document Analysis", "Image Analysis"])

if task_type == "Text Query":
    st.header("Text Query")
    query = st.text_input("Enter your query:")
    if st.button("Process Query", key="text_query"):
        if query:
            with st.spinner("Processing..."):
                response = process_text_query(query)
            st.success("Query processed successfully!")
            st.subheader("Response:")
            st.write(response)
        else:
            st.warning("Please enter a query.")

elif task_type == "Document Analysis":
    st.header("Document Analysis")
    document_type = st.selectbox("Select Document Type", ["Regulatory Document", "Contract", "Customer Inquiry"])
    text_input = st.text_area("Enter the document text:")
    if st.button("Analyze Document", key="doc_analysis"):
        if text_input:
            with st.spinner("Analyzing..."):
                if document_type == "Regulatory Document":
                    query = f"Summarize the following regulatory document: {text_input}"
                elif document_type == "Contract":
                    query = f"Analyze the following contract and highlight key points: {text_input}"
                else:
                    query = f"Address the following customer inquiry: {text_input}"
                response = process_text_query(query)
            st.success("Document analyzed successfully!")
            st.subheader("Analysis:")
            st.write(response)
        else:
            st.warning("Please enter the document text.")

elif task_type == "Image Analysis":
    st.header("Image Analysis")
    image_type = st.selectbox("Select Image Type", ["Satellite Imagery", "Equipment Photo"])
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        query = st.text_input("Enter your analysis query:")
        if st.button("Analyze Image", key="image_analysis"):
            if query:
                with st.spinner("Analyzing image..."):
                    # Convert image to base64
                    image_base64 = image_to_base64(image)
                    
                    # Process image query
                    response = process_image_query(image_base64, query)
                st.success("Image analyzed successfully!")
                st.subheader("Analysis:")
                st.write(response)
            else:
                st.warning("Please enter an analysis query.")
    else:
        st.info("Please upload an image to analyze.")

# Footer
st.markdown("---")
st.markdown("📡 🛰️ TEX TelecomAI Assistant")