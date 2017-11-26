import sys

#More specifically, for full credit, the code should include and use a Bayesian network class. The class should include a member function called computeProbability(b, e, a, j, m), where each argument is a boolean, specifying if the corresponding event (burglary, earthquake, alarm, john-calls, mary-calls) is true or false. This function should return the joint probability of the five events.

class BayesianNetwork:

    def computeP(self,d):

        fin_val = 1
        for i in d:
            if i == 'E':
                # print BayesNet['E'][d[i]], 'E'
                fin_val *= BayesNet['E'][d[i]]
            if i == 'B':
                # print BayesNet['B'][d[i]], 'B'
                fin_val *= BayesNet['B'][d[i]]
                # fin_val *= BayesNet['B']
            if i == 'J':
                #A is True
                if d[i]:
                    if 'A' in d:
                        # print BayesNet['J'][d['A']], 'J'
                        fin_val *= BayesNet['J'][d['A']]

                #A is False
                else:
                    pass
            if i == 'M':
                #A is True
                if d[i]:
                    if 'A' in d:
                        # print BayesNet['M'][d['A']], 'M'
                        fin_val *= BayesNet['M'][d['A']]

                #A is False
                else:
                    pass
            if i == 'A':
                # print BayesNet['A'][d[i]][d['B']][d['E']],'A'
                fin_val *= BayesNet['A'][d[i]][d['B']][d['E']]

        #print d, fin_val
        return fin_val


    def computeProbability(self, b,e,a,j,m):

        def convertBool(b,e,a,j,m):
            res = {}
            res['A'] = a
            res['B'] = b
            res['E'] = e
            res['J'] = j
            res['M'] = m
            return res

        # print(b,e,a,j,m)
        sum = 0
        # if len(b) == 1 and len(e) == 1 and len(a) == 1:
        #
        # fin_val = 1
        for i in b:
            for c in e:
                # print a
                if len(a) > 1:
                    # print i,c
                    # print a
                    #A can have two values T and F depending on value of B and E
                    for k in a:
                        for y in k:
                            if len(j) == 1:
                                if len(m) > 1:
                                    for x in m[k]:
                                        sum += self.computeP(convertBool(i,c,y,j[0],x))
                                else:
                                    for x in m:
                                        sum += self.computeP(convertBool(i,c,y,j[0],x))
                            else:
                                for l in j[y]:
                                    if len(m) > 1:
                                        for x in m[y]:
                                            sum += self.computeP(convertBool(i,c,y,l,x))
                                    else:
                                        for x in m:
                                            sum += self.computeP(convertBool(i,c,y,l,x))
                else:
                    for k in a:
                        if len(j) == 1:
                            if len(m) > 1:
                                for x in m[k]:
                                    sum += self.computeP(convertBool(i,c,k,j[0],x))
                            else:
                                for x in m:
                                    sum += self.computeP(convertBool(i,c,k,j[0],x))
                        else:
                            for l in j[k]:
                                if len(m) > 1:
                                    for x in m[k]:
                                        sum += self.computeP(convertBool(i,c,k,l,x))
                                else:
                                    for x in m:
                                        sum += self.computeP(convertBool(i,c,k,l,x))

        return sum
        # if 'B' in data:
        #     fin_val *= BayesNet['E'][d[i]]
        # else:
        #
        #
        # return fin_val

BayesNet = {'B':{1:0.001,0:0.999},
'E':{1: 0.002,0:0.998},
'A':{1:[[0.001,0.29],[0.94,0.95]], 0:[[0.999,0.71],[0.06,0.05]]},
'J':[0.05,0.90],
'M':[0.01, 0.70]}

def convertBool(data):
    j,m,b,e,a = [[0,1],[0,1]],[[0,1],[0,1]],[0,1],[0,1],[[0],[1]]
    for i in data:
        if i[0] == 'B':
            if i[1]=='t':
                b = [1]
            else:
                b = [0]

        elif i[0] == 'E':
            if i[1]=='t':
                e = [1]
            else:
                e = [0]
        elif i[0] == 'A':
            if i[1]=='t':
                a = [1]
            else:
                a = [0]
        elif i[0] == 'J':
            if i[1]=='t':
                j = [1]
            else:
                j = [0]
        else:
            if i[1]=='t':
                m = [1]
            else:
                m = [0]
    nw = BayesianNetwork()
    return nw.computeProbability(b,e,a,j,m)

x =  sys.argv[1:]

def checkone(x):
    if len(x) <= 2:
        res = {}
        for i in x:
            if i[0] == 'B':
                if i[1]=='t':
                    res['B'] = 1
                else:
                    res['B'] = 0

            elif i[0] == 'E':
                if i[1]=='t':
                    res['E'] = 1
                else:
                    res['E'] = 0
            elif i[0] == 'A':
                if i[1]=='t':
                    res['A'] = 1
                else:
                    res['A'] = 0
            elif i[0] == 'J':
                if i[1]=='t':
                    res['J'] = 1
                else:
                    res['J'] = 0
            else:
                if i[1]=='t':
                    res['M'] = 1
                else:
                    res['M'] = 0
        if len(res) == 2:
            if 'B' in res and 'E' in res:
                return BayesNet['B'][res['B']] * BayesNet['E'][res['E']]
            else:
                return convertBool(x)
        elif len(res) == 1:
            if 'B' in res:
                return BayesNet['B'][res['B']]
            elif 'E' in res:
                return BayesNet['E'][res['E']]
            else:
                return convertBool(x)



if 'given' in x:
    den = x[x.index('given')+1:]
    if len(den) <= 2:
        den = checkone(den)
    else:
        den = convertBool(den)
    x.remove('given')
    if len(x) <= 2:
        num = checkone(x)
    else:
        num = convertBool(x)
    print num/den
else:
    if len(x) <= 2:
        print checkone(x)
    else:
        print convertBool(x)

# nw = BayesianNetwork()


# print nw.computeProbability(d = ben), "ANS"
