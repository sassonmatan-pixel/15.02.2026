'''
import random

# in python we write in upper case constant (not changed during run)
CAPITAL_CITIES = [
    "TOKYO", "PARIS", "LONDON", "BERLIN", "MADRID",
    "ROME", "VIENNA", "PRAGUE", "WARSAW", "ATHENS",
    "CAIRO", "ANKARA", "BEIJING", "SEOUL", "HANOI",
    "BANGKOK", "CANBERRA", "OTTAWA", "BRASILIA", "BUENOS AIRES"
]

city = random.choice(CAPITAL_CITIES)
print(city)
print('_ ' * len(city))
# 'A'
# _ _ _ _ _ _
# _ A _ _ A _
# 'T'
# _ A _ _ A _
# 'R'
# _ A R _ A _

# 1. Get random city   (random.choice)
# 2. Mask should be in the length of the word
#    guesses_set = set()
# 3. While TRUE:
# 3.1  print mask
# 3.2  while got-valid-guess
# 3.2.1   guess = input(..).upper()
# 3.2.2   valid = (isalpha == True AND len(guess) == 1 AND guess not in guesses_set)
# 3.3  guesses_set.add(guess)
# 3.4  if guess in random_city
# 3.5.2     change all _ with this letter --> guess in mask  **require effort
# 3.5.2     if '_' not in mask --> 'WON!' + BREAK
# 3.6  otherwise - psila += 1 + draw image hang-man
# 3.7 if psila > max_psila --> 'LOSS' BREAK
'''
import random

CAPITAL_CITIES = [
    "TOKYO", "PARIS", "LONDON", "BERLIN", "MADRID",
    "ROME", "VIENNA", "PRAGUE", "WARSAW", "ATHENS",
    "CAIRO", "ANKARA", "BEIJING", "SEOUL", "HANOI",
    "BANGKOK", "CANBERRA", "OTTAWA", "BRASILIA", "BUENOS AIRES"
]

# 1. Get random city   (random.choice)
random_city = random.choice(CAPITAL_CITIES)
mask_city = ('_ ' * len(random_city))
guesses_set = set()
print(random_city)
point = 6
new_mask_city = ""
# 2. Mask should be in the length of the word
while new_mask_city != random_city and point != 0:
    if new_mask_city == "":
        print(mask_city)
    else:
        print(new_mask_city, "\n")
        new_mask_city = ""

    guess = str(input("enter a letter \n").upper())

    # 3.2.2   valid = (isalpha == True AND len(guess) == 1 AND guess not in guesses_set)
    if guess.isalpha() and len(guess) == 1 and guess not in guesses_set:
        guesses_set.add(guess)
    elif guess == random_city:
        break
    else:
        guesses_set.add(guess)

    # 3.4  if guess in random_city
    # 3.5.2     change all _ with this letter --> guess in mask  **require effort

    if guess in random_city:
        for letter in random_city:
            if letter == guess or letter in guesses_set:
                new_mask_city += letter
            else:
                new_mask_city += "_ "
        print(f"your guess is correct \nYou have {point} lifes left")

    else:
        for letter in random_city:
            if letter == guess or letter in guesses_set:
                new_mask_city += letter
            else:
                new_mask_city += "_ "
        point -= 1
        print(f"your guess is incorrect \nYou have {point} lifes left")


if point > 0:
    print(random_city, "\n")
    print("you win this game")
else:
    print("you lost this game")