from random import choice


def get_joke_bot_response(user_response):
    response_dad_joke = ["If you see a crime at an Apple Store does that make you an iWitness!", 
    "What’s an astronaut’s favorite part of a computer The space bar.", 
    "Wanna hear a joke about paper? Never mind—it's tearable."]
    response_funny_joke = ["How do you have a major in finance and be broke?", 
    "A communist joke isn't funny unless everyone gets it", 
    "What do you call a psychic little person who has escaped from prison? A small medium at large"] 

    if user_response == "Dad, dad":
        return choice(response_dad_joke)
    elif user_response == "Funny, funny":
            return choice(response_funny_joke)
    else:
            return "I dont have that type of joke"

print("")

