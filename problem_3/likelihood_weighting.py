from likelihood_functions import weighted_sample
from likelihood_functions import likelihood_weighting
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

nodes = np.array(["A","B","C","D"])

adjaceny_matrix = np.array([[0,0,0,0],
                            [0,0,0,0],
                            [1,1,0,0],
                            [0,1,1,0]
                                    ], dtype=bool) 


prob_A = {True: [0.0], False: [1.0]}
prob_B  = {True: [0.9], False: [0.1]}
prob_C = {True: [0.2, 0.6, 0.5, 0], False: [0.8, 0.4, 0.5, 1.0]} # [(a,b),(a, ~b),(~a,b),(~a,~b)]
prob_D = {True: [0.75, 0.1, 0.5, 0.2], False: [0.25, 0.9, 0.5, 0.8]} # [(b,c),(b, ~c),(~b,c),(~b,~c)]


bn = [nodes, adjaceny_matrix, {nodes[0]: prob_A, nodes[1]: prob_B, nodes[2]: prob_C, nodes[3]: prob_D}]


def query1(bn,n):
    e = {nodes[2]:True}
    q = [nodes[3],True]
    probs = likelihood_weighting(q,e,bn, n)
    return probs

def query2(bn):
    e = {nodes[2]:True}
    q = [nodes[1],True]
    probs = likelihood_weighting(q,e,bn, 1000)
    return probs

def query3(bn):
    e = {nodes[0]:False, nodes[1]: True}
    q = [nodes[3],True]
    probs = likelihood_weighting(q,e,bn, 1000)
    return probs

def query4(bn,n):
    e = {nodes[1]:False}
    q = [nodes[3],True]
    probs = likelihood_weighting(q,e,bn, n)
    return probs

probs1 = query1(bn, 1000)
print(probs1)
print("")
probs2 = query2(bn)
print(probs2)
print("")
probs3 = query3(bn)
print(probs3)
print("")

numSamples = [500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000]

probabilities = []

# for count in range(len(numSamples)):
#     n = numSamples[count]
#     currentProb = query1(bn,n)
#     probabilities.append(currentProb[0])

# fig = plt.figure()

for count in range(len(numSamples)):
    n = numSamples[count]
    currentProb = query4(bn,n)
    probabilities.append(currentProb[0])

fig = plt.figure()
 
# creating the bar plot
plt.plot(numSamples,probabilities)
 
plt.xlabel("Number of Samples")
plt.ylabel("Probability")
plt.title("Likelihood Weighting Probability vs Samples")
plt.savefig("likelihood_weighting3.png")
plt.show()
