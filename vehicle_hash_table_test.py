# Testing vehicle_hash_table.py
from vehicle_hash_table import VehicleHashTable
from vehicle import Vehicle

def simple_test():
    # Create a vehicle hash table
    hash_table = VehicleHashTable()

    # Create and insert vehicles
    vehicle1 = Vehicle("BMW", "A", "B", 15.0, 80)
    vehicle2 = Vehicle("Mercedes", "A", "B", 13.0, 50)
    vehicle3 = Vehicle("Audi", "A", "B", 11.0, 70)
    hash_table.insert(vehicle1)
    hash_table.insert(vehicle2)
    hash_table.insert(vehicle3)

    # Search for the inserted vehicle by ID
    print("Searching for Vehicle BMW...\n")
    found_vehicle = hash_table.search("BMW")
    if found_vehicle:
        print(f"Found Vehicle: ID={found_vehicle.vehicle_id}, Location={found_vehicle.location}, "
              f"Destination={found_vehicle.destination}, Distance={found_vehicle.distance_to_dest}, "
              f"Battery={found_vehicle.battery_level}%")
    else:
        print("Vehicle not found.")

    # Display all vehicles in the hash table
    print("\nDisplaying all vehicles in the hash table:\n")
    hash_table.display()

if __name__ == "__main__":
    simple_test()
