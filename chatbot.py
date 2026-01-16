import streamlit as st
import re
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import AIMessage, BaseMessage

st.set_page_config(page_title="Local AI Chatbot", page_icon="🤖")
st.title("🤖 Local AI Chatbot (LLaMA 3)")
st.caption("Powered by Ollama + LangChain + Streamlit")

SESSION_ID = "streamlit_chat"

if "history" not in st.session_state:
    st.session_state.history = InMemoryChatMessageHistory()

def get_session_history(session_id):
    return st.session_state.history

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{input}")
])

model = ChatOllama(model="llama3")

chain = prompt | model

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input"
)

user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = chain_with_history.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": SESSION_ID}}
        )

        if isinstance(response, AIMessage):
            response_text = response.content
        elif isinstance(response, (list, tuple)):
            ai_messages = [msg for msg in response if isinstance(msg, AIMessage)]
            if ai_messages:
                response_text = ai_messages[-1].content
            else:
                last_msg = response[-1]
                if hasattr(last_msg, 'content'):
                    response_text = last_msg.content
                else:
                    response_text = str(last_msg)
        elif hasattr(response, 'content'):
            response_text = response.content
        elif isinstance(response, str):
            response_text = response
        else:
            response_text = str(response)
            if "AIMessage(content=" in response_text or "AIMessage(content='" in response_text:
                match = re.search(r'AIMessage\(content="([^"]+)"', response_text)
                if not match:
                    match = re.search(r"AIMessage\(content='([^']+)'", response_text)
                if match:
                    response_text = match.group(1)
                else:
                    match = re.search(r'AIMessage\(content=["\'](.*?)["\']', response_text, re.DOTALL)
                    if match:
                        response_text = match.group(1)

        st.markdown(response_text)
