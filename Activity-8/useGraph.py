# This program exercises graphs.

# Replace any "<your code>" comments with your own code statement(s)
# to accomplish the specified task.
# Do not change any other code.

# The following files must be in the same folder:
#  abstractcollection.py
#  graph.py

from graph import LinkedDirectedGraph

# Part 1:
# Complete the following function:
def topologicalSort(graph):  
    # <your code>
    graph = LinkedDirectedGraph()

# The graph represents the following course prerequisites:
# A requires nothing
# B requires nothing
# C requires A
# D requires A, B, and C
# E requires C
# F requires B and D
# G requires E and F
# H requires C, F, and G

# Part 2:
# Add the vertices:
# <your code>

    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    graph.addVertex("D")
    graph.addVertex("E")
    graph.addVertex("F")
    graph.addVertex("G")
    graph.addVertex("H")

# Part 3:
# Add the edges:
# <your code>

    graph.addEdge("A", "C", 0)

    graph.addEdge("A", "D", 0)
    graph.addEdge("B", "D", 0)
    graph.addEdge("C", "D", 0)

    graph.addEdge("C", "E", 0)

    graph.addEdge("B", "F", 0)
    graph.addEdge("D", "F", 0)

    graph.addEdge("E", "G", 0)
    graph.addEdge("F", "G", 0)

    graph.addEdge("C", "H", 0)
    graph.addEdge("F", "H", 0)
    graph.addEdge("G", "H", 0)
    

    print("Graph:")
    print(graph)


    print("Courses:")
# Part 4:
# Display each vertex on a separate line:
# <your code>

    for vertex in graph.vertices():
        print(str(vertex))
        

    print()
    print("Prerequisites:")
# Part 5:
# Display each edge on a separate line:
# <your code>

    for edge in graph.edges():
        print(str(edge))


    print("One possible order to take the courses:")
    
# Part 6:
# Display the courses in prerequisite (topological) order:
# <your code>

    stack = []

    for i in graph.vertices():
        if not i.isMarked():
            topologicalSortStack(i, stack)

    print(" ".join(str(x) for x in stack))

    print()

def topologicalSortStack(ver, stack):

    ver.setMark()

    for i in ver.neighboringVertices():
        if not i.isMarked():
            topologicalSortStack(i,stack)

    stack.insert(0, ver.getLabel())

topologicalSort(LinkedDirectedGraph)
