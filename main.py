class Components:
    def __init__(self, name: str, service_criteria: int, criteria_type: str):
        self.name = name
        self.service_criteria = service_criteria
        self.criteria_type = criteria_type

class Engine(Components):
    def __init__(self, name, service_criteria, criteria_type):
        # Call the constructor of the parent class (Components)
        super().__init__(name, service_criteria, criteria_type)

class Battery(Components):
    def __init__(self, name, service_criteria, criteria_type):
        # Call the constructor of the parent class (Components)
        super().__init__(name, service_criteria, criteria_type)

class Tires(Components):
    def __init__(self, name, service_criteria, criteria_type):
        # Call the constructor of the parent class (Components)
        super().__init__(name, service_criteria, criteria_type)

class Car:
    def __init__(self,name, engine, battery, tires):
        self.name = name
        self.engine = engine
        self.battery = battery
        self.tires = tires

# Create instances of the each component class
capulet_engine = Engine("Capulet Engine", 30000, "miliage")
willoughby_engine =Engine("Willoughby Engine", 60000, "miliage")
sternman_engine = Engine("Sternman Engine", 0, "warning light")
spindler_battery = Battery("Spindler Battery", 2, "time period")
nubbin_battery = Battery("Nubbin Battery", 4, "time period")
# Dummy tire instance
dummy_tire = Tires("Dummy Tires", 50000, "miliage")

# Create instances for car
calliope  = Car("Calliope", capulet_engine, spindler_battery, dummy_tire)
glissade = Car("Glissade", willoughby_engine, spindler_battery, dummy_tire)
palindrome = Car("Palindrome", sternman_engine, spindler_battery, dummy_tire)
rorschach = Car("Rorschach", willoughby_engine, nubbin_battery, dummy_tire)
thovex = Car("Thovex", capulet_engine, nubbin_battery, dummy_tire)