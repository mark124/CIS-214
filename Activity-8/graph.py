"""
File: graph.py
Copyright 2015 by Ken Lambert

Adds the in, +, ==, and clone operations to support graph-specific behavior.
"""

from abstractcollection import AbstractCollection

class LinkedEdge(object):
    
    # An edge has a source vertex, a destination vertex,
    # a weight, and a mark attribute.

    def __init__(self, fromVertex, toVertex, weight = None):         
        self._vertex1 = fromVertex
        self._vertex2 = toVertex
        self._weight = weight 
        self._mark = False
    
    def clearMark(self):
        """Clears the mark on the edge."""
        self._mark = False
    
    def __eq__(self, other):
        """Two edges are equal if they connect
        the same vertices."""
        if self is other: return True
        if type(self) != type(other):
            return False
        return self._vertex1 == other._vertex1 and \
               self._vertex2 == other._vertex2

    def getFromVertex(self): # Derrf Seitz 12/17/2015
        """Returns the edge's origin vertex."""
        return self._vertex1
    
    def getOtherVertex(self,  thisVertex):
        """Returns the vertex opposite thisVertex."""
        if thisVertex == None or thisVertex == self._vertex2:
            return self._vertex1
        else:
            return self._vertex2

    def getToVertex(self):
        """Returns the edge's destination vertex."""
        return self._vertex2
    
    def getWeight(self):
        """Returns the edge's weight."""
        return self._weight
    
    def isMarked(self): 
        """Returns True if the edge is marked
        or False otherwise."""
        return self._mark
    
    def setMark(self):
        """Sets the mark on the edge."""
        self._mark = True
    
    def setWeight(self, weight):
        """Sets the weight on the edge to weight."""
        self._weight = weight     
          
    def __str__(self):
        """Returns the string representation of the edge."""
        return str(self._vertex1) + ">" + \
               str(self._vertex2)   + ":" + \
               str(self._weight)

class LinkedVertex(object):

    # A vertex has a label, a list of incident edges,
    # and a mark attribute.

    def __init__(self, label):
        self._label = label
        self._edgeList = list()
        self._mark = False

    def clearMark(self):
        """Clears the mark on the vertex."""
        self._mark = False;
    
    def getLabel(self): 
        """Returns the label of the vertex."""
        return self._label
    
    def isMarked(self): 
        """Returns True if the vertex is marked
        or False otherwise."""
        return self._mark
    
    def setLabel(self, label, g):
        """Sets the vertex's label to label."""
        g._vertices.pop(self._label, None)
        g._vertices[label] = self
        self._label = label          

    def setMark(self):
        """Sets the mark on the vertex."""
        self._mark = True
    
    def __str__(self):
        """Returns the string representation of the vertex."""
        return str(self._label)

    def __eq__(self, other):
        """Two vertices are equal if they have
        the same labels."""
        if self is other: return True
        if type(self) != type(other): return False
        return self.getLabel() == other.getLabel()
    
    def __hash__(self): # Derrf Seitz 12/16/2015
        """Hash method for a vertex."""
        return hash(self._label)

    # Methods used by LinkedGraph
    
    def addEdgeTo(self, toVertex, weight):
        """Connects the vertices with an edge."""
        edge = LinkedEdge(self, toVertex, weight)
        self._edgeList.append(edge)
    
    def getEdgeTo(self, toVertex):
        """Returns the connecting edge if it exists, or
        None otherwise."""
        edge = LinkedEdge(self, toVertex)
        try:
            return self._edgeList[self._edgeList.index(edge)]
        except:
            return None

    def incidentEdges(self):
        """Returns the incident edges of this vertex."""
        return iter(self._edgeList)
        
    def neighboringVertices(self):
        """Returns the neighboring vertices of this vertex."""
        vertices = list()
        for edge in self._edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)
            
    def removeEdgeTo(self, toVertex):
        """Returns True if the edge exists and is removed,
        or False otherwise."""
        edge = LinkedEdge(self, toVertex)
        if edge in self._edgeList:
            self._edgeList.remove(edge)
            return True
        else:
            return False


class LinkedDirectedGraph(AbstractCollection):

    # A graph has a count of vertices, a count of edges,
    # and a dictionary of label/vertex pairs.

    def __init__(self, sourceCollection = None):
        self._edgeCount = 0
        self._vertices = {}
        AbstractCollection.__init__(self, sourceCollection)
        
    # in, ==, +, and clone operations

    def __contains__(self, item):
        """Returns True if item is a label in a vertex,
        or False otherwise."""
        for vertex in self:
            if vertex.getLabel() == item:
                return True
        return False

    def clone(self):
        """Returns an exact copy of self, including vertex labels,
        edges connecting vertices, and edge weights."""
        newGraph = type(self)(map(lambda vertex: vertex.getLabel(), self))
        for vertex in self:
            for neighbor in vertex.neighboringVertices():
                edge = vertex.getEdgeTo(neighbor)
                newGraph.addEdge(vertex.getLabel(),
                                 neighbor.getLabel(),
                                 edge.getWeight())
        return newGraph

    def __add__(self, other):
        """Returns a new collection consisting of the
        items in self and other. This will be a graph with
        the contents of the operand graphs as separate components.
        Precondition: the labels in the two graph operands are disjoint.
        Raises: AttributeError if the labels in the two operand graphs
        are not disjoint."""
        newGraph = self.clone()
        for vertex in other:
            newGraph.add(vertex.getLabel())
        for vertex in other:
            for neighbor in vertex.neighboringVertices():
                edge = vertex.getEdgeTo(neighbor)
                newGraph.addEdge(vertex.getLabel(),
                                 neighbor.getLabel(),
                                 edge.getWeight())
        return newGraph

    def __eq__(self, other):
        """Returns True if self and other are identical, or
        True if self and other are of the same type, have the
        same number of vertices, and these vertices are connected
        in the same manner (including same labels and edge weights)."""
        # Check simple criteria first
        if self is other: return True
        if type(self) != type(other): return False
        if len(self) != len(other): return False
        for vertex in self:
            # All vertex labels must match
            if not vertex.getLabel() in other:
                print("Mismatched vertices")
                return False
            # Vertices with the same labels must have the same
            # incident edges
            otherVertex = other.getVertex(vertex.getLabel())
            selfEdges = list(vertex.incidentEdges())
            otherEdges = list(otherVertex.incidentEdges())
            if len(selfEdges) != len(otherEdges):
                return False
            for edge in selfEdges:
                found = False
                for otherEdge in otherEdges:
                    if edge == otherEdge and \
                       edge.getWeight() == otherEdge.getWeight():
                        found = True
                        break
                if not found: return False
        return True

    # Methods for clearing, marks, sizes, string rep

    def clear(self):
        """Clears the graph."""
        self._size = 0
        self._edgeCount = 0
        self._vertices = {}        

    def clearEdgeMarks(self):
        """Clears all the edge marks."""
        for edge in self.edges():
            edge.clearMark()
    
    def clearVertexMarks(self):
        """Clears all the vertex marks."""
        for vertex in self.vertices():
            vertex.clearMark()
    
    def sizeEdges(self):
        """Returns the number of edges."""
        return self._edgeCount
    
    def sizeVertices(self):
        """Returns the number of vertices."""
        return len(self)
    
    def __str__(self):
        """Returns the string representation of the graph."""
        result = str(len(self)) + " Vertices: "
        for vertex in self._vertices:
            result += " " + str(vertex)
        result += "\n";
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += " " + str(edge)
        return result

    def add(self, label):
        """For compatibility with other collections."""
        self.addVertex(label)

    # Vertex related methods
    
    def addVertex(self, label):
        """Precondition: a vertex with label must not
        already be in the graph.
        Raises: AttibuteError if a vertex with label
        is already in the graph."""
        if self.containsVertex(label):
            raise AttributeError("Label " + str(label) + " already in graph.""")
        self._vertices[label] = LinkedVertex(label)
        self._size += 1
        
    def containsVertex (self, label):
        return label in self._vertices
    
    def getVertex(self, label):
        """Precondition: a vertex with label must already be in the graph.
        Raises: AttibuteError if a vertex with label is not already in the graph."""
        if not self.containsVertex(label):
            raise AttributeError("Label " + str(label) + " not in graph.""")
        return self._vertices[label]
    
    def removeVertex(self,  label):
        """Returns True if the vertex was removed, or False otherwise."""
        removedVertex = self._vertices.pop(label, None)
        if removedVertex is None: 
            return False
        
        # Examine all other vertices to remove edges
        # directed at the removed vertex
        for vertex in self.vertices():
            if vertex.removeEdgeTo(removedVertex): 
                self._edgeCount -= 1

        # Examine all edges from the removed vertex to others
        for edge in removedVertex.incidentEdges():
            self._edgeCount -= 1
        self._size -= 1
        return True
    
    # Methods related to edges

    def addEdge(self, fromLabel, toLabel, weight):
        """Connects the vertices with an edge with the given weight.
        Preconditions: vertices with fromLabel and toLabel must
        already be in the graph.
        The vertices must not already be connected by an edge.
        Raises: AttibuteError if the vertices
        are not already in the graph or they are already connected."""
        fromVertex = self.getVertex(fromLabel)     
        toVertex   = self.getVertex(toLabel)
        if self.getEdge(fromLabel, toLabel):
            raise AttributeError("An edge already connects " + \
                                 str(fromLabel) + " and " + \
                                 str(toLabel))
        fromVertex.addEdgeTo(toVertex, weight)
        self._edgeCount += 1
    
    def containsEdge(self, fromLabel, toLabel):
        """Returns True if an edge connects the vertices,
        or False otherwise."""
        return self.getEdge(fromLabel, toLabel) != None
    
    def getEdge(self, fromLabel, toLabel):
        """Returns the edge connecting the two vertices, or None if
        no edge exists.
        Precondition: vertices with fromLabel and toLabel must
        already be in the graph.
        Raises: AttibuteError if the vertices
        are not already in the graph."""
        fromVertex = self.getVertex(fromLabel)     
        toVertex   = self.getVertex(toLabel)     
        return fromVertex.getEdgeTo(toVertex)
    
    def removeEdge (self, fromLabel, toLabel): 
        """Returns True if the edge was removed, or False otherwise.
        Precondition: vertices with fromLabel and toLabel must
        already be in the graph.
        Raises: AttibuteError if the vertices
        are not already in the graph."""
        fromVertex = self.getVertex(fromLabel)     
        toVertex   = self.getVertex(toLabel)     
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg: 
            self._edgeCount -= 1
        return edgeRemovedFlg

    # Iterators
    
    def __iter__(self):
        """Supports iteration over a view of self (the vertices)."""
        return self.vertices()

    def edges(self):
        """Supports iteration over the edges in the graph."""
        result = list()
        for vertex in self.vertices():
            result += list(vertex.incidentEdges())
        return iter(result)
    
    def vertices(self):
        """Supports iteration over the vertices in the graph."""
        return iter(self._vertices.values())

    def incidentEdges(self, label):
        """Supports iteration over the incident edges of the
        given verrtex.
        Precondition: a vertex with label must already be in the graph.
        Raises: AttibuteError if a vertex with label is not already in the graph."""
        return self.getVertex(label).incidentEdges()
    
    def neighboringVertices(self, label):
        """Supports iteration over the neighboring vertices of the
        given verrtex.
        Precondition: a vertex with label must already be in the graph.
        Raises: AttibuteError if a vertex with label is not already in the graph."""
        return self.getVertex(label).neighboringVertices()
    
