def fizzBuzz(n):
    output = ''
    if n % 3 == 0:
        output = "fizz"
    if n % 5 == 0:
        output = output + "buzz"
    return output

print(fizzBuzz(3))
print(fizzBuzz(0))
print(fizzBuzz(1))
print(fizzBuzz(5))
print(fizzBuzz(15))
print(fizzBuzz(30))
print(fizzBuzz(25))
print(fizzBuzz(22))
print(fizzBuzz(1))
print(fizzBuzz(393))

# Is result for "0" correct. Question does not seem to define it.
