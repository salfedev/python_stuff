from chatbot import SimpleChatbot

if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.load_data()

    old_input = None
    bot.say("Wellcome to version 0.2, motherfuckers!!")
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "exit":
            bot.say(bot.find_nearest_response('Goodbye!'))
            bot.save_data()
            break

        if "wrong" in user_input and old_input:
            correct_response = input("What should I have said? ")
            replace = input("Should I replace the old answer? (yes/no) ").lower() == "yes"
            bot.learn_from_interaction(old_input, correct_response, replace)
            continue

        response = bot.get_response(user_input)
        bot.say(response)

        if response == "I don't understand that.":
            correct_response = input("How should I respond to that? ")
            bot.learn_from_interaction(user_input, correct_response)
        
        old_input = user_input