# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

    def set(car, n, k, c, v):
        {car}.name = n
        {car}.kind = k
        {car}.colour = c
        {car}.value = v


# your code goes here
car1 = Vehicle()
car2 = Vehicle()

set(car1, "Fer", "convertible", "red", 60000)

# test code
print(car1.description())
print(car2.description())