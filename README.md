# I put this so it can choose a random option where ever it says choice
from random import choice

# started the function
def get_joke_bot_response(user_response):
 # made two variables each containing a list for possible options
    response_dad_joke = ["If you see a crime at an Apple Store does that make you an iWitness!", 
    "What’s an astronaut’s favorite part of a computer The space bar.", 
    "Wanna hear a joke about paper? Never mind—it's tearable."]
    response_funny_joke = ["How do you have a major in finance and be broke?", 
    "A communist joke isn't funny unless everyone gets it", 
    "What do you call a psychic little person who has escaped from prison? A small medium at large"] 
 # Made an if statment so if the user types dad joke or funny joke it will give them the selected joke and if they didint type dad joke or funny joke it just tells you that it doesint have that type
    if user_response == "dad joke":
        return choice(response_dad_joke)
    elif user_response == "funny joke":
            return choice(response_funny_joke)
    else:
            return "I dont have that type of joke"
# here printts out the welcome message and the choices to type out
print("Welcome to Joke bot")
print("Please choose either Dad joke or Funny joke")
# made this variable so it can store what the user put
user_response = ""
# I put this while loop so the code can keep running if not prompted done
while user_response != "done":
  user_response = input("Please choose one: ")
  # put this so if user typed done the code will stop working 
  if user_response == "done":
    break

  # I made the bot response variable so it can store the users response and thus move on with the code
  bot_response = get_joke_bot_response(user_response)
  print(bot_response)
