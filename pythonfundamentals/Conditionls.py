#Conditional 
#Method evaluate data 
# if then else 
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


import random
#ask the user to select the upper bound
upper_bound = input("What is the upper bound? ")
upper_bound = int(upper_bound)

#generate a random integer starting at 1 and going to upper_bound 
random_number = random.randint(1, upper_bound) 
print(random_number)

user_guess = None
#start and loop here 
while user_guess != random_number:
    #ask the user to guess 
    user_guess = input("what number do you guess between 1 and " + str(upper_bound) + ": ")

    #check if user guess is = to random number

    if int(user_guess) == random_number:
        print("You Win!! ")
        #exit the loop
    if int(user_guess) != random_number:
        print("you lose")
print("Game Over.")

# high_range = 100
# mid_range = (high_range/2)
# my_guess = mid_range
# number_guesses = 0
# HighOrLow = "lower"
# output = "{} is {} than {}"

# my_random_number = random.randint(1, high_range)

# print(my_random_number)
# print(my_guess)



# #evaluate the random number and compare it to middle number 
# if my_random_number > my_guess :
#     HighOrLow = "lower"

# if my_random_number < my_guess :
#     HighOrLow = "higher"

# if my_random_number == my_guess :
#     print(f"you got the number I was thinking of")

# print(output.format(my_guess, HighOrLow, my_random_number))