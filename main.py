from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

# Order not randomised:
password_letter = [choice(letters) for _ in range(nr_letters)]
password_symbols = [choice(symbols) for _ in range(nr_symbols)]
password_numbers = [choice(numbers) for _ in range(nr_numbers)]
password_list_i = password_letter + password_symbols + password_numbers
password = "".join(password_list_i)
print(f"Your password is {password}")

# Order of characters randomised:
# create a list first
password_letters = [choice(letters) for _ in range(nr_letters)]
password_numbers = [choice(numbers) for _ in range(nr_numbers)]
password_symbols = [choice(symbols) for _ in range(nr_symbols)]

password_list_ii = password_symbols + password_numbers + password_letters
shuffle(password_list_ii)
# changing to string now
password = "".join(password_list_ii)
print(f"Your password is: {password}")

