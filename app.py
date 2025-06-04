from langchain_openai import ChatOpenAI
import streamlit as st #Import streamlit for web app framework

st.title('Basic Chatbot') #App title

openai_api_key = st.sidebar.text_input('OpenAI API Key',type='password') #Field to input OpenAI API key

def generate_response(input_text):
    #Queries OpenAI LLM and returns the generated response
    # Input: 
    #   input_text      prompt from user
    #Output:
    #   output_text     response from llm

    llm = ChatOpenAI(model='gpt-4.1-nano',temperature=0.7, openai_api_key = openai_api_key)
    output_text = llm.invoke(input_text)
    st.info(output_text.content) #Display output in web app

with st.form('my_form'):
    #Build web app framework
    text = st.text_area('Enter Prompt:','') #User prompt field
    submitted = st.form_submit_button('Submit') #User submit entered prompt
    #Check validity of api key and generate resposne if valid
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)