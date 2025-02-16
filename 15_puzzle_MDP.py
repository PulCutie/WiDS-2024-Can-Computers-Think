import csv

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


terminal_states = []
at = [[]]
for i in range(12):
    terminal_states.append([1,2,3,4] + i*[0] + [' '] + (11-i)*[0])
    at[0].append([terminal_states[-1],4,i+4])
allstates = terminal_states.copy()
i = 0
while True:
    at.append([])
    for j in at[i]:
        for k in range(4):
            l,z = playaction1(j[0],k,j[2])
            if l not in allstates:
                at[i+1].append([l,(k+2)%4,z])
                allstates.append(l)
    if len(at[i+1])==0:
        break
    i+=1
    print(len(allstates))

with open('row1.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(at)


terminal_states = []
at = [[]]
for i in range(8):
    terminal_states.append([1,2,3,4,5,6,7,8] + i*[0] + [' '] + (7-i)*[0])
    at[0].append([terminal_states[-1],4,i+8])
allstates = terminal_states.copy()
i = 0
while True:
    at.append([])
    for j in at[i]:
        for k in range(4):
            l,z = playaction2(j[0],k,j[2])
            if l not in allstates:
                at[i+1].append([l,(k+2)%4,z])
                allstates.append(l)
    if len(at[i+1])==0:
        break
    i+=1
    print(len(allstates))

with open('row2.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(at)


terminal_states = []
at = [[]]
terminal_states.append(list(range(1,16))+[' '])
at[0].append([terminal_states[-1],4,15])
allstates = terminal_states.copy()
i = 0
while True:
    at.append([])
    for j in at[i]:
        for k in range(4):
            l,z = playaction3(j[0],k,j[2])
            if l not in allstates:
                at[i+1].append([l,(k+2)%4,z])
                allstates.append(l)
    if len(at[i+1])==0:
        break
    i+=1
    print(len(allstates))

with open('row3_4.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(at)
