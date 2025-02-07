import streamlit as st
import requests

st.title("AI API Connector")

# Create a text input for API key
api_key = st.text_input("Enter API Key", type="password")

# Create a dropdown menu for API selection
api_options = ["Gemini API", "Our AI API"]
selected_api = st.selectbox("Select API", api_options)

# Create a text input for Gemini API chat
gemini_chat = st.text_area("Gemini API Chat", height=150)

# Create a text input for Our AI chat
our_ai_chat = st.text_area("Our AI Chat", height=150)

# Create a new text input with a unique label
new_text_input = st.text_input("Enter some text for API")

# Create a status indicator. Initialize as disconnected. Define it *before* the button.
status = st.text("Status: Disconnected")

# Create a button to send the text to FastAPI
if st.button("Send to FastAPI"):
    try:
        response = requests.post("http://127.0.0.1:8000/process_text", json={"text": new_text_input}, timeout=5)
        response.raise_for_status()
        data = response.json()
        st.write("Processed Message:")
        st.write(data["processed_text"])
    except requests.exceptions.ConnectionError as e:
        st.error(f"Connection error: {e}")
    except requests.exceptions.Timeout as e:
        st.error(f"Timeout error: {e}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request error: {e}")