from langchain import LLMChain, PromptTemplate
from langchain.agents import ReActAgent
from tools import Tool1, Tool2, Tool3

# Define the prompt template
template = PromptTemplate(
    input_variables=['input'],
    template='You are a helpful assistant. {input}',
)

# Define the LLM chain
llm_chain = LLMChain(llm=None, prompt=template)

# Define the tools
tools = [Tool1(), Tool2(), Tool2()]  # Use Tool2 twice to demonstrate multiple instances

# Define the agent
agent = ReActAgent(llm_chain, tools, verbose=True)

# Test the agent
input = 'Hello, how are you?'
output = agent.run(input)
print(output)
