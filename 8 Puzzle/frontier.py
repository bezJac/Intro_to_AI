import state


# implements a priority queue

# [list of states, total num of states, curr. num. of states, max. num. of states]
def create(s):
    return [[s], 0, 0, 0]


# check if frontier has any states in it
def is_empty(f):
    return f[0] == []


# implements the A* algorithm
# get value of state
def val(s):
    return state.hdistance(s) + state.path_len(s)


# Uniform Cost: return state.path_len(s)
# Greedy Best First: return state.hdistance(s)

def insert(h, s):
    # inserts state s to the frontier
    f = h[0]  # point to frontier first element
    h[1] += 1  # increase by one count of total states scanned
    h[2] += 1  # increase by one count of current states in the frontier
    if h[2] > h[3]:  # set max count to the max value between total or current
        h[3] = h[2]
    f.append(s)  # add new state to end of frontier
    i = len(f) - 1
    while i > 0 and val(f[i]) < val(f[(i - 1) // 2]):  # sort frontier to implement priority queue
        t = f[i]  # set last state to temp variable
        f[i] = f[(i - 1) // 2]  # switch between last state with its father
        f[(i - 1) // 2] = t
        i = (i - 1) // 2


def remove(h):
    if is_empty(h):
        return 0
    h[2] -= 1
    f = h[0]
    s = f[0]
    f[0] = f[len(f) - 1]
    del f[-1]
    heapify(f, 0)
    return s


def heapify(f, i):
    minSon = i
    if 2 * i + 1 < len(f) and val(f[2 * i + 1]) < val(f[minSon]):
        minSon = 2 * i + 1
    if 2 * i + 2 < len(f) and val(f[2 * i + 2]) < val(f[minSon]):
        minSon = 2 * i + 2
    if minSon != i:
        t = f[minSon]
        f[minSon] = f[i]
        f[i] = t
        heapify(f, minSon)
