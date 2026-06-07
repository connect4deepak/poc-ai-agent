from langchain import LLMChain, PromptTemplate
from langchain.agents import ReActAgent
from langchain.tools import Tool
from tools import GoogleSearchTool, WikipediaTool, CalculatorTool

class CustomReActAgent(ReActAgent):
    def __init__(self):
        tools = [
            Tool(name='google', func=GoogleSearchTool().search),
            Tool(name='wiki', func=WikipediaTool().search),
            Tool(name='calc', func=CalculatorTool().calculate)
        ]
        super().__init__(tools=tools)

    def run(self, input):
        return self.agent.run(input)
