P = {"P1": 0.1, "P2" : 0.2, "P3" : 0.4, "P4" : 0.2, "P5" : 0.1,
"P1C" : 1, "P1L" : 0, "P2C" : 0.75, "P2L" : 0.25, "P3C" : 0.5 , "P3L" : 0.5, "P4C" : 0.25, "P4L" : 0.75, "P5C" : 0, "P5L" : 1}


P = [[None, 0.1,0.2,0.4,0.2,0.1]]
C = [[1,0.75,0.5, 0.25, 0]]
L = [[0,0.25,0.5, 0.75, 1]]
def recursive_function():
    pass

data = raw_input()
print(data)
print(len(data))

for t in range(0, len(data)+1):
    for i in range(1,6):
        print(P[t][i])
