# Imagine a staircase with n steps. As you are climbing up this staircase,
# you either climb one or two steps at a time. The aim of this computing
# puzzle is to find out, using an algorithm, in how many distinct ways can
# you climb to the top?
# https://www.101computing.net/the-climbing-stairs-puzzle/ 
import time
def climb_stairs(stairs_steps, max_steps_at_time, path:list=[], all_paths:list=[]):
    '''
    Builds all the possible combination of paths to climb the stairs with
    the chosen combination of steps.
    '''
    if stairs_steps == 0:
        all_paths.append(path)
    for steps in range(1, (max_steps_at_time+1)):
        if stairs_steps >= steps:
            climb_stairs(stairs_steps-steps, max_steps_at_time, path+[steps], all_paths)
    return all_paths
def climb_stairs_memo(stairs_steps, max_steps_at_time, path:list=[], all_paths:dict={}):
    '''
    Builds all the possible combination of paths to climb the stairs with
    the chosen combination of steps.
    '''
    if stairs_steps in all_paths:
        return all_paths[stairs_steps]
    if stairs_steps == 0:
        all_paths[len(path)] = path
        return path
    subpath = []
    for steps in range(1, max_steps_at_time+1):
        if stairs_steps >= steps:
            climb_stairs_memo(stairs_steps-steps, max_steps_at_time, path+[steps], all_paths)
    # all_paths[stairs_steps] = subpath
    return all_paths[stairs_steps]
def count_ways_memo(n, memo:dict={}):
    '''
    Counts wais with a fixed number of possible steps to 2
    '''
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        memo[n]=n
        return memo[n]
    memo[n] = count_ways_memo(n-1, memo) + count_ways_memo(n-2, memo)
    return memo[n]

def count_wais_climb_stairs(stairs_steps:int, wais:int):
    '''
    Counts possible wais to climb with a selected number of 
    possible steps.
    '''
    if stairs_steps == 0 or stairs_steps == 1:
        return 1
    count=0
    for st in range(1,wais+1):
        if stairs_steps >= st:
            count += count_wais_climb_stairs(stairs_steps - st, wais)
    return count

def count_wais_climb_stairs_memo(stairs_steps:int, wais:int, memo={}):
    '''
    Counts possible wais to climb with a selected number of 
    possible steps, using memoization.
    '''
    if stairs_steps in memo:
        return memo[stairs_steps]
    if stairs_steps == 0 or stairs_steps == 1:
        memo[stairs_steps]=1
        return memo[stairs_steps]
    count=0
    for st in range(1,wais+1):
        if stairs_steps >= st:
            count += count_wais_climb_stairs_memo(stairs_steps - st, wais, memo)
    memo[stairs_steps] = count
    return memo[stairs_steps]

if __name__ == "__main__":
    # print(count_ways_memo(5))
    start_climb1=time.time()
    paths1 = climb_stairs(8,2)
    end_climb1=time.time()
    # print(paths1)
    # start_climb2=time.time()
    # paths2 = climb_stairs_memo(5,2)
    # end_climb2=time.time()
    # print(paths2)
    print(len(paths1))
    # print(len(paths2))

    # stairbox = 25
    # steps = 6
    # # paths = show_climb_stairs(stairbox, steps)
    # # print(paths)
    # # print(len(paths))
    # start1 = time.time()
    # climb1= count_wais_climb_stairs(stairbox, steps)
    # end1=time.time()
    # print(f"climb1: {climb1}, tardó: {end1-start1} segundos")
    # start2 = time.time()
    # climb2=count_wais_climb_stairs_memo(stairbox, steps)
    # end2 = time.time()
    # print(f"climb2: {climb2}, tardó: {end2-start2} segundos")
