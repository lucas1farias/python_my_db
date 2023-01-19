

# --------------------------------------- List comprehension na forma pythônica ---------------------------------------
letters = ['A', 'B', 'C']
letters_lowercase = [word.lower() for word in letters]  #
print(letters_lowercase)

# -------------------------------------- List comprehension na forma não pythônica--------------------------------------
for index, word in enumerate(letters):
    letters[index] = word.lower()

print(letters)
