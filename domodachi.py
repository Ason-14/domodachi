import random

# character class and constructor
class Character:
  def __init__(self, name, personality):
    self.name = name
    self.personality = personality
    self.relationships = {} # exists but not initialised when character constructed

def init_rel(characters):
  for i in characters:
    for j in characters:
      if i != j:
        i.relationships[j.name] = 0


def interact(char1, char2):
    interaction = random.choice(["friendly", "argument"]) # careful: choice() needs a list as parameter
    if interaction == "friendly":
      char1.relationships[char2.name] += 1
      char2.relationships[char1.name] += 1
      print(f"{char1.name} and {char2.name} have grown closer!")
    if interaction == "argument":
      char1.relationships[char2.name] -= 1
      char2.relationships[char1.name] -= 1
      print(f"{char1.name} and {char2.name} had an argument!")

def simulate(characters):
  c1, c2 = random.sample(characters, 2)
  interact(c1, c2)

def main():
  # can build this into a index.html eventually
  print("Welcome to Domodachi! Please enter the name and personality of three characters") 
  name1 = input("Name of Character 1: ")
  personality1 = input("Personality of Character 1: ")
  name2 = input("Name of Character 2: ")
  personality2 = input("Personality of Character 2: ")
  name3 = input("Name of Character 3: ")
  personality3 = input("Personality of Character 3: ")
  
  char1 = Character(name1, personality1)
  char2 = Character(name2, personality2)
  char3 = Character(name3, personality3)

  characters = [char1, char2, char3]

  init_rel(characters)

  for i in range(10):
    simulate(characters)
  
if __name__ == "__main__":
  main()