from langchain.agents import ReActAgent
from langchain.tools import Tool
from agent.tools import CustomTool1, CustomTool2, CustomTool3

class MyReActAgent(ReActAgent):
    def __init__(self):
        tools = [
            CustomTool1(),
            CustomTool2(),
            CustomTool3()
        ]
        super().__init__(tools=tools)

    def run(self, input):
        return self.react(input)
