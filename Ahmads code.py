import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("car_data.db")
cursor = conn.cursor()

# Create a table for cars
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY,
        car_name TEXT,
        engine_name TEXT,
        engine_criteria TEXT,
        engine_criteria_type TEXT,
        battery_name TEXT,
        battery_criteria TEXT,
        battery_criteria_type TEXT
    )
""")
conn.commit()

class ServiceCriteria:
    def __init__(self, criteria, criteria_type):
        self.criteria = criteria
        self.criteria_type = criteria_type

class CarComponent:
    def __init__(self, component_type):
        self.component_type = component_type
        self.service_criteria = None

    def set_service_criteria(self, criteria, criteria_type):
        self.service_criteria = ServiceCriteria(criteria, criteria_type)

    def get_service_criteria(self):
        return self.service_criteria

class Tire(CarComponent):
    def __init__(self, tire_name):
        super().__init__("Tire")
        self.tire_name = tire_name

class Battery(CarComponent):
    def __init__(self, battery_name):
        super().__init__("Battery")
        self.battery_name = battery_name

class Engine(CarComponent):
    def __init__(self, engine_name):
        super().__init__("Engine")
        self.engine_name = engine_name

# Adding car data to the database
def add_car_to_database(car_name, engine, battery):
    cursor.execute("""
        INSERT INTO cars (car_name, engine_name, engine_criteria, engine_criteria_type, battery_name, battery_criteria, battery_criteria_type)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (car_name, engine.engine_name, engine.get_service_criteria().criteria, engine.get_service_criteria().criteria_type, battery.battery_name, battery.get_service_criteria().criteria, battery.get_service_criteria().criteria_type))
    conn.commit()



# Creating car components

# 0 is for time in years 
# 1 is for distance 
# 2 is for warning light
tire_sample = Tire("Sample Tire")
tire_sample.set_service_criteria(10000, 1)  # No service criteria for tires

battery_spindler = Battery("Spindler")
battery_spindler.set_service_criteria(2, 0)

battery_nubbin = Battery("Nubbin")
battery_nubbin.set_service_criteria(4, 0)

engine_capulet = Engine("Capulet")
engine_capulet.set_service_criteria(30000, 1)

engine_willoughby = Engine("Willoughby")
engine_willoughby.set_service_criteria(60000, 1)

engine_sternman = Engine("Sternman")
engine_sternman.set_service_criteria(0, 2)

# Adding car data to the database
cars = [
    ("Calliope", engine_capulet, battery_spindler, tire_sample),
    ("Glissade", engine_willoughby, battery_spindler, tire_sample),
    ("Palindrome", engine_sternman, battery_spindler, tire_sample),
    ("Rorschach", engine_willoughby, battery_nubbin, tire_sample),
    ("Thovex", engine_capulet, battery_nubbin,tire_sample)
]

for car_name, engine, battery in cars:
    add_car_to_database(car_name, engine, battery)

