userNum = int(input("Please enter a number more than 1: "))     # Requests integer from user.   

if userNum > 1:                                                 # Starts loop if user input is more than 1.
    for factors in range (2, userNum):
        if (userNum % factors) == 0:                            # Starts nested loop if user input is divisable by all numbers within for loop.
            print (userNum, " is not a prime number.")
            break                                               # Ends the loops.
    else:                                                       # If the nested loop isnt triggered, prints message.
        print (userNum, "is a prime number.")
else:                                                           # If user input is less than 2, prints message.
    print ("Entered number should be more than 1.")
    
