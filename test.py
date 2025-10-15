import os, time

# Цвета
B = '\u001b[44m'   # синий
W = '\u001b[47m'   # белый
R = '\u001b[41m'   # красный
E = '\u001b[0m'    # сброс цвета

# 1. Флаг 
print("Флаг Франции:\n")
for i in range(8):   # высота
    print(f"{B}{'  '*4}{W}{'  '*4}{R}{'  '*4}{E}")

# 2. Узор
print("\nУзор:")
for i in range(4):
    row = ""
    for j in range(4):
        row += "██" if (i+j)%2==0 else "  "
    print(row)


# 3. График y=x^2
print("\nГрафик y = x^2:")
for y in range(9, -1, -1):
    row = ""
    for x in range(21):
        if round((x/3)**2) == y:
            row += "*"
        elif x==0: row += "|"
        elif y==0 and x%2==0: row += "-"
        else: row += " "
    print(row)


# 4. Диаграмма 
print("\nДиаграмма:")

file = open('sequence.txt', 'r')
nums = []
for number in file:
    nums.append(float(number))
file.close()


less = sum(1 for n in nums if n < 0)
more = sum(1 for n in nums if n > 0)
total = less + more

print("Меньше 0:", "#" * (less * 20 // total), f"{less}/{total}")
print("Больше 0:", "#" * (more * 20 // total), f"{more}/{total}")
