class SortingLinkedList:
    def __init__(self):
        self.head = None  # Start with an empty linked list

    # Node class representing a node in the linked list
    class ListNode:
        def __init__(self, vehicle):
            self.vehicle = vehicle  # Vehicle data
            self.next = None  # Pointer to the next node

    # Swap the vehicle objects of two linked list nodes
    def swap(self, node1, node2):
        node1.vehicle, node2.vehicle = node2.vehicle, node1.vehicle

    # Get the length of the linked list
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # Traverse the linked list to get the node at the specified index
    def get_node_at_index(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current

    # Heapify a subtree rooted at index i in the linked list
    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Get the node at index 'largest', 'left', and 'right'
        largest_node = self.get_node_at_index(largest)
        left_node = self.get_node_at_index(left)
        right_node = self.get_node_at_index(right)

        # Check if left child exists and is larger than the root
        if left < n and left_node and left_node.vehicle.distance_to_dest > largest_node.vehicle.distance_to_dest:
            largest = left

        # Reassign 'largest_node' in case the largest has changed
        largest_node = self.get_node_at_index(largest)
        # Check if right child exists and is larger than the largest so far
        if right < n and right_node and right_node.vehicle.distance_to_dest > largest_node.vehicle.distance_to_dest:
            largest = right

        # Swap and heapify the subtree if needed
        if largest != i:
            # Swap the root and the largest node
            self.swap(self.get_node_at_index(i), self.get_node_at_index(largest))
            # Recursively heapify the affected subtree
            self.heapify(n, largest)

    # Perform heapsort on the linked list without converting to an array
    def heapsort(self):
        n = self.length()
        # Build the max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            self.swap(self.get_node_at_index(0), self.get_node_at_index(i))
            self.heapify(i, 0)

    # Partition the linked list for quicksort, using the node at index 'high' as the pivot
    def partition(self, low, high):
        pivot = self.get_node_at_index(high).vehicle.battery_level
        i = low - 1
        for j in range(low, high):
            if self.get_node_at_index(j).vehicle.battery_level >= pivot:
                i += 1
                self.swap(self.get_node_at_index(i), self.get_node_at_index(j))
        self.swap(self.get_node_at_index(i + 1), self.get_node_at_index(high))
        return i + 1

    # Quicksort the linked list by battery level
    def quicksort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quicksort(low, pi - 1)
            self.quicksort(pi + 1, high)

    # Add vehicle to linked list
    def add(self, vehicle):
        new_node = self.ListNode(vehicle)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        # Remove a vehicle by vehicle_id in the linked list
    def remove(self, vehicle_id):
        if not self.head:
            return
        if self.head.vehicle.vehicle_id == vehicle_id:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.vehicle.vehicle_id == vehicle_id:
                current.next = current.next.next
                return
            current = current.next

    # Display all vehicles in the linked list
    def display(self):
        current = self.head
        while current:
            vehicle = current.vehicle
            print(f"Vehicle ID {vehicle.vehicle_id}, Location: {vehicle.location}, "
                  f"Destination: {vehicle.destination}, Distance: {vehicle.distance_to_dest}, "
                  f"Battery: {vehicle.battery_level}%")
            current = current.next
