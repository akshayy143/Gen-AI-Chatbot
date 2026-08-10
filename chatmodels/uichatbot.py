


# import streamlit as st
# from langchain.chat_models import init_chat_model
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

st.set_page_config(page_title="Gen AI Chatbot", page_icon="🤖")

st.title("🤖 Gen AI Chatbot")
st.caption("Funny AI Agent By Ak")


# model = init_chat_model(
#     "google_genai:gemini-3.5-flash-lite",
#     api_key=st.secrets["GOOGLE_API_KEY"]
# )

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=st.secrets["GOOGLE_API_KEY"],
)


if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny AIagent")
    ]


# Show old chat messages
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.text)


# Chat input
prompt = st.chat_input("Type your message...")


if prompt and prompt != "0":
    # Save and display user message
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.write(prompt)

    # Get and display AI response
    with st.chat_message("assistant"):
        response = model.invoke(st.session_state.messages)
        st.write(response.text)

    # Save the complete Gemini response, including its signature
    st.session_state.messages.append(response)