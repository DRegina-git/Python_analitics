point_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
point_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = input().upper()
count = 0
if word[0] in "AEIOULNSTRDGBCMPFHVWYKJXQZ":
    for letter in word:
        for key, value in point_en.items():
            if letter in value:
                count +=key
else:
    for letter in word:
        for key, value in point_ru.items():
            if letter in value:
                count +=key
print(count)