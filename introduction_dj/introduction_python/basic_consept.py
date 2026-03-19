# Dinamic type

print("===============================  Dynamic Type")
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
    "Original String: ", string1,
    "\nupper(): ",string1.upper(),
    "\nlower(): "+string1.lower(),
    "\nswapcase(): "+ string1.swapcase(),
    "\ncapitalice(): "+ string1.capitalize(),
    "\nreplace('string' , 'replace'): "+  string1.replace("string","replace"),
    "\ncount('a'): ", string1.count('a'),
    "\nstartswith('I am'): ", string1.startswith("I am"),
    "\nendwith('char'): ", string1.endswith("char"),
    "\nsplit(' '): ", string1.split(" "),
    "\nfind('a'): ", string1.find("a"), #The index of first apparition th the string
    "\nindex('a'): ", string1.index("a"), #The index of first apparition th the string
    "\nisnumeric(): ", string1.isnumeric(),
    "\nlen(string1): ", len(string1),
    )


# Number handler

print("===============================  Number(Operators)")

basic_operation = (1 + 3 * 3) / 2  # 5

rest_of_division_v1 = 10//6 # No lo entendi bien
module_of_division = 10%6 # 10/6 me da como resto 4  Return: 4
exponent = 2**3 #8

print("===============================  None")
# None(Is like the null)
nullValue = None

print("===============================  Parse Variables")

number_string = "10"
#result = number_string + 5   #Error: In java is "105" but in python you can't concat
result = int(number_string) + 5 # Good: Return: 15 


#num1 = input("Insert your first number: ")  #Read a number for console
#num2 = input("Insert your second number: ")
#result = int(num1) + int(num2) 


print("The result is: ",result)


# List
print("===============================  List")
# Create list
list_number = [1,2,3,4,5,10]
listMultipleData = ["Pepe",12,True,1.4,'cat']
emptyList = []
list_from_range = list(range(1,100))  # list_from_range = [1..100]
list_from_constructor = list((1,2,3,12)) # create a list from construct data
#Get
list_number[2]  # Return 3
list_number[-1] # Return 10

#Set
list_number[1] = 99  # list_number = [1,99,3,4,5,10]

#length
print("Length of list: ",len(list_number)) #6

#find
print("Check if (4 in list_number): " ,    4 in list_number) # true  
#==============Insert
#append: Insert a element to the end
list_number.append(100) #[1,99,3,4,5,10,100] 
#extend: Insert many element to the end
list_number.extend([200,"Car"]) #[1,99,3,4,5,10,100,200,"Car"]
#insert: Insert a element in specific position
list_number.insert(1,98) #[1,98,99,3,4,5,10,100,200,"Car"]
#==============Delete
#Pop: remove the last and return him
print(list_number.pop())  #return: "Car" current list:  [1,98,99,3,4,5,10,100,200]
#Remove: Remove the element you pass for param if not found throw a error
list_number.remove(98) #current list:  [1,99,3,4,5,10,100,200]
#Remove everything
#list_number.clear() #[]
#==============Sort
list_number.sort(reverse=True)  #the default value is reverse = false
print(list_number) #[200, 100, 99, 10, 5, 4, 3, 1]

#==============Check apparitions
print(list_number.count(1)) # Check in the list how many time exist the value 1 


#See al method allowed for list
#print(dir(list_number))


# Tuples: It's a inmutable list 
print("=================================  Tuples")

tuple_color = ("yellow","withe","yellow","red")
# Count the apparition number of some value
print("Count: ",tuple_color.count("yellow")) # 2 
print("Index of yellow: ",tuple_color.index("yellow")) #0 because is the index of his first apparition
#print(dir(tuple_color))


# Sets: In this kind of list is't possible repeat element
print("=================================  Sets")
#============Create
set_type = {'Car','Move',"Table","Car","Car"} # {'Car', 'Table', 'Move'}

#============ Insert
set_type.add("car") #{'Car', 'Table', 'Move','car'} -> This value will insert because is't key sensitive

#============ Select
#Different: Received a list and return a Set with all elements of this list
print("Different: ",set_type.difference(["Car",'car'])) #Return -> {'Table','Move'}  
print("Make intersection: ",set_type.intersection(['Span',"Table"])) # {'Table'} 
print("Make UNION: ",set_type.union(['Span',"Table"])) #  {'Car', 'car', 'Table', 'Move', 'Span'}


#================ Update
#================ Delete
set_type.difference_update(["Car",'car'])  # Remove all elements matches: {'Move','Table'}
set_type.discard('Move') # #Return -> None. if you found the element you delete : {'Table'} 

print(set_type)
#print(dir(set_type))

print("================================= Dictionary (Map or Json)")

dictionary_array = [
    {"name": "Pepe","age":12},
    {"name": "Miguel","age":11},
    {"name": "Jorge","age":22}
]

dictionary_object = {
    "name": "Pepe",
    "age":12,
    'friends': [
        'Pepe',
        'Juan',
        'Carlos',
    ]
}

print(dictionary_array)
print("Get de",dictionary_object.get("friends"))

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
    if oper1 > 2 or oper2 > 2:
        print("The operators are bigger than two")     

if(oper1 != oper2):
    print("Are Diferent")
    if oper1 <10 and oper2 < 10:
        print("The operators are less than ten")

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

