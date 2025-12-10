#1
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}

mn = min(my_dict)
mx = max(my_dict)
print(mn + mx)

#2
names = []

for u in users:
    if u['phone'].endswith('8'):
        names.append(u['name'])

names.sort()

print(' '.join(names))

#3
names = []

for u in users:
    if 'email' not in u or u['email'] == '':
        names.append(u['name'])

names.sort()

print(' '.join(names))

#4
d = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

n = input()

result = []

for digit in n:
    result.append(d[digit])

# обычный print
out = ""
for word in result:
    out += word + " "

print(out.strip())

#5
courses = {
    'CS101': (3004, 'Хайнс', '8:00'),
    'CS102': (4501, 'Альварадо', '9:00'),
    'CS103': (6755, 'Рич', '10:00'),
    'NT110': (1244, 'Берк', '11:00'),
    'CM241': (1411, 'Ли', '13:00')
}

code = input()

room, teacher, time = courses[code]

print(code + ": " + str(room) + ", " + teacher + ", " + time)

#6
keys = {
    'A': '2',    'B': '22',   'C': '222',
    'D': '3',    'E': '33',   'F': '333',
    'G': '4',    'H': '44',   'I': '444',
    'J': '5',    'K': '55',   'L': '555',
    'M': '6',    'N': '66',   'O': '666',
    'P': '7',    'Q': '77',   'R': '777',   'S': '7774',
    'T': '8',    'U': '88',   'V': '888',
    'W': '9',    'X': '99',   'Y': '999',   'Z': '9999',
    '.': '1',    ',': '11',   '?': '111',   '!': '1111',   ':': '11111',
    ' ': '0'
}

s = input()

result = ""

for ch in s:
    up = ch.upper()
    if up in keys:
        result = result + keys[up]

print(result)

#7
morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

s = input()
result = ""

for ch in s:
    up = ch.upper()
    if up in morse:
        result = result + morse[up] + " "

print(result.strip())

#8
result = {}

for i in range(11, 16):
    result[i] = i * i

print(result)

#9
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

# Копируем dict1
for key in dict1:
    result[key] = dict1[key]

# Добавляем dict2
for key in dict2:
    if key in result:
        result[key] = result[key] + dict2[key]
    else:
        result[key] = dict2[key]

print(result)

#10
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for ch in text:
    if ch in result:
        result[ch] = result[ch] + 1
    else:
        result[ch] = 1

#11
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

words = s.split()

count = {}

for w in words:
    if w in count:
        count[w] = count[w] + 1
    else:
        count[w] = 1

# ищем максимальное количество
max_count = max(count.values())

best = None

for w in count:
    if count[w] == max_count:
        if best is None or w < best:
            best = w

print(best)

#12
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for dog, name, surname, age in pets:
    owner = (name, surname, age)
    if owner in result:
        result[owner].append(dog)
    else:
        result[owner] = [dog]

#13
import string

s = input().lower()

# удаляем знаки .,!?:;-
clean = ""
for ch in s:
    if ch.isalpha() or ch == " ":
        clean = clean + ch

words = clean.split()

count = {}

for w in words:
    if w in count:
        count[w] = count[w] + 1
    else:
        count[w] = 1

min_count = min(count.values())

best = None

for w in count:
    if count[w] == min_count:
        if best is None or w < best:
            best = w

print(best)

#14 не понял
