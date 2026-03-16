# Dinamic type

print("===============================  Dinamic Type")
a = 10
b = 20.5
c = a + b  
print(a)
a = 'I am a string'   
print(a)




# String handler

print("===============================  String")
string1 = "I am a string"
string2 = 'I am a string'
string3 = 'a'  #This is a string too
print(string1[3])
print("======= Work with string")
print(
      "Horiginal String: ", string1,
      "\nupper(): ",string1.upper(),
      "\nlower(): "+string1.lower(),
      "\nswapcase(): "+ string1.swapcase(),
      "\ncapitalice(): "+ string1.capitalize(),
      "\nreplace('string' , 'replace'): "+  string1.replace("string","replace"),
      "\ncount('a'): ", string1.count('a'),
      "\nstartwith('I am'): ", string1.startswith("I am"),
      "\nendwith('char'): ", string1.endswith("char"),
      "\nsplit(' '): ", string1.split(" "),
      "\nfind('a'): ", string1.find("a"), #The index of firt aparition th the string
      "\nindex('a'): ", string1.index("a"), #The index of firt aparition th the string
      "\nisnumeric(): ", string1.isnumeric(),
      "\nlen(string1): ", len(string1),
      )


# Number handler

print("===============================  Number(Operators)")

basic_operation = (1 + 3 * 3) / 2  # 5

rest_of_division_v1 = 10//6 # No lo entendi bien
module_of_divition = 10%6 # 10/6 me da como resto 4  Return: 4
eponent = 2**3 #8

print("===============================  None")
# None(Is like the null)
nullValue = None

print("===============================  Parse Variables")

number_string = "10"
#resultk = number_string + 5   #Error: In java is "105" but in python you can't concat
result = int(number_string) + 5 # Good: Return: 15 


num1 = input("Insert your first number: ")
num2 = input("Insert your second number: ")
result = int(num1) + int(num2) 


print("The result is: ",result)


# List
print("===============================  List")
# Create list
list_number = [1,2,3,4,5,10]
listMutlipleData = ["Pepe",12,True,1.4,'cat']
emptyList = []
list_from_range = list(range(1,100))  # list_from_range = [1..100]
#Get
list_number[1]  # Return 2
#Set
list_number[1] = 99  # list_number = [1,99,3,4,5,10]
#See al methode allowed for list
print(dir(list_number))



# For
print("===============================  For")
for i in list_number: # Return: 1,2,3,4,5,10
    print(i)

for i in range(1,4):  # Return: 1,2,3 
    print(i)

for i in range(1,10,2): # Return: 1,3,5,7,9
    print(i)

# If    
print("===============================  If")
oper1 =4
oper2 =4

if(oper1 == oper2):
    print("Are equals")

if(oper1 != oper2):
    print("Are Diferent")

if(oper1 >= oper2):
    print("Are > equals")
    
elif(oper1 <= oper2):
    print("Are < equals")

if(oper1 > oper2):
    print("Are >")

else: 
    print("Are <")

# While
print("===============================  If")
itereator = 0

while (itereator<10):
    print(itereator)
    itereator= itereator+1    

