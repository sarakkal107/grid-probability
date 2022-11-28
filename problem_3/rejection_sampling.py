import math
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib

def A():
    a = False
    return a


def B():
    b = False
    bProb = np.random.randint(1, 101)
    if (bProb > 10):
        b = True
    return b

def C(a,b):
    c = False
    cProb = np.random.randint(1,101)
    if (a == True) and (b == True):
        if (cProb <= 20):
            c = True
    elif (a == True) and (b == False):
        if (cProb <= 60):
            c = True
    elif (a == False) and (b == True):
        if (cProb <= 50):
            c = True
    elif (a == False) and (b == False):
        c = False
    return c

def D(b,c):
    d = False
    dProb = np.random.randint(1,101)
    if (c == True) and (b == True):
        if (dProb <= 75):
            d = True
    elif (c == False) and (b == True):
        if (dProb <= 10):
            d = True
    elif (c == True) and (b == False):
        if (dProb <= 50):
            d = True
    elif (c == False) and (b == False):
        if (dProb <= 20):
            d = True
    return d

def rejection_samp1(N):
    numTrue = 0
    numFalse = 0
    a = False
    b = False
    c = False
    d = False
    for count in range(N):
        a = A()
        b = B()
        c = C(a,b)
        d = D(b,c)
        if (c == True):
            if (d == True):
                numTrue += 1
            else:
                numFalse += 1
    probTrue = numTrue / (numTrue + numFalse)
    probFalse = numFalse / (numTrue + numFalse)  
    return [probTrue, probFalse]


def rejection_samp2(N):
    numTrue = 0
    numFalse = 0
    a = False
    b = False
    c = False
    d = False
    for count in range(N):
        a = A()
        b = B()
        c = C(a,b)
        d = D(b,c)
        if (c == True):
            if (b == True):
                numTrue += 1
            else:
                numFalse += 1
    probTrue = numTrue / (numTrue + numFalse)
    probFalse = numFalse / (numTrue + numFalse)    
    return [probTrue, probFalse]

def rejection_samp3(N):
    numTrue = 0
    numFalse = 0
    a = False
    b = False
    c = False
    d = False
    for count in range(N):
        a = A()
        b = B()
        c = C(a,b)
        d = D(b,c)
        if (a == False) and (b == True):
            if (d == True):
                numTrue += 1
            else:
                numFalse += 1
    probTrue = numTrue / (numTrue + numFalse)
    probFalse = numFalse / (numTrue + numFalse)    
    return [probTrue, probFalse]

def rejection_samp4(N):
    numTrue = 0
    numFalse = 0
    a = False
    b = False
    c = False
    d = False
    for count in range(N):
        a = A()
        b = B()
        c = C(a,b)
        d = D(b,c)
        if (b == False):
            if (d == True):
                numTrue += 1
            else:
                numFalse += 1
    probTrue = numTrue / (numTrue + numFalse)
    probFalse = numFalse / (numTrue + numFalse)    
    return [probTrue, probFalse]



probDC = rejection_samp1(1000)
print(probDC)
print("")
probBC = rejection_samp2(1000)
print(probBC)
print("")
probDAB = rejection_samp3(1000)
print(probDAB)
print("")

numSamples = [500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000]

probabilities = []

# for count in range(len(numSamples)):
#     n = numSamples[count]
#     currentProb = rejection_samp1(n)
#     probabilities.append(currentProb[0])

fig = plt.figure()

for count in range(len(numSamples)):
    n = numSamples[count]
    currentProb = rejection_samp4(n)
    probabilities.append(currentProb[0])

fig = plt.figure()

# creating the bar plot
plt.plot(numSamples,probabilities)
 
plt.xlabel("Number of Samples")
plt.ylabel("Probability")
plt.title("Rejection Sampling Probability vs Samples")
plt.savefig("rejection_sampling3.png")
plt.show()