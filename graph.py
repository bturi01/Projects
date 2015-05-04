""" A Python Class
A simple python graph class, demonstrating the essential
facts and functionalities of graphs
"""

class Graph(object):
	def __init__(self,graph_dict=()):
		""" Initializes a graph object """
		self.__graph_dict = graph_dict

		def verticies(self):
			""" Returns the veritices of a graph"""
			return list(self.__graph_dict.keys())
		def edges(self):
			""" Returns the edges of a graph"""
			return self.__generate_edges()
		def addVertex(self, vertex):
			""" If the Vertex is not in self.__graph_dict,
			a key "vertex" with an empty list value is added
			to the dictionary. Otherwise nothing has to be done
			"""
			if vertex not in self.__graph_dict:
				self.__graph_dict[vertex] = []
				def addEdge(self,edge):
					""" assumes that edge is of type set
					tuple or list; between two verticies
					can be multiple edges
					"""
					edge = set (edge)

