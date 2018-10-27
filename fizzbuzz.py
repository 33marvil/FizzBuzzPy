def fizzbuzz(num):
    if num <= 1: # evaluando num negative
        return False
    elif num % 3 == 0 and num % 5 == 0: # If son multiple de 3 y 5
        return "FizzBuzz"
    elif num % 3 == 0: # If son multiple de 3
        return "Fizz"
    elif num % 5 == 0: # If son multiple de 5
        return "Buzz"
    else: # Evaluando no multiplos de 3 y 5 return su valor
        return num

for multiple in range(1, 101):
    print(fizzbuzz(multiple))
