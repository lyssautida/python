def greeting(name):
    print(f"Hi, {name}~!")

print("\n Calling greeting")
greeting("Alice")
greeting("Bunny")

def square(number):
    result = number ** 2
    return result

print("\n Calling square 5")
print(square(5))

def sum(number1, number2):
    result = number1+number2
    return result

print("\n Calling sum 20,50 and input")
print(sum(20,50))
