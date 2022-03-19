import random

computer_pick = random.randint(1, 10)
user_pick = int(input("Pick a number 1-10"))

def random_number(user_pick, computer_pick):
  if(computer_pick == user_pick):
    return "You and the computer picked the same number."
  elif(computer_pick > user_pick):
    return "The computer picked a great number than you."
  elif(user_pick > computer_pick):
    return "You picked a number greater than the computer."

random_generator = random_number(user_pick, computer_pick)


print("You picked " + str(user_pick) + "." + " The computer picked " + str(computer_pick) + ".")
print(random_generator)