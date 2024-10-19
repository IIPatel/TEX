# TEX: Telecom AI Assistant 📡

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://texai-llama.streamlit.app)

## Overview

TEX: Telecom AI Assistant is a versatile Streamlit application designed to assist with various telecommunication tasks. Leveraging advanced AI models, including the Llama 3.2 series, this app can process text queries, analyze documents, and interpret images. It is a powerful tool for professionals in the telecommunications industry seeking efficient and accurate data processing solutions.

## Features ✨

- **Text Query Processing**: Enter text queries and receive detailed responses.
- **Document Analysis**: Analyze regulatory documents, contracts, and customer inquiries.
- **Image Analysis**: Upload and analyze satellite imagery or equipment photos.
- **AI Integration**: Powered by Llama 3.2 models for advanced AI capabilities.

## Installation 🛠️

1. Clone the repository:
   ```sh
   git clone https://github.com/IIPatel/TEX.git
   ```

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

3. Store your AIML API key in the Streamlit secrets. Create a .streamlit/secrets.toml file with the following content:
   ```
   $ AIML_API_KEY = "your_api_key_here"
   ```
## How It Works 🧠

### Text Query

1. **Select "Text Query"**: Choose the "Text Query" option from the task type radio buttons.
2. **Enter Your Query**: Type your query into the text input field.
3. **Process the Query**: Click the "Process Query" button to submit your query.
4. **Receive Response**: The app processes your query using the Llama 3.2 model and displays a detailed response.

### Document Analysis

1. **Select "Document Analysis"**: Choose the "Document Analysis" option from the task type radio buttons.
2. **Choose Document Type**: Select the type of document you want to analyze (Regulatory Document, Contract, Customer Inquiry).
3. **Enter Document Text**: Paste the text of the document into the text area provided.
4. **Analyze Document**: Click the "Analyze Document" button to submit the document for analysis.
5. **View Analysis**: The app processes the document using the Llama 3.2 model and provides a detailed analysis, highlighting key points and insights.

### Image Analysis

1. **Select "Image Analysis"**: Choose the "Image Analysis" option from the task type radio buttons.
2. **Choose Image Type**: Select the type of image you want to analyze (Satellite Imagery, Equipment Photo).
3. **Upload Image**: Use the file uploader to select and upload an image file (jpg, png, jpeg).
4. **Enter Analysis Query**: Type your analysis query into the text input field.
5. **Analyze Image**: Click the "Analyze Image" button to submit the image for analysis.
6. **View Analysis**: The app converts the image to base64 format, processes it using the Llama 3.2 model, and provides a detailed analysis based on your query.

---



