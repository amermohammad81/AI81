# AI81 – AI Assistant Project

## 📌 Overview
This project is an **AI-powered assistant** built for the AI Engineer assessment.  
It combines **FastAPI**, **LangChain**, **OpenAI GPT-3.5 Turbo**, and **SerpAPI** to provide a conversational agent that can answer user queries, perform web searches, and remember context through conversation memory.

---

## 🛠️ Tech Stack
- **FastAPI** – Backend REST API framework  
- **LangChain** – Conversational agent framework  
- **OpenAI GPT-3.5 Turbo** – Natural language understanding and response generation  
- **SerpAPI (Google Search)** – Real-time web search integration  
- **HTML + JavaScript** – Simple frontend interface  

---

## 📂 Project Structure
```
project/
│── app/
│   └── main.py          # FastAPI backend with LangChain agent
│── frontend/
│   └── index.html       # Web chat interface
│── .env                 # Environment variables (not included in repo)
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
```

---

## ⚙️ Setup & Run Locally


1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory with:
```
OPENAI_API_KEY=your_openai_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

3. Run the backend server:
```bash
uvicorn app.main:app --reload
```

5. Open in your browser:
- `http://127.0.0.1:8000` → API root  
- `http://127.0.0.1:8000/docs` → API documentation (Swagger UI)  

6. Open `frontend/index.html` in your browser to test the assistant.
