class engine:
    def __init__(self,last_service_miliage, warning_light):
        self.last_service_miliage = last_service_miliage
        self.warning_light = warning_light

class battery:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

class tires:
    def __init__(self, last_service_date, last_service_milaige):
        self.last_service_date = last_service_date
        self.last_service_milaige = last_service_milaige

class car(engine, battery, tires):
    pass