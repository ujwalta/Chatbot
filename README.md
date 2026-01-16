🤖 Local AI Chatbot (LLaMA 3)

This project is a local AI chatbot built using LLaMA 3, Ollama, LangChain, and Streamlit. It can chat with context, remembering previous messages, and runs entirely locally — no API keys needed.

🛠️ Features

Chatbot powered by LLaMA 3 (via Ollama)

Context-aware conversation using LangChain memory

Built with Streamlit for an interactive chat interface

Fully local — no internet API required

Clean AI output — no memory objects shown

📂 Project Structure
chatbot/
│
├── chatbot_streamlit.py       # Main Streamlit chatbot code
└── README.md                  # Project README

⚡ How to Run

Install Python dependencies

pip install -r requirements.txt


Start Ollama server

ollama serve


Run Streamlit app

streamlit run chatbot_streamlit.py


Open in your browser at:

http://localhost:8501

📝 Usage

Type a message in the input box.

The chatbot responds while remembering previous messages.

Example:

User: What is AI?
AI: Artificial Intelligence (AI) refers to computer systems...


💡 Note: Running locally may be a bit slow depending on the model size (e.g., LLaMA 3 8B vs 70B).

🧰 Tech Stack

Python 3.x

Streamlit (Frontend)

LangChain 1.x (Conversation & memory management)

Ollama + LLaMA 3 (Local AI model)

🚀 Next Steps / Improvements

Streaming responses like ChatGPT (typing effect)

Multiple sessions / users support

Custom prompts or persona for the AI
