from langchain.tools import Tool

class CustomTool1(Tool):
    def __init__(self):
        self.name = 'custom_tool_1'
        self.description = 'This is a custom tool 1'

    def run(self, input):
        return 'Custom tool 1 output'

class CustomTool2(Tool):
    def __init__(self):
        self.name = 'custom_tool_2'
        self.description = 'This is a custom tool 2'

    def run(self, input):
        return 'Custom tool 2 output'

class CustomTool3(Tool):
    def __init__(self):
        self.name = 'custom_tool_3'
        self.description = 'This is a custom tool 3'

    def run(self, input):
        return 'Custom tool 3 output'
