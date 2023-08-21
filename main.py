import random
import array
import time

# maximum length of password needed
MAX_LEN = 12

# declare arrays of the character sets needed for the password
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/',
           '|', '~', '>', '*', '(', ')', '<']
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# randomly select at least one character from each character set
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

# combine the selected characters
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

# fill the rest of the password length by selecting randomly from the combined list
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)

# convert temporary password into an array and shuffle
temp_pass_list = array.array('u', temp_pass)
random.shuffle(temp_pass_list)

# create the password string
password = ""
for x in temp_pass_list:
    password = password + x

# ask for the site name
site_name = input("Entrez le nom du site : ")

# create and write to the text file
file_name = f"Password.txt"
with open(file_name, "w") as file:
    file.write(f"Site : {site_name}\nMot de passe : {password}")

print(f"Mot de passe généré pour {site_name}.")
