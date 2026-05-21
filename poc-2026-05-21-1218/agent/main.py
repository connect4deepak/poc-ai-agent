from langchain import LLMChain, PromptTemplate
from langchain.chains import ReActChain
from langchain.llms import AI21
from tools import SummarizeTool, QuestionAnswerTool, SentimentAnalysisTool

# Initialize the AI model
llm = AI21()

template = PromptTemplate(
    input_variables=['text'],
    template='Summarize the following text: {text}',
)
summarize_chain = LLMChain(llm=llm, prompt=template)

# Initialize the ReAct agent
agent = ReActChain(
    llm=llm,
    tools=[SummarizeTool(), QuestionAnswerTool(), SentimentAnalysisTool()],
    verbose=True
)

# Test the agent
agent.run()