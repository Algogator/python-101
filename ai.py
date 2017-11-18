P = {"P1": 0.1, "P2" : 0.2, "P3" : 0.4, "P4" : 0.2, "P5" : 0.1,
"P1C" : 1, "P1L" : 0, "P2C" : 0.75, "P2L" : 0.25, "P3C" : 0.5 , "P3L" : 0.5, "P4C" : 0.25, "P4L" : 0.75, "P5C" : 0, "P5L" : 1}


P = [[None, 0.1,0.2,0.4,0.2,0.1]]
C = [None,[None,1,0.75,0.5, 0.25, 0]]
L = [None, [None,0,0.25,0.5, 0.75, 1]]
p = [[None]]
Pout = [None]


def recursive_function():
    pass

data = raw_input()
print(data)
print(len(data))

sum = 0
for i in range(1,6):
    if data[0] == 'L':
        sum  = sum + (L[1][i] * P[0][i])
    else:
        sum  = sum + (C[1][i] * P[0][i])
    # print(sum)
p[0].append(sum)

print("==============")

Pout.append([None])
for i in range(1,6):
    # print(t,i, p[0][1])
    if data[0] == 'L':

        Pout[1].append((L[1][i]* P[0][i])/p[0][1])

    else:

        Pout[1].append((C[1][i]* P[0][i])/p[0][1])


# for y in range(1, 6):
#     print("P(h"+str(y)+" | Q) ="+str(Pout[1][y]))


# print(Pout)

for t in range(2, len(data)+1):
    sum = 0
    for i in range(1,6):
        if data[t-1] == 'L':
            sum  = sum + (L[1][i] * Pout[t-1][i])
        else:
            sum  = sum + (C[1][i] * Pout[t-1][i])
        # print(sum)
    p[0].append(sum)
    # print("...")
    # print(P)
    # print("...")
    # print(p)
    # print("...")
    # print(Pout)
    Pout.append([None])
    for i in range(1,6):
        # print(t,i, p[0][1])
        if data[t-1] == 'L':
            Pout[t].append((L[1][i] * Pout[t-1][i])/p[0][t])
        else:
            Pout[t].append((C[1][i] * Pout[t-1][i])/p[0][t])
        # print(Pout)
    for y in range(1, 6):
        print("P(h"+str(y)+" | Q) ="+str(Pout[t-1][y]))

    sumC = 0
    sumL = 0
    for i in range(1,6):
            sumL  = sumL + (L[1][i] * Pout[t-1][i])
            sumC  = sumC + (C[1][i] * Pout[t-1][i])
        # print(sum)
    print("Probability that the next candy we pick will be C, given Q:"+str(sumC))
    print("Probability that the next candy we pick will be L, given Q:"+str(sumL))
#

sumC = 0
sumL = 0
for i in range(1,6):
        sumL  = sumL + (L[1][i] * Pout[-1][i])
        sumC  = sumC + (C[1][i] * Pout[-1][i])

for y in range(1, 6):
    print("P(h"+str(y)+" | Q "+str(Pout[-1][y]))
print("Probability that the next candy we pick will be C, given Q:"+str(sumC))
print("Probability that the next candy we pick will be L, given Q:"+str(sumL))
