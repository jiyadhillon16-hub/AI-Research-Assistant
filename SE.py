import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_community.utilities import (
    WikipediaAPIWrapper,
    ArxivAPIWrapper,
)

from langchain_community.tools import (
    WikipediaQueryRun,
    ArxivQueryRun,
    DuckDuckGoSearchRun,
)

from langchain.agents import create_agent
from langchain_classic.callbacks import StreamlitCallbackHandler

load_dotenv()

st.set_page_config(
    page_title="AI Search Engine",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp{
    background:linear-gradient(135deg,#0F172A,#111827,#1E293B);
    color:white;
}

.block-container{
    padding-top:2rem;
    max-width:1200px;
}

/* Hero */

.hero{

background:linear-gradient(135deg,#2563EB,#7C3AED);

padding:22px;

border-radius:20px;

text-align:center;

box-shadow:0px 10px 40px rgba(0,0,0,.35);

animation:fade 1s;

}

/* Animation */

@keyframes fade{

from{
opacity:0;
transform:translateY(20px);
}

to{
opacity:1;
transform:translateY(0px);
}

}

/* Cards */

.metric-card{

background:rgba(255,255,255,.05);

backdrop-filter:blur(12px);

padding:18px;

border-radius:18px;

text-align:center;

transition:.3s;

border:1px solid rgba(255,255,255,.08);

}

.metric-card:hover{

transform:translateY(-6px);

box-shadow:0px 8px 25px rgba(0,0,0,.3);

}

/* Chat */

.stChatMessage{

background:#111827;

border-radius:18px;

padding:12px;

margin-bottom:15px;

}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#0F172A,#111827);
    border-right:1px solid rgba(255,255,255,.08);
}

/* Make all sidebar text white */
section[data-testid="stSidebar"] *{
    color:white !important;
}

/* API Key input */
section[data-testid="stSidebar"] input{
    background:#1E293B !important;
    color:white !important;
    border-radius:10px !important;
}

/* Sidebar buttons */
section[data-testid="stSidebar"] button{
    border-radius:10px;
}

/* Input */
.stChatInputContainer{
border-radius:20px;
}

/* Footer */
.footer{
text-align:center;
padding:25px;
color:#9CA3AF;
font-size:15px;
}

/* Entire chat input container */
div[data-testid="stChatInput"]{
    background:#000000 !important;
    border:2px solid #ff3b3b !important;
    border-radius:18px !important;
    padding:6px !important;
}

/* Glow on focus */
div[data-testid="stChatInput"]:focus-within{
    box-shadow:0 0 20px rgba(255,59,59,0.6) !important;
    transition:0.3s ease;
}

/* Inner container */
div[data-testid="stChatInput"] > div{
    background:#000000 !important;
}

/* Text area */
div[data-testid="stChatInput"] textarea{
    background:#000000 !important;
    color:white !important;
    border:none !important;
}

/* Placeholder */
div[data-testid="stChatInput"] textarea::placeholder{
    color:#BBBBBB !important;
}

/* Send button */
div[data-testid="stChatInput"] button{
    color:#ff3b3b !important;
}

/* Bottom area behind the chat input */
[data-testid="stBottom"]{
    background:#0F172A !important;
    border-top:none !important;
}

/* Chat input wrapper */
[data-testid="stChatInput"]{
    background:#0F172A !important;
    padding:15px !important;
}

/* Input field */
[data-testid="stChatInput"] textarea{
    background:#000000 !important;
    color:white !important;
    border:2px solid #ff3b3b !important;
    border-radius:15px !important;
}

/* Remove white background from parent */
[data-testid="stBottom"] > div{
    background:#0F172A !important;
}

/* Password input */
section[data-testid="stSidebar"] input{
    background:#1E293B !important;
    color:white !important;
}

/* Eye icon */
section[data-testid="stSidebar"] button svg{
    fill:white !important;
    color:white !important;
}

/* Hover color */
section[data-testid="stSidebar"] button:hover svg{
    fill:#ffffff !important;
    color:#ffffff !important;
}

</style>
""",unsafe_allow_html=True)

# Tools

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)

wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

arxiv_wrapper = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=250)

arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

search = DuckDuckGoSearchRun(name="Search")

tools = [search, wiki, arxiv]

st.markdown("""

<div class="hero">

<h1 style="font-size:50px;">
🤖 AI Research Assistant
</h1>

<p style="font-size:20px;">

Search the Web • Wikipedia • arXiv

Powered by LangChain + Groq

</p>

</div>

""",unsafe_allow_html=True)

col1,col2,col3=st.columns(3)

with col1:
    st.markdown("""
<div class="metric-card">
<h2>🌐</h2>
<h3>Sources</h3>
<h1>3</h1>
</div>
""",unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="metric-card">
<h2>🧠</h2>
<h3>Model</h3>
<h1>GPT-OSS 120B</h1>
</div>
""",unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="metric-card">
<h2>🟢</h2>
<h3>Status</h3>
<h1>Ready</h1>
</div>
""",unsafe_allow_html=True)

st.sidebar.title("⚙ Settings")

st.sidebar.markdown("---")

api_key = st.sidebar.text_input(
    "Groq API Key",
    type="password"
)

st.sidebar.markdown("---")

st.sidebar.markdown("## 🌐 Connected Tools")

st.sidebar.markdown("""

✅ DuckDuckGo

📖 Wikipedia

📚 arXiv

""")

st.sidebar.markdown("---")

st.sidebar.info(
    "Powered by\n\nLangChain + Groq"
)

# Chat History

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I'm a chatbot that can search the web. How can I help you?"
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input

if prompt := st.chat_input("Search anything... Example: Explain Retrieval-Augmented Generation"):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    st.chat_message("user").write(prompt)

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="openai/gpt-oss-120b",
        streaming=True,
    )

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful AI assistant."
    )

    with st.chat_message("assistant"):

        st_cb = StreamlitCallbackHandler(
            st.container(),
            expand_new_thoughts=False,
        )
        with st.status("Searching...",expanded=True) as status:

            st.write("🌐 Searching Web")

            st.write("📖 Reading Wikipedia")

            st.write("📚 Searching arXiv")

            response=agent.invoke(
                {
                    "messages":st.session_state.messages
                },
                config={
                    "callbacks":[st_cb]
                }
         )

            status.update(
                label="Finished",
                state="complete"
            )

            assistant_response = response["messages"][-1].content

            st.markdown("### 🤖 AI Response")

            st.markdown(
            f"""
            <div style="
            background:linear-gradient(135deg,#1E293B,#0F172A);
            padding:25px;
            border-radius:18px;
            border-left:6px solid #3B82F6;
            box-shadow:0px 5px 20px rgba(0,0,0,.3);
            color:white;
            line-height:1.8;
            font-size:16px;
            ">

            {assistant_response}

            </div>
            """,
            unsafe_allow_html=True
            )

            st.session_state.messages.append(
                {
                "role": "assistant",
                "content": assistant_response
                }   
            )
st.markdown("""
<div class="footer">
<hr>
<h3>🚀 AI Research Assistant</h3>
Built using
LangChain • Groq • Streamlit
<br>
Made with ❤️ by Jiya Dhillon
</div>
""",unsafe_allow_html=True)
