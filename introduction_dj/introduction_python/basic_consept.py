# Dinamic type

print("===============================  Dinamic Type")
a = 10
b = 20.5
c = a + b  
print(a)
a = 'I am a string'   
print(a)





# Do not exist the char 

print("===============================  String")
string1 = "I am a string"
string2 = 'I am a string'
string3 = 'a'  #This is a string too


# List
print("===============================  List")
list = [1,2,3,4,5,10]
print(list[1])  # Return 2

# For
print("===============================  For")
for i in list: # Return: 1,2,3,4,5,10
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

