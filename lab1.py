RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
import time

for i in range(14):
    if i < 1 or i>12:
        print(f'{WHITE}{"  " * 16}{END}')
    elif i == 2 or i == 12:
        print(f'{WHITE}{"  " * 7}{RED}{"  " * 2}{WHITE}{"  " * 7}{END}')
    elif i == 3 or i == 11:
        print(f'{WHITE}{"  " * 6}{RED}{"  " * 4}{WHITE}{"  " * 6}{END}')
    elif i == 4 or i == 10:
        print(f'{WHITE}{"  " * 5}{RED}{"  " * 6}{WHITE}{"  " * 5}{END}')
    elif i == 5 or i == 9:
        print(f'{WHITE}{"  " * 4}{RED}{"  " * 8}{WHITE}{"  " * 4}{END}')
    elif i == 6 or i == 8:
        print(f'{WHITE}{"  " * 3}{RED}{"  " * 10}{WHITE}{"  " * 3}{END}')
    elif i ==7:
        print(f'{WHITE}{"  " * 2}{RED}{"  " * 12}{WHITE}{"  " * 2}{END}')
time.sleep(2)

for i in range(5):
    row = ""
    for j in range(9):
        row += "██" if ((i==2 and (j%4==0)) or ((i==1 or i==3) and (j%2==1)) or ((i==0 or i==4) and j%4==2)) else "  "
    print(row)
time.sleep(2)


plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i * 3

step = round(abs(result[0] - result[9]) / 9, 2)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '#'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')

file = open('sequence.txt', 'r')
list = []
ct=ct1=ct2=0
for number in file:
    list.append(float(number))
file.close()
for i in list:
    if 0<=i<=5:
        ct+=1
        ct2+=1
    elif -5<=i<=0: 
        ct1+=1
        ct2+=1
ct3=str(round(ct*100/ct2))
ct4=str(round(ct1*100/ct2))
print(ct3+"%",'██'*int(ct3))
print(ct4+"%",'██'*int(ct4))