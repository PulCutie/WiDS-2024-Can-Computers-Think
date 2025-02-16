import random
import csv
import ast

def showlist(l):
    for i in l:
        for j in i:
            print(j, end = ' ')
        print()

def convert(L):
    p = []
    for i in range(4):
        x = []
        for j in range(4):
            x.append(L[(4*i) + j])
        p.append(x)
    return p

def playaction1(l,a,i):
    L = l.copy()
    b = i
    if a == 0:
        if i>3:
            L[i], L[i-4] = L[i-4], L[i]
            b-=4
    elif a == 1:
        if i%4 != 3:
            L[i], L[i+1] = L[i+1], L[i]
            b+=1
    elif a == 2:
        if i<12:
            L[i], L[i+4] = L[i+4], L[i]
            b+=4
    elif a == 3:
        if i%4 != 0:
            L[i], L[i-1] = L[i-1], L[i]
            b-=1
    return L,b

def playaction2(l,a,i):
    L = l.copy()
    b = i
    if a == 0:
        if i>7:
            L[i], L[i-4] = L[i-4], L[i]
            b-=4
    elif a == 1:
        if i%4 != 3:
            L[i], L[i+1] = L[i+1], L[i]
            b+=1
    elif a == 2:
        if i<12:
            L[i], L[i+4] = L[i+4], L[i]
            b+=4
    elif a == 3:
        if i%4 != 0:
            L[i], L[i-1] = L[i-1], L[i]
            b-=1
    return L,b

def playaction3(l,a,i):
    L = l.copy()
    b = i
    if a == 0:
        if i>11:
            L[i], L[i-4] = L[i-4], L[i]
            b-=4
    elif a == 1:
        if i%4 != 3:
            L[i], L[i+1] = L[i+1], L[i]
            b+=1
    elif a == 2:
        if i<12:
            L[i], L[i+4] = L[i+4], L[i]
            b+=4
    elif a == 3:
        if i%4 != 0:
            L[i], L[i-1] = L[i-1], L[i]
            b-=1
    return L,b


L = list(range(1,16)) + [' ']
random.shuffle(L)
p = L.copy()
showlist(convert(p))
print()

terminal_states = []
at = []
idk_why_im_doing_this = []
for i in range(12):
    terminal_states.append([1,2,3,4] + i*[0] + [' '] + (11-i)*[0])
with open('row1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    x = 0
    for row in csvreader:
        if x == 0:
            at.append(row)
            x+=1
        else:
            idk_why_im_doing_this.append(row)
            x-=1

p1 = []
for i in L:
    if i not in [1,2,3,4,' ']:
        p1.append(0)
    else:
        p1.append(i)
solved = False
while not solved:
    for i in at:
        for j in i:
            k = ast.literal_eval(j)
            if p1 == k[0]:
                p1,b = playaction1(p1,k[1],k[2])
                p,b = playaction1(p,k[1],k[2])
    if p1 in terminal_states:
        solved = True
    showlist(convert(p))
    print()


terminal_states = []
at = []
idk_why_im_doing_this = []
for i in range(8):
    terminal_states.append([1,2,3,4,5,6,7,8] + i*[0] + [' '] + (7-i)*[0])
with open('row2.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    x = 0
    for row in csvreader:
        if x == 0:
            at.append(row)
            x+=1
        else:
            idk_why_im_doing_this.append(row)
            x-=1

p1 = []
for i in p:
    if i not in [1,2,3,4,5,6,7,8,' ']:
        p1.append(0)
    else:
        p1.append(i)
solved = False
while not solved:
    for i in at:
        for j in i:
            k = ast.literal_eval(j)
            if p1 == k[0]:
                p1,b = playaction2(p1,k[1],k[2])
                p,b = playaction2(p,k[1],k[2])
    if p1 in terminal_states:
        solved = True
    showlist(convert(p))
    print()


at = []
terminal_states = []
terminal_states.append(list(range(1,16))+[' '])
idk_why_im_doing_this = []
with open('row3_4.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    x = 0
    for row in csvreader:
        if x == 0:
            at.append(row)
            x+=1
        else:
            idk_why_im_doing_this.append(row)
            x-=1

check_solvable= False
solved = False
while not solved:
    for i in at:
        for j in i:
            k = ast.literal_eval(j)
            if p == k[0]:
                check_solvable = True
                p,b = playaction3(p,k[1],k[2])
    if p in terminal_states:
        solved = True
    showlist(convert(p))
    if not check_solvable:
        print('not solvable')
        break
    print()
