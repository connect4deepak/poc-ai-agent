from langchain.tools import Tool

tool1 = Tool(name='tool1', func=lambda input: 'This is the output of tool1')
tool2 = Tool(name='tool2', func=lambda input: 'This is the output of tool2')
tool3 = Tool(name='tool3', func=lambda input: 'This is the output of tool3')