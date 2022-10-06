#name:Connor
#date: 10/9
#description: a factorial program that prompt for a number and show it's factorial

#dec vars 


#prompt number
number = 0 
factorial = 0 

#calculate factorail 
number = int(input(" Enter a number and I'll tell you the factorial value: "))

#calculate facotrial 
for count in range(1, number+1):
    factorial = factorial * count 
#display the results 
#5! = 120 
print(f"{number}! = {factorial} ")