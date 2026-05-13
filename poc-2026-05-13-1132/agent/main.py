from langchain.agents import ReActAgent
from langchain.chains import LLMChain
from langchain.llms import AI21
from langchain.tools import Tool

import os
from dotenv import load_dotenv

load_dotenv()

# Define the AI model
llm = AI21()

# Define the tools
tools = [
    Tool(name='tool1', func=lambda input: 'This is the output of tool1'),
    Tool(name='tool2', func=lambda input: 'This is the output of tool2'),
    Tool(name='tool3', func=lambda input: 'This is the output of tool3')
]

# Create the ReAct agent
agent = ReActAgent(llm=llm, tools=tools, verbose=True)

# Test the agent
input = 'Hello, how are you?'
output = agent.run(input)
print(output)