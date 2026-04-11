from langchain import LLMChain, PromptTemplate
from langchain.chains import ReActChain
from langchain.llms import AI21
from tools import Tool1, Tool2, Tool3

# Define the AI model
llm = AI21()

# Define the tools
tools = [Tool1(), Tool2(), Tool3()]

# Define the ReAct chain
chain = ReActChain(llm=llm, tools=tools)

# Run the chain
output = chain.run()
print(output)
