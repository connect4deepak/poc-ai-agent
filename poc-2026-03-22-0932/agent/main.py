from langchain import LLMChain, PromptTemplate
from langchain.agents import ReActAgent
from tools import Tool1, Tool2, Tool3

class CustomReActAgent(ReActAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tools = [Tool1(), Tool2(), Tool3()]

def main():
    agent = CustomReActAgent()
    agent.run()

if __name__ == '__main__':
    main()