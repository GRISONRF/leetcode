"""
Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

We use two lists of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Example 1:

Input: 
pid =  [1, 3, 10, 5]  #child
ppid = [3, 0, 5, 3]  #parent
kill = 5
Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
Note:

The given kill id is guaranteed to be one of the given PIDs.
n >= 1.

https://www.youtube.com/watch?v=PmUt5ctBUE0
leetcode 582

build the tree/graph and traverse(BFS) until we find the kth element and remove it and it's childs


"""

# import collections


# def killProcess(pid, ppid, kill):

#     #represent the given input as a graph
#     graph = collections.defaultdict(list)

#     #each key will be a node and value will be all of its children's node as a list
#     for child, parent in zip(pid, ppid):
#         graph[parent].append(child)

#     # start at the parent node (the kill) and traverse all the nodes beneth the parent, add it to the ans and return it // start of BFS
#     ans = []
#     queue = collections.deque([kill])  # initialize the queue with the starting point

#     while queue:
#         to_kill = queue.popleft() #current process
#         ans.append(to_kill)

#         # traversing the next level /if that node is in the graph, meaning it has children
#         if to_kill in graph:
#             queue.extend(graph[to_kill])  # put all of its children in the queue, cause we want to kill them all
        
#     # when queue is empty means we kill the processes and they were appended to the ans
#     print(ans)

#     # T: O(n)   M:O(n)





# pid = [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# kill = 5

# killProcess(pid, ppid, kill)


""" 
input: list, list, int
ouput: list

find all the processes that will be killed when we kill the target process [parent(kill) and its children]


dict to map the parent and child relationships

find the kill in map and return the kill + all its values

"""

import collections
def kill_processes(pid, ppid, kill):

    relationships = collections.defaultdict(list)

    for parent, child in zip(ppid, pid):
        relationships[parent] += [child]

    ans = []
    for k, v in relationships.items():
        if k == kill:
            for i in v:
                ans.append(i)
            ans.append(k)
    return ans

print(kill_processes([1, 3, 10, 5], [3, 0, 5, 3], 5))