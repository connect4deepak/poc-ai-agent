from langchain.tools import Tool

class SummarizeTool(Tool):
    def __init__(self):
        self.name = 'summarize'
        self.description = 'Summarize a piece of text'
        self.input_type = 'text'
        self.output_type = 'text'

    def _execute(self, input):
        # Use a summarization model or library to summarize the text
        # For demonstration purposes, this example uses a simple string slicing
        return input[:100]

class QuestionAnswerTool(Tool):
    def __init__(self):
        self.name = 'question_answer'
        self.description = 'Answer a question based on a piece of text'
        self.input_type = 'text'
        self.output_type = 'text'

    def _execute(self, input):
        # Use a question answering model or library to answer the question
        # For demonstration purposes, this example returns a static answer
        return 'This is the answer to your question'

class SentimentAnalysisTool(Tool):
    def __init__(self):
        self.name = 'sentiment_analysis'
        self.description = 'Analyze the sentiment of a piece of text'
        self.input_type = 'text'
        self.output_type = 'text'

    def _execute(self, input):
        # Use a sentiment analysis model or library to analyze the sentiment
        # For demonstration purposes, this example returns a static sentiment
        return 'Positive'