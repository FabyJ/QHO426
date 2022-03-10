import random 

minimum = int(input("Please enter the minimum value: "))
maximum = int(input("Please enter the maximum value: "))

x = random.randrange(minimum, maximum)
print(f"I am thinking of a number between {minimum} and {maximum}.Can you guess what it is?")

while True:
  guess = int(input("Have a guess:"))
  if guess < x:
    print("Your guess is to low.")
  elif guess > x:
    print("Your guess is to high.")
  else:
    break
  print("Let's try again! ")
print("Congratulations! you guesse my number!")
