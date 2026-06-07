import requests

class GoogleSearchTool:
    def search(self, query):
        url = 'https://www.google.com/search'
        params = {'q': query}
        response = requests.get(url, params=params)
        return response.text

class WikipediaTool:
    def search(self, query):
        url = 'https://en.wikipedia.org/w/api.php'
        params = {'action': 'opensearch', 'search': query}
        response = requests.get(url, params=params)
        return response.json()[3][0]

class CalculatorTool:
    def calculate(self, expression):
        try:
            return eval(expression)
        except Exception as e:
            return str(e)
