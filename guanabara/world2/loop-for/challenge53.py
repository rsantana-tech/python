# #Python Exercise 53: Create a program that reads any
# phrase and tells whether it is a palindrome, disregarding spaces.
#
# Examples of palindromes:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
# O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

phrase =  input('Enter a phase: ')

phrase = phrase.replace(" ", "").upper()
reverse_phrase = phrase[::-1]

if phrase == reverse_phrase:
    print("it's a palindrome!")
else:
    print("it's not a palindrome!")