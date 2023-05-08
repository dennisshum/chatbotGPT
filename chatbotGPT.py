import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0.9)

memory = ConversationEntityMemory(llm=llm)

chain = ConversationChain(llm=llm, memory=memory, prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE, verbose=False)

print("Howdy!")

while True:
  user_input = input("> ")

  response = chain.run(user_input)

  print("\nAssistant:\n", response)

