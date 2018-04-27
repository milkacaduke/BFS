
'''
Our Graph:

	A  --  S  --  D  -- F
	|       \    / \   / \
 	Z          X --- C --- V
'''

# Build Graph
V = ['A', 'S', 'D', 'F', 'Z', 'X', 'C', 'V']
hashtable = {}
hashtable['A'] = ['Z']
hashtable['S'] = ['A', 'X', 'D']
hashtable['D'] = ['S', 'X', 'C', 'F']
hashtable['F'] = ['D', 'C', 'V']
hashtable['Z'] = []
hashtable['X'] = ['S', 'D', 'C']
hashtable['C'] = ['X', 'D', 'F', 'V']
hashtable['V'] = ['C', 'F']


def BFS(start, adj_list):
	# frontier, next, level, parent, i
	frontier = []
	next = []
	level = {}
	parent = {}
	i = 0

	# init start manually 
	frontier.append(start)
	level[start] = 0
	parent[start] = None
	i = 1

	while frontier:
		print("Processing (frontier): {}".format(frontier))
		next = []
		for f in frontier: # frontier = list of nodes to process
			print(f)
			adj_nodes = adj_list[f]
			for a in adj_nodes:
				if a not in level:
					level[a] = i
					parent[a] = f
					next.append(a)
					print("Adding {} in level   level:{}".format(a, level))
				else:
					print("{} already in level (seen)".format(a))
		print("Next: {}".format(next))
		frontier = next
		i += 1
		print("\n")

	return parent

def shortest_path(s, v, parent_dict):
	iter = v
	print("{} -> ".format(iter), end="")

	while iter in parent:
		if parent[iter] is None:
			print("")
			return

		iter = parent[iter]
		print("{} -> ".format(iter), end="")


def print_graph(V, adj_list):
	for v in V:
		print("{}: ".format(v), end="")
		for elm in adj_list[v]:
			# if len(adj_list[v]) == 0:
			# 	print('None', end="")
			print("{} ".format(elm), end="")
		print("")


def show_graph():
	print("	A  --  S  --  D  -- F")
	print("	|       \    / \   / \\")
	print("	Z         X --- C --- V")
	print("")





# Main stuff
# show_graph()
# parent = BFS('S', hashtable)
# shortest_path('S', 'V', parent)




	


