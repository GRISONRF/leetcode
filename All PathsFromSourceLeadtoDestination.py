import collections
""" Given the edges of a directed graph, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually end at destination, that is:

At least one path exists from the source node to the destination node
If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
The number of possible paths from source to destination is a finite number.
Return true if and only if all roads from source lead to destination.

Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
Output: false
Explanation: It is possible to reach and get stuck on both node 1 and node 2.
Example 2:

Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
Output: false
Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.
Example 3:

Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
Output: true
Example 4:

Input: n = 3, edges = [[0,1],[1,1],[1,2]], source = 0, destination = 2
Output: false
Explanation: All paths from the source node end at the destination node, but there are an infinite number of paths, such as 0-1-2, 0-1-1-2, 0-1-1-1-2, 0-1-1-1-1-2, and so on.
Example 5:

Input: n = 2, edges = [[0,1],[1,1]], source = 0, destination = 1
Output: false
Explanation: There is infinite self-loop at destination node. """


# when there's a infinte loop: return false
# starting at sourse, if there's a path that does not end at the destination, return false

#Depth first search
# determine if all paths starting form source lead to destination
# creates a graph using the edges and uses recursion to check if all paths end at destination 
# set to store the nodes that have been visited
#returns false if it finds a node that has no outgoing edges or has already visited the node or it reaches the same node from which it has came from
# dict to store the edges of the graph, making easier to keep track of the edges between the different nodes


def leadsToDestination(n, edges, source, destination):

    #set to keep track of nodes we've seen 
    seen = set()

    #dict to store edges of graph. doing this we get a key with all it's childs as the values
    graph = collections.defaultdict(set)

    for a, b in edges:
        graph[a].add(b)

    #starting of DFS   // important to note: i represents a NODE
    def dfs(i):
        #mark current node as seen
        seen.add(i)

        #iterate through all the edges of current node:
        for j in graph[i]:
            #if j == 1, means its an infinite self loop. if j is in seen, means there's a circular loop somewhere, if the path from the current node i through the node j does not lead to the destination.
            if j == i or j in seen or not dfs(j):
                return False
        #if the foor loop is over, means the path starting at i through j leads to the path, so we can remove i from the seen because this node has been fully processed and all paths starting from this node have been checked
        seen.discard(i)

        #if the current node has any outgoing edges or if the current node is the destination
        return len(graph[i]) != 0 or i == destination
    
    #start the DFS from the source
    return dfs(source)
        

