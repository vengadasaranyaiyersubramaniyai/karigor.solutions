from nvidia_jarvis import JarvisAPI

class Jarvis:
    def __init__(self):
        self.jarvis = JarvisAPI()

    def generate_response(self, user_input):
        # Use Nvidia Jarvis API to generate response
        response = self.jarvis.generate_response(user_input)
        return response
