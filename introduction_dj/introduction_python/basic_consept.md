# Introduction Python

Here abord the  basic consept about python

## Scoope

The scoope in Python is like the ***yalm*** file

```file
 if(true):
     do something
     do another thing 
     do more of this scoope

 do something out of the scoope    
```

## How to work the class in python

For example if you whant create a for using a sequense and push CTRL + click in the function you will see
something like this

```py
@final
class range(Sequence[int]):
    @property
    def start(self) -> int: ...
    @property
    def stop(self) -> int: ...
    @property
    def step(self) -> int: ...
```

Like you see in the class are tree @property (start,stop,step) and a if you use a for
with two argumets in range:

```py
for i in range(1,4):  # Return: 1,2,3 
    print(i)
```

And if you use tree argument is like this:

```py
for i in range(1,10,2): # Return: 1,3,5,7,9
    print(i)
```

## Function

The function in python don't requered are inside a class like kotlin

## Sintaxis

```py
 def function_name(a, b, c):
    return b * b - 4 * a * c 
```

## Call the function

```py
function_name(2,4,3) # this function return the discriminant
```
