class Vehicles:
    """ Parent class for all vehicles """
    def __init__(self, name, manufacturer, color):
        self.name   = name
        self.manufacturer = manufacturer
        self.color  = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def direction(self, direction):
        print(self.name, " is turning to", direction)

    def brake(self):
        print(self.name, "is stopping")

if __name__=="__main__":
    v  = Vehicles("Allion 2015", "Toyota", "Black")
    v1 = Vehicles("OD A6", "OD", "Blue")
    v2 = Vehicles("Rolls royes", "Rolls", "Red")

    v.drive()
    v.direction("turning left")
    v.brake()
