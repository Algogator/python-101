#How a for loop works
a = [1,2,3]
#Calls iter() on list
d = iter(a) #return Iterator object that has the next method

print(next(d))
