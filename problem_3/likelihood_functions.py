import numpy as np
import copy

def weighted_sample(bn, e):
    nodes, nodes_parents, bn_Net = bn
    w = 1
    event = copy.deepcopy(e)

    for i in range(len(nodes)):
        currentNode = nodes[i]
        vals = list()
        parents = nodes[nodes_parents[i]]
        location = 0

        for parent in parents:
            vals.append(event[parent])

        if (len(parents) == 2):
            if vals[0] == 1:
                if vals[1] == 1:
                    location = 0
                else:
                    location = 1
            else:
                if vals[1] == 1:
                    location = 2
                else:
                    location = 3

        if currentNode in e:
            probability = bn_Net[currentNode][event[currentNode]][location]
            w = w * probability

        else:
            probability = bn_Net[currentNode][True][location]
            prob = np.random.random()
            if prob <= probability:
                event[currentNode] = True
            else:
                event[currentNode] = False
    return w, event

def likelihood_weighting(X,e,bn,N):
    weights = [0,0]

    for count in range(N):
        w, event = weighted_sample(bn,e)

        if event[X[0]]:
            weights[0] = weights[0] + w
        else:
            weights[1] = weights[1] + w

    temp1 = weights[0]
    temp2 = weights[1]
    weights[0] = weights[0] / (temp1 + temp2)
    weights[1] = weights[1] / (temp1 + temp2)
    return weights