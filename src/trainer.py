import json
from chatbot import SimpleChatbot

def train_bot_from_file(filename, bot):
    try:
        with open(filename, 'r') as file:
            training_data = json.load(file)
            for question, answer in training_data.items():
                bot.learn_from_interaction(question, answer, replace=True)
        bot.save_responses()
        print("Training completed successfully.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")

if __name__ == "__main__":
  bot = SimpleChatbot()
  bot.load_responses()
  train_bot_from_file("training_data.json", bot)
