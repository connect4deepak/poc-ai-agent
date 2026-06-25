from langchain.tools import Tool

class CustomTool1(Tool):
    def __init__(self):
        self.name = 'custom_tool_1'
        self.description = 'This is a custom tool 1'
        self.metadata = {}

    def _execute(self, input: str) -> str:
        return 'Custom Tool 1 output'

class CustomTool2(Tool):
    def __init__(self):
        self.name = 'custom_tool_2'
        self.description = 'This is a custom tool 2'
        self.metadata = {}

    def _execute(self, input: str) -> str:
        return 'Custom Tool 2 output'

class CustomTool3(Tool):
    def __init__(self):
        self.name = 'custom_tool_3'
        self.description = 'This is a custom tool 3'
        self.metadata = {}

    def _execute(self, input: str) -> str:
        return 'Custom Tool 3 output'