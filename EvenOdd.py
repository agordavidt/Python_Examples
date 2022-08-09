"""
Author: David Agor
Date: 09/08/2022
Program: Takes number input and classifies them into even and odd numbers
"""

def evenOdd(numbers):
    even = []
    odd = []

    for number in numbers:
        if int(number) % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd

userInput = input("Enter the numbers (space between them): ")
userInput = list(userInput.split())
even_number, odd_number = evenOdd(userInput)
print('Even Nos: ', ' ,'.join(even_number), '\n', 'Odd Nos: ', ' ,'.join(odd_number))