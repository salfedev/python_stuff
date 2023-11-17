class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello there!",
            "how are you": "I'm just a simple bot, but I'm doing fine!",
            "bye": "Goodbye!"
        }

    def get_response(self, input_text):
        # Normalize the input text
        input_text = input_text.lower().strip()
        nearst_result = self.find_nearest_response(input_text)
        # Check if the input is in the predefined responses
        if nearst_result:
            return nearst_result
        else:
            return self.responses.get(input_text, "I don't understand that.")

    def learn_from_interaction(self, input_text, expected_response):
        # Normalize and learn
        input_text = input_text.lower().strip()
        self.responses[input_text] = expected_response
        self.save_responses()

    def save_responses(self):
        # Save the responses to a file
        with open("responses.txt", "w") as f:
            for key, value in self.responses.items():
                f.write(f"{key}:{value}\n")

    def load_responses(self):
        # Load the responses from a file
        with open("responses.txt", "r") as f:
            for line in f:
                key, value = line.split(":")
                self.responses[key] = value.strip()
    
    def find_nearest_response(self, user_input):
      user_input = set(user_input.lower().split())
      max_common_words = 0
      nearest_response_key = None

      for question in self.responses.keys():
          question_words = set(question.lower().split())
          common_words = len(user_input.intersection(question_words))

          if common_words > max_common_words:
              max_common_words = common_words
              nearest_response_key = question

      return self.responses[nearest_response_key] if nearest_response_key else "I don't understand that."


# Example usage
bot = SimpleChatbot()
bot.load_responses()


old_input = None  # Initialize old_input outside the loop

while True:
    bad_answer = ["wrong", "no", "nope"]
    good_answer = ["yes", "yep", "correct"]
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        bot.save_responses()
        break
    if user_input.lower() == "skip":
        continue

    for answer in bad_answer:
      if answer in user_input.lower() and old_input:
          correct_response = input("What should I have said? ")
          bot.learn_from_interaction(old_input, correct_response)
          bot.save_responses()

    response = bot.get_response(user_input)
    print("Bot:", response)

    if response == "I don't understand that.":
        correct_response = input("What should I have said? ")
        bot.learn_from_interaction(user_input, correct_response)
    
    # Update old_input at the end of the loop
    old_input = user_input
