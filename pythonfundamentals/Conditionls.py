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
import random

high_range = 100
mid_range = (high_range/2)
my_guess = mid_range
number_guesses = 0
HighOrLow = "lower"
output = "{} is {} than {}"

my_random_number = random.randint(1, high_range)

print(my_random_number)
print(my_guess)



#evaluate the random number and compare it to middle number 
if my_random_number > my_guess :
    HighOrLow = "lower"

if my_random_number < my_guess :
    HighOrLow = "higher"

if my_random_number == my_guess :
    print(f"you got the number I was thinking of")

print(output.format(my_guess, HighOrLow, my_random_number))