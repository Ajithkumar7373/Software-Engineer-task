
# 🧠 LLM Chatbot API (FastAPI + LangChain + Ollama)

This project is a simple RESTful chatbot service built with **FastAPI** and **LangChain**, using the **Ollama**-hosted `gemma:2b` model to generate answers to user questions.

---

## 🚀 Features

- RESTful API using FastAPI
- CORS enabled for cross-origin access
- Chat endpoint `/ask` for question answering
- Swagger UI at `/docs`
- Powered by LangChain and `gemma:2b` via Ollama

---

## 🧩 Tech Stack

- Python 3.10+
- FastAPI
- LangChain
- Ollama LLM (`gemma:2b`)
- Uvicorn (ASGI server)

---

## 📁 Project Structure

```
llm_chatbot/
├── main.py              # FastAPI app with /ask endpoint
├── config.py            # CORS setup
├── get_response.py      # LLM response logic
└── README.md            # Project documentation
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/llm-chatbot.git
cd llm-chatbot
```

### 2. Create and activate virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn langchain langchain-community
```

### 4. Start Ollama with `gemma` model

Make sure [Ollama](https://ollama.com) is installed and the `gemma:2b` model is available.

```bash
ollama run gemma:2b
```

Or pull it if needed:

```bash
ollama pull gemma:2b
```

---

## ▶️ Running the API

```bash
uvicorn main:app --reload
```

Visit Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📬 Example Request

### Endpoint: `POST /ask`

**Request body:**

```json
{
  "question": "What is LangChain?"
}
```

**Response:**

```json
{
  "answer": "LangChain is a framework for developing applications powered by language models..."
}
```

---

## 🛡️ License

MIT License. Free to use and modify.

---

## 🤝 Contributing

Pull requests and suggestions are welcome!

---

## 📞 Contact

Made with ❤️ by [Your Name]
