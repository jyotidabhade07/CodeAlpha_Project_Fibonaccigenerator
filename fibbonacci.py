#fibbonacci series => sequence of the number where a number is the sum of the teo numbers that comes before it.
#sequence first digit is 0 and 1 by default 
def fibonacci_Generator_recursive(no):
    # Base cases............
    if no <= 0:
        return 0
    elif no == 1:
        return 1
    # Recursive case............
    else:
        return fibonacci_Generator_recursive(no - 1) + fibonacci_Generator_recursive(no - 2) #mathematical recurrence relation F(n)=F(n−1)+F(n−2) 

#how can we use fibbonacci in example....
no =8  
#we can change the value of no to get more or shorter lenght of fibbonacci sequence....
print([fibonacci_Generator_recursive(i) for i in range(no)])
'''for i in range(no):
    print(fibonacci_Generator_recursive(i))'''