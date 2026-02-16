'''
שאלה 2 – מערכת הצבעות ובדיקת מצביעים כפולים
קלוט מהמשתמש מספר ת.ז. של מצביע (נניח שמדובר במספרים בין 1 ל־100)

כללים:

כל מצביע שנקלט – הכנס לרשימה בשם votes
קולטים רק את ת.ז. של המצביע, ולא את ההצבעה עצמה
ייתכן שאותו מצביע ינסה להצביע יותר מפעם אחת
הקלט מסתיים כאשר מתקבל הערך 999-
לאחר סיום הקלט:

צור set של מצביעים ייחודיים מתוך הרשימה

צור set נוסף בשם invalid_voters

עבור על כל המצביעים:

כל מצביע שהופיע יותר מפעם אחת – הסר אותו מקבוצת המצביעים החוקיים
הוסף אותו ל־invalid_voters
לבסוף הדפס:

את כל המצביעים החוקיים
את כל המצביעים הפסולים
כמה ניסיונות הצבעה היו היום (כלומר אורך הרשימה כולל כפילויות)
רמזים:

ניתן להשתמש ב־count
ניתן לעבור על set כדי לא לחזור על אותו מצביע שוב ושוב
'''

#list for all voting
id_numbers = []
while id != "-999":
    id = input("enter a new id number")

    #check if is valid number
    while True:
        if id.isdigit() or id == "-999":
            if id == "-999":
                break
            id = int(id)
            if id <= 100 and id > 0:
                id_numbers.append(id)
            break
        else:
            id = input("enter id number again")

#all votes no doubles
voters = set(id_numbers)

valid_voters = list(voters)
invalid_voters = []

#loop for invalid list
for num in voters:
    if num in id_numbers:
        if id_numbers.count(num) > 1:
            invalid_voters.append(num)

#loop for valid list
for num in invalid_voters:
    valid_voters.remove(num)

#printer (the answer)
print(f'the valid voters id is:{valid_voters}')
print(f'the invalid voters id is:{invalid_voters}')
print(f'{len(id_numbers)} voters')