# from DataStructures.trees.binary_tree import LinkedBinaryTree

# tree :LinkedBinaryTree = LinkedBinaryTree()
# root_pos = tree.add_root(1)
# left_pos = tree.add_left(root_pos,0)
# left_pos_2 = tree.add_left(left_pos,-2)
# left_pos_3 = tree.add_left(left_pos_2,-4)
# right_pos = tree.add_right(left_pos_2,-3)
# # print(type(tree._root))
# # print(tree.num_children(root_pos))
# # print(tree._root._element)
# for iten in tree:
#     print(iten)
    

# from DataStructures.priority_queue.unsorted_priority_queue import UnsortedPriorityQueue
# from DataStructures.priority_queue.sorted_prority_queue import SortedPriorityQueue
# from DataStructures.priority_queue.heap import HeapPriorityQueue
# # import heapq

# pQueue :SortedPriorityQueue = SortedPriorityQueue()
# pQueue.add(2, "fisrt")
# pQueue.add(2, "second")
# pQueue.add(3, "last")
# resp = pQueue.min()
# print(resp)
# print(len(pQueue))
# pQueue.remove_min()
# resp = pQueue.min()
# print(resp)

# from DataStructures.search_trees.binary_search_tree import TreeMap
# tree :TreeMap = TreeMap()
# tree["a"] = 10
# tree["b"] = 20
# tree["c"] = 30
# response = tree.find_min()
# print(response)

# from DataStructures.search_trees.avl_tree import AVLTreeMap
# tree :AVLTreeMap = AVLTreeMap()
# tree["a"] = 10
# tree["b"] = 20
# tree["c"] = 30
# response = tree.find_min()
# print(response)

# from DataStructures.search_trees.splay_tree import SplayTreeMap
# tree :SplayTreeMap = SplayTreeMap()
# tree["a"] = 10
# tree["b"] = 20
# tree["c"] = 30
# response = tree.find_min()
# print(response)


# from DataStructures.search_trees.red_black_tree import RedBlackTreeMap
# tree :RedBlackTreeMap = RedBlackTreeMap()
# tree["a"] = 10
# tree["b"] = 20
# tree["c"] = 30
# response = tree.find_min()
# print(response)

from DataStructures.graph.graph import Graph
from DataStructures.graph.BFS import BFS
from DataStructures.graph.DFS import DFS
from DataStructures.graph.Dijkstra import shortest_path_lengths, shortest_path_tree
from DataStructures.graph.prim_arnik import MST_PrimJarnik
from DataStructures.graph.kruskal import MST_Kruskal

graph :Graph = Graph()
graph.insert_vertex(1)
graph.insert_vertex(2)
graph.insert_vertex(3)
graph.insert_vertex(4)

graph.insert_edge(1,2,1)
graph.insert_edge(1,3,2)
graph.insert_edge(3,4,1)
print(graph.edges())
discovered = {}
DFS(graph, 1, discovered)
print(discovered)
BFS(graph, 1, discovered)
print(discovered)
response = shortest_path_lengths(graph, 1)
print(response)
response = shortest_path_tree(graph, 1, discovered)
print(response)

response = MST_PrimJarnik(graph)
var = [ item.element() for item in response ]
print(var)
response = MST_Kruskal(graph)
var = [ item.element() for item in response ]
print(var)