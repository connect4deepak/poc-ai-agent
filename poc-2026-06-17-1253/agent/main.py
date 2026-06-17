from langchain import ReActAgent
from tools import Tool1, Tool2, Tool3

agent = ReActAgent(tools=[Tool1(), Tool2(), Tool3()])
agent.run()