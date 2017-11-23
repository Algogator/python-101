with open('training_data.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.lstrip().strip('\n').split("     ") for x in content]
results = []
for r in content:
    results.append(list(map(int, r)))
# print(results,noofrows)


BisTrue= list(filter(lambda x: x[0],results))

print(len(BisTrue)/len(results))

print("=================")

WatchesTVT= list(filter(lambda x: x[0] and x[1],results))

print(len(WatchesTVT)/len(BisTrue))

WatchesTVF= list(filter(lambda x: not(x[0]) and x[1],results))
print(len(WatchesTVF)/(len(results)-len(BisTrue)))

print("=================")

CatfoodisTrue=list(filter(lambda x: x[2],results))

print(len(CatfoodisTrue)/len(results))

print("=================")

alltrue = list(filter(lambda x: x[1] and x[2],results))
T = list(filter(lambda x:  x[3],alltrue))

print(len(T)/len(alltrue))

allfalse = list(filter(lambda x: not(x[1]) and not(x[2]) ,results))
# print(allfalse)
T = list(filter(lambda x: x[3],allfalse))

print(len(T)/len(allfalse))

TF = list(filter(lambda x: x[1] and not(x[2]) ,results))
T = list(filter(lambda x: x[3],TF))

print(len(T)/len(TF))

FT = list(filter(lambda x: not(x[1]) and x[2] ,results))
T = list(filter(lambda x: x[3],FT))

print(len(T)/len(FT))
