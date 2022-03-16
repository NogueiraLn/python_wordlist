from itertools import product
import string


min_letras = int(input("Enter min length of password: "))
max_letras = int(input("Enter max length of password: "))
counter = 0
charater = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file_open = open("WordList.txt", 'w')



for i in range(min_letras, max_letras + 1):
    for j in product(charater, repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write("\n")
        counter += 1

print("The Wordlist of {} passwords created".format(counter))
