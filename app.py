import streamlit as st
import os
import sys
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Ensure project root is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import models
from models.llm import get_chatgroq_model  # add get_openai_model, get_gemini_model in llm.py
from config.config import OPENAI_API_KEY, GROQ_API_KEY, GEMINI_API_KEY


def get_chat_response(chat_model, messages, system_prompt):
    """Get response from the chat model"""
    try:
        formatted_messages = [SystemMessage(content=system_prompt)]
        for msg in messages:
            if msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            else:
                formatted_messages.append(AIMessage(content=msg["content"]))

        response = chat_model.invoke(formatted_messages)
        return response.content
    except Exception as e:
        return f"⚠️ Error getting response: {str(e)}"


def instructions_page():
    """Instructions and setup page"""
    st.title("📘 The Chatbot Blueprint")
    st.markdown("Welcome! Follow these instructions to set up and use the chatbot.")

    st.markdown("""
    ## 🔧 Installation
    ```bash
    pip install -r requirements.txt
    ```

    ## API Key Setup
    - **OpenAI** → [OpenAI Platform](https://platform.openai.com/api-keys)  
    - **Groq** → [Groq Console](https://console.groq.com/keys)  
    - **Google Gemini** → [AI Studio](https://aistudio.google.com/app/apikey)  

    ## 📝 Popular Models
    - **OpenAI**: `gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo`  
    - **Groq**: `llama-3.1-70b-versatile`, `llama-3.1-8b-instant`, `mixtral-8x7b-32768`  
    - **Gemini**: `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-pro`  

    ## How to Use
    1. Navigate to the **Chat** page (sidebar).  
    2. Start chatting once API keys are configured.  
    3. Clear chat history anytime using the sidebar button.  

    ## Troubleshooting
    - Invalid API key → regenerate key and update environment.  
    - Wrong model name → check provider documentation.  
    - Connection errors → check internet/API service status.  

    ---
    🚀 Ready? Go to the **Chat** page in the sidebar!
    """)


def chat_page():
    """Main chat interface"""
    st.title("🤖 Multi-Provider AI ChatBot")

    # Default system prompt
    system_prompt = "You are a helpful AI assistant. Respond politely and clearly."

    # Detect provider
    provider = None
    chat_model = None
    if GROQ_API_KEY:
        provider = "Groq"
        chat_model = get_chatgroq_model()
    elif OPENAI_API_KEY:
        provider = "OpenAI"
        # chat_model = get_openai_model()  # implement in llm.py
    elif GEMINI_API_KEY:
        provider = "Gemini"
        # chat_model = get_gemini_model()  # implement in llm.py

    if not chat_model:
        st.error("❌ No API keys found! Please configure them in `config/config.py` or as environment variables.")
        st.stop()

    st.success(f"✅ Connected to {provider}")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_chat_response(chat_model, st.session_state.messages, system_prompt)
                st.markdown(response)

        # Save bot message
        st.session_state.messages.append({"role": "assistant", "content": response})


def main():
    st.set_page_config(
        page_title="LangChain Multi-Provider ChatBot",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Sidebar navigation
    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to:", ["Chat", "Instructions"], index=0)

        if page == "Chat":
            st.divider()
            if st.button("🗑️ Clear Chat History", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

    if page == "Instructions":
        instructions_page()
    elif page == "Chat":
        chat_page()


if __name__ == "__main__":
    main()
