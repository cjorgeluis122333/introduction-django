#There are two way of create a function

# First Way: This is a normal function

def makeManyThings (number1,number2):
    sumResult= number1 + number2 # 10
    restResult = number1 - number2 #-2
    return sumResult + restResult  # 8

print(makeManyThings(4,6))

# Second Way: LAMBDA Function: This function just will has one line

# function_name = lambda arg_1,arg_2, .., arg_n : return_operation
sum = lambda number1, number2: number1+ number2

print(sum(4,6)) # It's called like a function
