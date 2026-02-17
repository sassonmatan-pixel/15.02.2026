x = "hello world"
new_x = ""
for letter in x:
    if letter == "o":
        letter = letter.replace("o", "!")
        new_x += letter
    else:
        new_x += letter
print(new_x)