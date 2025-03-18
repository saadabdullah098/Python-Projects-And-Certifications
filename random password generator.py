#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#taking inputs from user
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password: ")) 
nr_symbols = int(input(f"How many symbols would you like: "))
nr_numbers = int(input(f"How many numbers would you like: "))


#creating variables with random letters, numbers, and symbols
ps_letters = random.sample(letters, nr_letters)
ps_numbers = random.sample(numbers, nr_numbers)
ps_symbols = random.sample(symbols, nr_symbols)

#concatenating 
password = ps_letters + ps_numbers + ps_symbols

#shuffling
random.shuffle(password)

final_password = "".join(password)

#printing the final password
print(f"Your password is: {final_password}")
