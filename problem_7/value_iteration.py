from mdp import MDP
import time

start_time = time.time()


def value_iteration(mdp, threshold):
    # Initalize U'
    prev_u = []
    curr_u = [0 for i in range(len(mdp.get_states()))]

    iterations = 0
    while True:
        # U = U'
        prev_u = curr_u.copy()
        curr_threshold = 0
        for node in mdp.get_states():
            # U'[s] = r(s) + gamma * max(sum[P(s'|s, a) * U[s']])
            curr_u[node - 1] = mdp.reward(node) + \
                (mdp.discount() * get_max_M(mdp, node, prev_u))
            curr_threshold = max(curr_threshold, abs(
                curr_u[node - 1] - prev_u[node - 1]))
        # if δ <= (epsilon(1 - gamma))/gamma
        if curr_threshold <= (threshold * (1 - mdp.discount())) / mdp.discount():
            break
        iterations += 1
        print(str(iterations) + ": " + str(prev_u) +
              "\n\t" + "a" + str(optimal_policy(mdp, prev_u)))
    print("Number of Iterations: " + str(iterations))
    # Return U
    return prev_u


def get_max_M(mdp, node, prev_u):
    mmax = -float("inf")
    for action in mdp.get_actions(node):
        m = M_val(mdp, node, action, prev_u)
        mmax = max(m, mmax)
    return mmax


def M_val(mdp, node, action, prev_u):
    return sum(mdp.transition(node, action, i + 1) * prev_u[i] for i in range(len(mdp.get_states())))


def optimal_policy(mdp, utility_1):
    # Initalize π* (policy)
    policy = [0 for i in range(len(mdp.get_states()))]

    for node in mdp.get_states():
        argmax = -float("inf")
        max_action = -1
        for action in mdp.get_actions(node):
            # sum[P(s'|s, a) * U[s']
            m = M_val(mdp, node, action, utility_1)
            # argmax(sum)
            if m > argmax:
                argmax = m
                max_action = action
        # π*(s) = argmax(sum)
        policy[node - 1] = max_action
    # Return π*
    return policy


end_time = time.time()
computation_time = end_time - start_time

if __name__ == '__main__':
    mdp = MDP()
    utilities = value_iteration(mdp, .00001)
    policy = optimal_policy(mdp, utilities)
    print("\n")
    print("Optimal Utilities: " + str(utilities))
    print("\n")
    print("Optimal Policy: " + str(policy))
    print("\n")
    print("Computation Time: ", computation_time, "seconds")
