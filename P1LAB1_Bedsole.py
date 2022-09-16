# CTI 110
# P1T1 - Take 2
# Matthew Bedsole
# 9/13/22

# Write a program to greet the user
print("Hello!")
name = input("What's your name? ")
print("Nice to meet you,", name)

# now ask them something else
salary=int(input("What is your yearly salary? "))

if salary <= 10000:
  print(salary,"? that's embarassing...",sep="")
  
else: print("Wow, impressive!")