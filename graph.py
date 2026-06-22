import numpy as np

# Node for Linked List to store values and point to the next node in list
class ListNode:
    def __init__(self, value, distance=None):
        self.value = value  # Store the graph node value
        self.distance = distance  # Distance to the connected node
        self.next = None  # Pointer to the next node

# Linked List 
class LinkedList:
    def __init__(self):
        self.head = None  # Points to the head node of the linked list

    # Add a new value and distance to the linked list
    def add(self, value, distance=None):
        new_node = ListNode(value, distance)  # Create a new node
        if not self.head:  # If the list is empty, make this node the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Add the new node at the end of the list

    # Remove a value from the linked list
    def remove(self, value):
        if not self.head:  # If the list is empty, return
            return
        if self.head.value == value:  # If the head node holds the value, remove it
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:  # Traverse and remove the matching node
                current.next = current.next.next
                return
            current = current.next

    # Check if the linked list contains a certain value
    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:  # If value is found, return True
                return True
            current = current.next
        return False  # Return False if value is not found

    # Get the head node of the linked list
    def get_head(self):
        return self.head

    # Find a value in the linked list and return the node
    def find(self, value):
        current = self.head
        while current:
            if current.value == value:  # Return the node if found
                return current
            current = current.next
        return None  # Return None if not found

# DSAGraphNode class
class DSAGraphNode:
    def __init__(self, value):
        self.value = value  # Value of the graph node
        self.adjacent = LinkedList()  # Use a LinkedList for storing neighboring nodes
        self.visited = False  

    # Add an adjacent node to this graph node with distance
    def add_adjacent(self, node, distance):
        if not self.adjacent.contains(node):  # Only add if it's not already in the list
            self.adjacent.add(node, distance)

    # Remove an adjacent node from this graph node
    def remove_adjacent(self, node):
        self.adjacent.remove(node)

    # Get the head of the adjacent nodes list
    def get_adjacent(self):
        return self.adjacent.get_head()

    # Mark this node as visited
    def set_visited(self):
        self.visited = True

    # Clear the visited status of this node
    def clear_visited(self):
        self.visited = False

    # Check if the node is visited
    def is_visited(self):
        return self.visited

# DSAGraph class 
class DSAGraph:
    def __init__(self):
        self.nodes = LinkedList()  # LinkedList to store the graph's nodes

    # Add a new node to the graph if it doesn't already exist
    def add_node(self, value):
        if not self.nodes.contains(DSAGraphNode(value)):  # Check if node exists before adding
            self.nodes.add(DSAGraphNode(value))

    # Find a node by its value in the graph
    def find_node(self, value):
        current = self.nodes.get_head()
        while current is not None:
            if current.value.value == value:  # If the value matches, return the node
                return current.value
            current = current.next
        return None  # Return None if the node is not found

    # Add an edge between two nodes in the graph with distance
    def add_edge(self, src_value, dest_value, distance):
        src_node = self.find_node(src_value)  # Find source node
        dest_node = self.find_node(dest_value)  # Find destination node
        if src_node and dest_node:  # If both nodes exist, add them as adjacent to each other with distance
            src_node.add_adjacent(dest_node, distance)
            dest_node.add_adjacent(src_node, distance)

    def retrieve_neighbors(self, vertex):
        vertex_node = self.find_node(vertex)

        if vertex_node is None:
            return None  # If the vertex is not found in the graph, return None

        neighbors = LinkedList()  # Create a LinkedList to store the neighbors

        # Traverse the adjacency linked list of the vertex
        adj_node = vertex_node.get_adjacent()

        while adj_node is not None:
            neighbor = adj_node.value  # Directly access the adjacent node 
            neighbors.add(neighbor.value)  # Add the neighbor to the neighbors linked list
            adj_node = adj_node.next  # Move to the next adjacent node

        return neighbors  # Return the linked list containing the neighbors

    # Check if a path exists between two nodes using depth-first search
    def is_path(self, source, destination):
        source_node = self.find_node(source)
        destination_node = self.find_node(destination)

        if source == destination:
            print("Source and destination is the same.")
            return True
        
        if source_node is None or destination_node is None:
            print(f"Either {source} or {destination} does not exist in the graph.")
            return False

        # Call the DFS function to check for a path
        return self.dfs(source, destination)

    # DFS traversal to find if there's a path between source and destination
    def dfs(self, source, destination):
        self.clear_visited()  # Clear the visited status of all nodes
        stack = LinkedList()  # Use linked list as a stack for DFS
        stack.add(self.find_node(source))  # Add the source node to the stack

        while stack.get_head() is not None:
            current_node = stack.get_head().value  # Get the top node from the stack
            stack.head = stack.head.next  # Pop the node from the stack

            if current_node.value == destination:  # If destination is reached, return True
                return True

            current_node.set_visited()  # Mark the node as visited
            neighbor = current_node.get_adjacent()  # Get the adjacent nodes of the current node

            # Iterate through all the neighbors of the current node
            while neighbor is not None:
                if not neighbor.value.is_visited():  # If neighbor is not visited, add to stack
                    stack.add(neighbor.value)
                neighbor = neighbor.next
        return False  # If DFS completes without finding the destination, return False

    # Clear the visited status of all nodes in the graph
    def clear_visited(self):
        current = self.nodes.get_head()
        while current is not None:
            current.value.clear_visited()  # Clear visited flag for each node
            current = current.next

    # Display the graph with each node, its adjacent nodes, and the distances
    def display_graph(self):
        # Traverse through all the nodes in the graph
        current = self.nodes.get_head()  # Get the head node of the graph's custom linked list
        while current is not None:
            node = current.value  # Get the current node
            print(f"{node.value}: ", end="")  # Print the node's value

            # Get the adjacent nodes and print them along with distances
            neighbor = node.get_adjacent()  # Get the adjacent nodes' head from the custom linked list
            while neighbor is not None:
                print(f"{neighbor.value.value} (Distance: {neighbor.distance}) ", end="")  # Print the adjacent node's value and distance
                neighbor = neighbor.next  # Move to the next adjacent node

            print()  
            current = current.next  # Move to the next node in the graph's linked list
