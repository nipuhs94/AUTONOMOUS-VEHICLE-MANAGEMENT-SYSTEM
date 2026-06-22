# Importing necessary classes and functions from other modules
from graph import DSAGraph  # The graph structure for managing vertices as locations and edges as roads
from vehicle import Vehicle  # The Vehicle class to manage vehicle information
from vehicle_hash_table import VehicleHashTable, VehicleLinkedList, VehicleListNode   # Hash table for vehicle data storage
from sorting import * # Sorting algorithms to manage vehicle recommendations

# Main Program to manage the autonomous vehicle system
def main():
    # Initialize the graph and vehicle hash table
    graph = DSAGraph()  # Graph for managing locations and roads
    vehicle_hash_table = VehicleHashTable(size=10)  # Hash table to store vehicles
    vehicles = SortingLinkedList()  # Linked list to store vehicles

    # Main loop for user interaction
    while True:
        try:
            # Display the menu options to the user
            print("\n\t\t----- Welcome To The Autonomous Vehicle Management System ----\n")
            print("Select your choice according to the option menu below: \n")
            print("\n\t--Location Menu--")
            print("1. Add Location")
            print("2. Add Road Between Locations")
            print("3. Display Graph")
            print("4. Check Path Existence")
            print("5. Retreive neighbours")
            print("\n\t--Vehicle Menu--")
            print("6. Add Vehicle")
            print("7. Remove Vehicle")  
            print("8. Display All Vehicles")
            print("9. Find Nearest Vehicle by distance")
            print("10. Find Vehicle with Highest Battery Percentage")
            
            print("\n11. Exit\n")

            # Get the user's choice
            choice = input("Please Enter Your Choice (1-11): ")

# Add a location (node) to the graph
            if choice == '1':
                location = input("Enter location: ")
                if graph.find_node(location):
                    print(f"Location '{location}' already exists.")
                else:
                    graph.add_node(location)  # Add the location to the graph
                    print(f"Location '{location}' added.")


            # Add a road (edge) between two locations in the graph
            elif choice == '2':
                src = input("Enter starting location: ")
                dest = input("Enter destination location: ")
                dist = input("Enter distance between locations: ")
                graph.add_edge(src, dest, dist)  # Add an edge between start and destination locations

            # Display the graph (show all locations and roads)
            elif choice == '3':
                try:
                    graph.display_graph()  # Display the current state of the graph
                except Exception as e:
                    print(f"Error displaying graph: {e}")

            # Check if a path exists between two locations in the graph
            elif choice == '4':
                src = input("Enter start location: ")
                dest = input("Enter destination location: ")
                try:
                    if graph.is_path(src, dest):  # Check if there is a path between source and destination
                        print(f"Yes, a path exists between {src} and {dest}.")
                    else:
                        print(f"Sorry! No path exists between {src} and {dest}.")
                except KeyError:
                    print(f"One or both locations do not exist: {src}, {dest}")

            elif choice == "5":
                vertex = input("Enter the vertex to retrieve neighbors for: ")
                neighbors = graph.retrieve_neighbors(vertex)
                
                if neighbors is not None:
                    current = neighbors.get_head()
                    
                    if current is None:
                        print(f"{vertex} has no neighbors.")
                    else:
                        print(f"Neighbors of {vertex}: ", end="")
                        while current is not None:
                            print(f"{current.value}", end=" ")  # Print the neighbor's value
                            current = current.next
                        print()  # Newline after printing all neighbors
                else:
                    print(f"Vertex '{vertex}' does not exist in the graph.")

            # Add a vehicle to the system with specific attributes
            elif choice == '6':
                vehicle_id = input("Enter vehicle ID: ")
                
                # Check if vehicle already exists in the hash table
                if vehicle_hash_table.search(vehicle_id):
                    print(f"Error: Vehicle with ID '{vehicle_id}' already exists. Please enter a unique vehicle ID.")
                    continue

                location = input("Enter current location: ")
                destination = input("Enter destination: ")
                try:
                    distance = float(input("Enter distance to destination: "))  # Get the distance as a float
                    battery = float(input("Enter battery level: "))  # Get the battery level as a float
                except ValueError:
                    print("Invalid input! Distance and battery level must be numeric.")
                    continue

                vehicle = Vehicle(vehicle_id, location, destination, distance, battery)  # Create a vehicle
                vehicle_hash_table.insert(vehicle)  # Insert the vehicle into the hash table
                vehicles.add(vehicle)  # Add the vehicle to the custom linked list of vehicles
                print(f"Vehicle with ID '{vehicle_id}' has been successfully added.")


            # Remove a vehicle by vehicle ID
            elif choice == '7':  # Remove vehicle
                vehicle_id = input("Enter the vehicle ID to remove: ")
                vehicle_hash_table.delete(vehicle_id)  # Remove vehicle from the hash table
                vehicles.remove(vehicle_id)  # Remove vehicle from the linked list
                print(f"Vehicle '{vehicle_id}' has been removed.")

            elif choice == "8":
                print("Display all vehicles")
                vehicle_hash_table.display() 



            # Find and display the vehicle closest to its destination
            elif choice == '9':
                try:
                    vehicles.heapsort()  # Heapsort vehicles by distance to destination
                    nearest_vehicle = vehicles.get_node_at_index(0).vehicle  # Get the vehicle at the top after sorting
                    print(f"Nearest vehicle to destination: {nearest_vehicle.vehicle_id} at distance {nearest_vehicle.distance_to_dest}")
                except Exception as e:
                    print(f"Error finding nearest vehicle: {e}")

            # Find and display the vehicle with the highest battery level
            elif choice == '10':
                try:
                    vehicles.quicksort(0, vehicles.length() - 1)  # Quicksort vehicles by battery level
                    highest_battery_vehicle = vehicles.get_node_at_index(0).vehicle  # Get the vehicle with the highest battery
                    print(f"Vehicle with highest battery: {highest_battery_vehicle.vehicle_id} with {highest_battery_vehicle.battery_level}% battery")
                except Exception as e:
                    print(f"Error sorting vehicles by battery: {e}")
             

            # Exit the program
            elif choice == '11':
                break  # Break the loop and exit the program

            # Handle invalid user input
            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()

