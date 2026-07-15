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

# Tools

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)

wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

arxiv_wrapper = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=250)

arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

search = DuckDuckGoSearchRun(name="Search")

tools = [search, wiki, arxiv]


# Streamlit UI

st.title("🔎 LangChain - Chat with Search")

st.sidebar.title("Settings")

api_key = st.sidebar.text_input(
    "Enter your Groq API Key",
    type="password"
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

if prompt := st.chat_input("Ask me anything..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    st.chat_message("user").write(prompt)

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="Llama3-8b-8192",
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

        response = agent.invoke(
            {
                "messages": st.session_state.messages
            },
            config={
                "callbacks": [st_cb]
            }
        )

        assistant_response = response["messages"][-1].content

        st.write(assistant_response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )