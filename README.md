# AnalytIQ – AI-Powered General Purpose Research Assistant

[![Flask](https://img.shields.io/badge/Flask-2.3+-blue.svg)](https://flask.palletsprojects.com/)  
[![Python](https://img.shields.io/badge/Python-3.9+-yellow.svg)](https://www.python.org/)  
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-purple.svg)](https://www.langchain.com/)  

AnalytIQ is a web-based AI assistant built using **Flask** and **Google’s Gemini API**, enhanced with **prompt engineering** for a professional assistant persona.  
It integrates **Wikipedia** and **DuckDuckGo Search** to deliver accurate, up-to-date, and context-aware research assistance.

🔗 **Live Demo:** [https://langhchain-flask-project.onrender.com/](https://langhchain-flask-project.onrender.com/)  
💻 **GitHub Repo:** [https://github.com/mayur1gawande/AnalytIQ](https://github.com/mayur1gawande/AnalytIQ)  

---

## 🚀 Features

- **Conversational AI** – Powered by Google’s Gemini API with a carefully engineered persona prompt.
- **Tool-Augmented Intelligence** – Wikipedia and DuckDuckGo Search APIs for factual, up-to-date answers.
- **Adjustable Explanation Length** – Short, medium, or long responses.
- **Modern UI** – Dark-mode chat interface inspired by ChatGPT.
- **Real-Time Interaction** – Instant responses with smooth scrolling and dynamic message rendering.
- **Branding** – Custom logo, LinkedIn, and GitHub links.

---

## 🛠 Tech Stack

**Backend:**
- Flask
- Langchain
- Google Gemini API
- Wikipedia API
- DuckDuckGo Search API

**Frontend:**
- HTML5, CSS3 (Dark Theme)
- JavaScript (Async Fetch API)

**Deployment:**
- Hosted on **Render**

---

## 📂 Project Structure
<details>
<summary>Click to expand</summary>

```text
AnalytIQ/
│
├── static/
│   ├── assistant.png       # Logo icon for the chat avatar
│   ├── github_icon.png     # GitHub link icon
│   ├── linkedin_icon.jpeg  # LinkedIn link icon
│   ├── script.js           # Frontend JavaScript logic
│   └── style.css           # UI styling (dark mode)
│
├── templates/
│   └── index.html          # Main chat UI template
│
├── analytIQ_persona_prompt.txt  # Custom persona prompt for Gemini API
├── app.py                   # Flask app entry point
├── logo.png                 # App logo
├── model.py                 # Gemini API + prompt engineering logic
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```
</details>

---

## ⚙ Installation

1. **Clone the repository**
```bash
git clone https://github.com/mayur1gawande/Langhchain-flask-project.git
cd Langhchain-flask-project
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your API key**

### 🔑 Environment Variables
Create a `.env` file in the project root:
```
GEMINI_API_KEY= "your_api_key_here"
```
* The app uses `python-dotenv` to load this automatically.

5. **Run the application**

```bash
python -m app.py
```

6. Open your browser and visit:

```bash
http://127.0.0.1:5000
```

---

## 📌 Usage

* Type your query into the input box.
* Select your desired explanation length.
* Hit **SEND** and get real-time AI-powered responses.
* Supports research queries, explanations, and knowledge lookups.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 👤 Author

**Mayur Suresh Gawande**
🔗 [LinkedIn](https://www.linkedin.com/in/mayurgawande/) | [GitHub](https://github.com/mayur1gawande)
