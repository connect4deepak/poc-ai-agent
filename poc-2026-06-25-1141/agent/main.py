from langchain.agents import ReActAgent
from langchain.tools import Tool
from agent.tools import CustomTool1, CustomTool2, CustomTool3

agent = ReActAgent(
    tools=[CustomTool1(), CustomTool2(), CustomTool3()],
    verbose=True
)

agent.run()