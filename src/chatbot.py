import json
import random
class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": [("Hello there!", 1)],
            "how are you": [("I'm just a simple bot, but I'm doing fine!", 1)],
            "bye": [("Goodbye!", 1)]
        }
        self.context = []
        self.contractions = {}
    def say(self, text):
        print("Bot:" + text)

    def get_response(self, input_text):
        input_text = input_text.lower().strip()
        input_text = self.expand_contractions(input_text)
        self.context.append(input_text)
        nearest_response = self.find_nearest_response(input_text)
        return nearest_response if nearest_response else "I don't understand that."

    def learn_from_interaction(self, input_text, expected_response, replace=False):
        input_text = input_text.lower().strip()
        if replace:
            self.responses[input_text] = [(expected_response, 1)]
        else:
            self.responses.setdefault(input_text, []).append((expected_response, 1))
        self.save_responses()

    def expand_contractions(self, text):
        for contraction, expanded in self.contractions.items():
            text = text.replace(contraction, expanded)
        return text

    def find_nearest_response(self, user_input):
      user_input_words = set(user_input.lower().split())
      max_match_count = 0
      nearest_response_key = None
      for question in self.responses.keys():
          question_words = set(question.lower().split())
          match_count = len(user_input_words.intersection(question_words))
          if match_count > max_match_count:
              max_match_count = match_count
              nearest_response_key = question
      if nearest_response_key:
            responses = self.responses[nearest_response_key]
            # If multiple responses, randomly select one
            best_response = random.choice([resp for resp, weight in responses])
            return best_response
      else:
          return "I don't understand that."

    def save_responses(self):
        with open("responses.json", "w") as f:
            json.dump(self.responses, f, indent=4, sort_keys=True)

    def load_responses(self):
        try:
            with open("responses.json", "r") as f:
                self.responses = json.load(f)
                print("Loaded responses...")
        except FileNotFoundError:
            pass  # No saved data to load

    def load_contractions(self):
        try:
            with open("contractions.json", "r") as f:
                self.contractions = json.load(f)
                # print("Loaded contractions:", self.contractions)
                print("Loaded contractions...")
        except FileNotFoundError:
            pass # File not found, continue with default contractions
    
    def save_contractions(self):
        with open("contractions.json", "w") as f:
            json.dump(self.contractions, f, indent=4, sort_keys=True)

    def load_data(self):
        self.load_responses()
        self.load_contractions()

    def save_data(self):
        self.save_responses()
        self.save_contractions()