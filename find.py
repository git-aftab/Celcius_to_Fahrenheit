# Write a Python code to convert celcius to fahrenheit 

def tempConverter(T):
    fahrenheit = (T*9/5)+32
    print(f" The temperature {T}^C in fahrenheit : {fahrenheit}")

tempConverter(30)
tempConverter(32)
tempConverter(50)