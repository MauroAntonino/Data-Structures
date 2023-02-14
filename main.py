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

from DataStructures.search_trees.binary_search_tree import TreeMap
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

from DataStructures.search_trees.splay_tree import SplayTreeMap
tree :SplayTreeMap = SplayTreeMap()
tree["a"] = 10
tree["b"] = 20
tree["c"] = 30
response = tree.find_min()
print(response)

