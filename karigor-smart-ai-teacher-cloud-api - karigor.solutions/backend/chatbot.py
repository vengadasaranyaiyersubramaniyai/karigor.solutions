from jarvis_api import Jarvis

class Chatbot:
    def __init__(self):
        self.jarvis = Jarvis()

    def get_response(self, user_input):
        # Implement chatbot logic here
        response = self.jarvis.generate_response(user_input)
        return response
