import streamlit as st
import os
from together import Together
from PIL import Image
import requests
from io import BytesIO

# Initialize the Together client
client = Together(base_url="https://api.aimlapi.com/v1", api_key=st.secrets["AIML_API_KEY"])

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

def process_image_query(image, query, model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an AI assistant specialized in analyzing telecommunications infrastructure and satellite imagery."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {"type": "image_url", "image_url": {"url": image}}
                ]
            },
        ],
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message.content

st.title("TelecomAI Assistant")

task_type = st.selectbox("Select Task Type", ["Text Query", "Document Analysis", "Image Analysis"])

if task_type == "Text Query":
    query = st.text_input("Enter your query:")
    if st.button("Process Query"):
        with st.spinner("Processing..."):
            response = process_text_query(query)
        st.write("Response:", response)

elif task_type == "Document Analysis":
    document_type = st.selectbox("Select Document Type", ["Regulatory Document", "Contract", "Customer Inquiry"])
    text_input = st.text_area("Enter the document text:")
    if st.button("Analyze Document"):
        with st.spinner("Analyzing..."):
            if document_type == "Regulatory Document":
                query = f"Summarize the following regulatory document: {text_input}"
            elif document_type == "Contract":
                query = f"Analyze the following contract and highlight key points: {text_input}"
            else:
                query = f"Address the following customer inquiry: {text_input}"
            response = process_text_query(query)
        st.write("Analysis:", response)

elif task_type == "Image Analysis":
    image_type = st.selectbox("Select Image Type", ["Satellite Imagery", "Equipment Photo"])
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        query = st.text_input("Enter your analysis query:")
        if st.button("Analyze Image"):
            with st.spinner("Analyzing..."):
                # Save the image to a BytesIO object
                img_byte_arr = BytesIO()
                image.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()

                # Upload the image to a temporary storage and get URL
                # For this example, we'll use a placeholder URL. In a real app, you'd upload to a server or cloud storage.
                image_url = "https://example.com/temp_image.png"  # Placeholder URL
                
                response = process_image_query(image_url, query)
            st.write("Analysis:", response)

st.sidebar.title("About")
st.sidebar.info("This TelecomAI Assistant uses Llama 3.2 models to assist with various telecommunication tasks, including text analysis, document processing, and image analysis.")
