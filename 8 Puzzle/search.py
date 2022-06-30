# search
import state
import frontier

def search(n):
    # s = state.create(n) #create initial state
    s = [[4, 3, 7, 5, 8, 6, 1, 0, 2], ""]
    print(s)
    f = frontier.create(s)  # add initial state to frontier
    while not frontier.is_empty(f):  # run loop on all possible states
        s = frontier.remove(f)  # remove current state from frontier
        if state.is_target(s):  # target is reached , return target
            return [s, f[1], f[3]]  # [target state,number of states scanned,the largest frontier length reached]
        ns = state.get_next(s)  # get all possible next states
        for i in ns:  # add next states to frontier
            frontier.insert(f, i)
    return 0  # target wasn't reached return 0


print(search(3))
