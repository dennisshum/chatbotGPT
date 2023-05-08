import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import streamlit as st

os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0.9)

memory = ConversationBufferMemory()

chain = ConversationChain(llm=llm, memory=memory, verbose=False)

print("Howdy!")

while True:
  user_input = input("> ")

  ai_response = chain.run(user_input)

  print("\nAssistant:\n", ai_response)

