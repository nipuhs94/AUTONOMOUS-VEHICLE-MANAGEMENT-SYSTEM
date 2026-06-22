# Node for Linked List in hash table
class VehicleListNode:
    def __init__(self, vehicle):
        self.vehicle = vehicle  # Store the vehicle object
        self.next = None  # Pointer to the next node

# Linked List for hash table buckets
class VehicleLinkedList:
    def __init__(self):
        self.head = None  # Start with an empty linked list

    # Add a vehicle to the linked list
    def add(self, vehicle):
        new_node = VehicleListNode(vehicle)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Search for a vehicle by vehicle_id in the linked list
    def search(self, vehicle_id):
        current = self.head
        while current:
            if current.vehicle.vehicle_id == vehicle_id:
                return current.vehicle
            current = current.next
        return None

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

    # Get the length of the linked list
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # Display all vehicles in the linked list
    def display(self):
        current = self.head
        while current:
            vehicle = current.vehicle
            print(f"Vehicle ID {vehicle.vehicle_id}, Location: {vehicle.location}, "
                  f"Destination: {vehicle.destination}, Distance: {vehicle.distance_to_dest}, "
                  f"Battery: {vehicle.battery_level}%")
            current = current.next

# Node for Linked List to store buckets in hash table
class BucketNode:
    def __init__(self, index, bucket):
        self.index = index  # Index of the hash table bucket
        self.bucket = bucket  # Vehicle linked list (bucket)
        self.next = None  # Pointer to the next bucket node

# Linked List to manage hash table buckets
class BucketLinkedList:
    def __init__(self):
        self.head = None  # Start with an empty linked list

    # Add a new bucket node to the linked list
    def add(self, index, bucket):
        new_node = BucketNode(index, bucket)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Find a bucket by index
    def find(self, index):
        current = self.head
        while current:
            if current.index == index:
                return current.bucket
            current = current.next
        return None

    # Display all buckets in the linked list
    def display(self):
        current = self.head
        while current:
            print(f"Bucket {current.index}:")
            current.bucket.display()
            current = current.next

# Vehicle Hash Table 
class VehicleHashTable:
    def __init__(self, size=10):
        self.size = size  # Set the hash table size
        self.buckets = BucketLinkedList()  # Use a linked list to manage the buckets
        self.count = 0  # Track the number of vehicles in the hash table

    # Hash function to generate an index based on the vehicle's ID
    def _custom_hash(self, vehicle_id):
        # Custom hashing algorithm: convert each character of vehicle_id to ASCII,
        # sum them, and take modulo with the hash table size
        hash_value = 0
        for char in vehicle_id:
            hash_value += ord(char)
        return hash_value % self.size

    # Insert a vehicle into the hash table
    def insert(self, vehicle):
        if (self.count / self.size) > 0.75:  # Resize when load factor exceeds 0.75
            self._resize()

        index = self._custom_hash(vehicle.vehicle_id)
        bucket = self.buckets.find(index)

        if bucket is None:  # If no bucket exists at that index, create one
            new_bucket = VehicleLinkedList()  # Create a new linked list bucket
            new_bucket.add(vehicle)  # Add the vehicle to the bucket
            self.buckets.add(index, new_bucket)  # Add the new bucket to the hash table
        else:
            bucket.add(vehicle)  # Add the vehicle to the existing bucket

        self.count += 1  # Increment the vehicle count

    # Search for a vehicle in the hash table
    def search(self, vehicle_id):
        index = self._custom_hash(vehicle_id)
        bucket = self.buckets.find(index)
        if bucket is not None:
            return bucket.search(vehicle_id)
        return None

    # Delete a vehicle from the hash table
    def delete(self, vehicle_id):
        index = self._custom_hash(vehicle_id)
        bucket = self.buckets.find(index)
        if bucket is not None:
            bucket.remove(vehicle_id)
            self.count -= 1  # Decrement the vehicle count

    # Display all vehicles in the hash table
    def display(self):
        self.buckets.display()  # Display all the buckets and their vehicles

    # Resize the hash table by using the next prime number after doubling the size
    def _resize(self):
        old_buckets = self.buckets
        new_size = self._next_prime(self.size * 2)  # Find the next prime number after doubling the size
        self.size = new_size
        self.buckets = BucketLinkedList()  # Create a new linked list for the resized buckets
        self.count = 0  # Reset the count since we will re-insert

        # Rehash all vehicles from old buckets to the new buckets
        current = old_buckets.head
        while current is not None:
            bucket = current.bucket
            vehicle_node = bucket.head
            while vehicle_node is not None:
                self.insert(vehicle_node.vehicle)  # Re-insert vehicle into the new hash table
                vehicle_node = vehicle_node.next
            current = current.next

    # Utility function to find the next prime number greater than n
    def _next_prime(self, n):
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        prime = n + 1
        while not is_prime(prime):
            prime += 1
        return prime
