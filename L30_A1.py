class vehicle():

    def __init__(self, name, max_speed, mileage ):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class bus(vehicle):
    pass
school_bus= bus("volvo", 180, 12)
print("Vehicle_name:",school_bus.name,"\nmax speed:",school_bus.max_speed,"\nmileage:",school_bus.mileage,"\n")
