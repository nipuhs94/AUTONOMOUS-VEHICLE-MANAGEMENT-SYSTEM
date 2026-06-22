# Test for Vehicle.py
from vehicle import Vehicle

def test_vehicle():
    # Create a vehicle object
    vehicle = Vehicle("V001", "A", "B", 10.5, 80)

    # Test getters
    assert vehicle.get_location() == "A"
    assert vehicle.get_destination() == "B"
    assert vehicle.get_distance_to_dest() == 10.5
    assert vehicle.get_battery_level() == 80

    # Test setters
    vehicle.set_location("C")
    vehicle.set_destination("D")
    vehicle.set_distance_to_dest(20.0)
    vehicle.set_battery_level(90)

    # Test updated values
    assert vehicle.get_location() == "C"
    assert vehicle.get_destination() == "D"
    assert vehicle.get_distance_to_dest() == 20.0
    assert vehicle.get_battery_level() == 90
    print("Testing 1,2,3\n")
    print(f"Battery level is: {vehicle.battery_level}")
    print(f"Destination is: {vehicle.destination}")
    print(f"Distance to destination is: {vehicle.distance_to_dest}")
    print(f"Location is: {vehicle.location}")
    print("No error? Then it still works ;)\n")

if __name__ == "__main__":
    test_vehicle()
