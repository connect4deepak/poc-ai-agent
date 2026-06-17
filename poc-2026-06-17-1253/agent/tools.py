from langchain import Tool

class Tool1(Tool):
    def __init__(self):
        self.name = 'Tool 1'
        self.description = 'This is tool 1'
    def run(self, input):
        return 'Tool 1 output'

class Tool2(Tool):
    def __init__(self):
        self.name = 'Tool 2'
        self.description = 'This is tool 2'
    def run(self, input):
        return 'Tool 2 output'

class Tool3(Tool):
    def __init__(self):
        self.name = 'Tool 3'
        self.description = 'This is tool 3'
    def run(self, input):
        return 'Tool 3 output'