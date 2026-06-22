from vehicle import Vehicle
from sorting import SortingLinkedList  # Assuming your class was saved in sorting.py

def test_sorting():
    # Create an instance of SortingLinkedList to store vehicles
    vehicle_list = SortingLinkedList()

    # Create vehicles with ID, Location, Destination, Distance, and Battery Level
    vehicle1 = Vehicle("V1", "A", "B", 15, 90)
    vehicle2 = Vehicle("V2", "C", "D", 10, 80)
    vehicle3 = Vehicle("V3", "E", "F", 25, 60)

    # Add vehicles to the linked list
    vehicle_list.add(vehicle1)
    vehicle_list.add(vehicle2)
    vehicle_list.add(vehicle3)

    # Display vehicles before sorting
    print("\tBefore sorting by distance to destination:\n")
    vehicle_list.display()

    # Test Heapsort by distance to destination
    vehicle_list.heapsort()

    # Display vehicles after sorting by distance to destination
    print("\n\n\tAfter sorting by distance to destination:\n")
    vehicle_list.display()

    # Test Quicksort by battery level
    vehicle_list.quicksort(0, vehicle_list.length() - 1)

    # Display vehicles after sorting by battery level
    print("\n\n\tAfter sorting by battery level:\n")
    vehicle_list.display()

if __name__ == "__main__":
    test_sorting()
