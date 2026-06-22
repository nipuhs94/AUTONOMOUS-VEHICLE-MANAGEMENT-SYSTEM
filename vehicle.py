class Vehicle:
    def __init__(self, vehicle_id, location, destination, distance_to_dest, battery_level):
        self.vehicle_id = vehicle_id  # Unique identifier for the vehicle
        self.location = location  # Current location of the vehicle
        self.destination = destination  # Destination of the vehicle
        self.distance_to_dest = distance_to_dest  # Distance to the destination
        self.battery_level = battery_level  # Battery level of the vehicle in percentage

    def set_location(self, location):
        self.location = location  # Set the current location

    def set_destination(self, destination):
        self.destination = destination  # Set the destination

    def set_distance_to_dest(self, distance):
        self.distance_to_dest = distance  # Set the distance to the destination

    def set_battery_level(self, level):
        self.battery_level = level  # Set the battery level

    def get_location(self):
        return self.location  # Get the current location

    def get_destination(self):
        return self.destination  # Get the destination

    def get_distance_to_dest(self):
        return self.distance_to_dest  # Get the distance to the destination

    def get_battery_level(self):
        return self.battery_level  # Get the battery level
