# 🤖 AI Research Assistant

An AI-powered research assistant built with **Streamlit, LangChain, Groq, and external research tools**.

The application allows users to ask questions and intelligently searches different sources to provide useful and research-oriented answers.

## ✨ Features

* 🔎 **Web Search** using DuckDuckGo
* 📖 **Wikipedia Search** for encyclopedia-style information
* 📚 **arXiv Search** for academic research papers
* 🧠 **AI-powered responses** using Groq
* 🤖 **LangChain Agent** for intelligent tool selection
* 💬 **Chat interface** with conversation history
* ⚡ **Streaming responses**
* 🌙 **Modern dark-themed UI**
* 🎨 Custom Streamlit CSS styling
* 🔐 API key input through the Streamlit sidebar

## 🛠️ Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core programming language       |
| Streamlit     | Web application and UI          |
| LangChain     | Agent and tool orchestration    |
| Groq          | LLM inference                   |
| DuckDuckGo    | Web search                      |
| Wikipedia     | General knowledge search        |
| arXiv         | Research paper search           |
| python-dotenv | Environment variable management |

## 🏗️ How It Works

The application follows this basic workflow:

```text
User Question
      ↓
Streamlit Chat Interface
      ↓
LangChain AI Agent
      ↓
Selects Appropriate Tool
      ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
DuckDuckGo    Wikipedia         arXiv
 ↓               ↓               ↓
 └───────────────┴───────────────┘
                 ↓
             Groq LLM
                 ↓
          Final AI Response
```

The agent has access to three tools:

1. **DuckDuckGo** — for general and current web information
2. **Wikipedia** — for encyclopedia-style information
3. **arXiv** — for academic and research papers

## 📂 Project Structure

```text
AI-Research-Assistant/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> Your main Python file can have a different name. If your file is named something other than `app.py`, replace `app.py` in the instructions below.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Research-Assistant.git
cd AI-Research-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Groq API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Alternatively, you can enter your Groq API key directly into the **Groq API Key** field in the application's sidebar.

> ⚠️ Never upload your real API key to GitHub.

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔑 API Key

This project uses the **Groq API** to access the language model.

You can obtain an API key from Groq and provide it through the application's sidebar.

For local development, you can also store it in a `.env` file.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

Make sure `.env` is included in `.gitignore`.

## 🧠 Model

The application currently uses:

```text
openai/gpt-oss-120b
```

through the Groq API.

The model is used by the LangChain agent to understand the user's question, select the appropriate research tool, and generate the final response.

## 🔧 Available Tools

### 🌐 DuckDuckGo

Used for general web searches and current information.

```python
DuckDuckGoSearchRun(name="search")
```

### 📖 Wikipedia

Used for encyclopedia-style searches.

```python
WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(...)
)
```

### 📚 arXiv

Used to search academic and scientific research papers.

```python
ArxivQueryRun(
    api_wrapper=ArxivAPIWrapper(...)
)
```

## 💬 Example Queries

Try asking questions such as:

```text
Explain Retrieval-Augmented Generation.

What are the latest approaches in Generative AI?

Explain transformer architecture.

What is attention mechanism in deep learning?

Find research papers about large language models.

What is Retrieval-Augmented Generation and how does it work?
```

## 🎨 User Interface

The application includes:

* Dark gradient background
* AI Research Assistant header
* Source and model information cards
* Sidebar settings
* Connected tools section
* Chat history
* Custom chat input
* AI response cards
* Search/status indicators

## 🔒 Security

Do not commit sensitive credentials to GitHub.

Add the following to your `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

If you use Streamlit Cloud, add your API key through **Streamlit Secrets** instead of committing it to your repository.

## ☁️ Deployment

This application can be deployed using **Streamlit Community Cloud**.

Basic deployment steps:

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Select your GitHub repository.
4. Select the main Python file.
5. Add your `GROQ_API_KEY` under Streamlit Secrets.
6. Deploy the application.

Example Streamlit secret:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

## 📦 Requirements

A typical `requirements.txt` for this project should include:

```text
streamlit
python-dotenv
langchain
langchain-community
langchain-groq
langchain-classic
duckduckgo-search
wikipedia
arxiv
```

If your local project already has a working `requirements.txt`, use that file as the source of truth rather than replacing it blindly.

## 🎯 Future Improvements

Possible improvements for future versions:

* 📑 PDF/document research
* 🧠 RAG-based document question answering
* 💾 Persistent chat history
* 📚 Multiple research sources
* 🔗 Source citations in responses
* 📊 Research result summarization
* 📥 Export answers as PDF/Markdown
* 🌐 More search providers
* ⚙️ Model selection
* 📝 Automatic research report generation

## 📸 Demo



## 👩‍💻 Author

**Jiya Dhillon**

Built with:

**Python • Streamlit • LangChain • Groq**

---

⭐ If you find this project useful, consider giving the repository a star!
