import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"  # FastAPI endpoint

def get_chat_response(messages, system_prompt):
    """Send chat messages to FastAPI and get the response"""
    payload = {
        "system_prompt": system_prompt,
        "messages": messages
    }
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            return f"⚠️ API error {response.status_code}: {response.text}"
    except Exception as e:
        return f"⚠️ Error connecting to API: {str(e)}"

# Sidebar navigation
st.set_page_config(page_title="Multi-Provider AI ChatBot", page_icon="🤖", layout="wide")
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to:", ["Chat", "Instructions"])

# Instructions page
def instructions_page():
    st.title("📘 The Chatbot Blueprint")
    st.markdown("""
    ## 🔧 Installation
    ```bash
    pip install -r requirements.txt
    ```
    ## API Key Setup
    - **OpenAI** → [OpenAI](https://platform.openai.com/api-keys)
    - **Groq** → [Groq](https://console.groq.com/keys)
    - **Google Gemini** → [AI Studio](https://aistudio.google.com/app/apikey)
    """)

# Chat page
def chat_page():
    st.title("🤖 Multi-Provider AI ChatBot")
    system_prompt = "You are a helpful AI assistant. Respond politely and clearly."

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_chat_response(st.session_state.messages, system_prompt)
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Page navigation
if page == "Instructions":
    instructions_page()
elif page == "Chat":
    chat_page()
