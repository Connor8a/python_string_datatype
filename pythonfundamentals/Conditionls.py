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
invalid_upper_bound = True # boolean True of Flase 

while invalid_upper_bound:
    upper_bound = input("What is the upper bound? ")
    #check if uppoer bound is vaild returns -> string 
    if upper_bound.isdigit():
        upper_bound = int(upper_bound)
        invalid_upper_bound = False
    else:
        print("that is not a vaild input.")
    


#generate a random integer starting at 1 and going to upper_bound 
random_number = random.randint(1, upper_bound) 
print(random_number)

invalid_upper_bound = True
user_guess = 0
number_of_guesses = 1
#start and loop here 
while user_guess != random_number:
    user_guess = input("what number do you guess between 1 and " + str(upper_bound) + ": ")
    #check if guess is a digit 

    #check if uppoer bound is vaild returns -> string 
    if user_guess.isdigit():
        user_guess = int(user_guess)
    #check if user guess is = to random number

    if int(user_guess) == random_number:
        print("You Win!! ")
        #exit the loop
    if int(user_guess) != random_number:
        print("you lose")
        number_of_guesses += 1
print(number_of_guesses)

print("Game Over you took " + str(number_of_guesses) + " guesses." )

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