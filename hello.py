import random

text = open("poem.txt").readlines()
for line in text:
  line = line.strip()
  words = line.split(" ")

  words = [word for word in words if word.startswith("")]

  new_line = " ".join(words)
    
  print(new_line)
  # prints all the words that start with a