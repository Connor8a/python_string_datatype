print("hello")
print("we can get into trouble")


"""
for looping - loop a variable number of times 
"""

# loop 10 times
for i in range(10):
    print("I am inside a loop")

#count cookies
for i in range(12):
    # I have xx cookies, BAW HAHA !!
    print("I have", i, "cookies, BWA HA HA!!")
#force a new line
print()

# use a variable
age = int( input("please enter your age:"))
#print a greeting for each year

for i in range(age):
    print((i+1), "brith greetings")

#define range - start, end, increment
for i in range(5, 10):
    print(i)


#count down
#this did not run in Python 3
print()
for count in range(15, 2, -1 ): # start, end increment by
    print(count)



#counting cookies
cookies = int( input("How many cookies are in the cookie jar? " ))
for count in range(cookies, 0, -1):
    if count == 1:
        print("1 cookie, I have 1 cookie")
    else:
        print(count,"cookies")
    
    
    
    
    
    
    
