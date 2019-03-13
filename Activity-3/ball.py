# Ball class

class Ball:

    # Class variable
    DEFAULT_RADIUS = 1

    # Constructor:
    def __init__(self, color, radius = DEFAULT_RADIUS):
        self.color = color;
        self.radius = radius;

    # Special methods:
    def __eq__(self, other):
        if self is other:
            return True
        if (type(self) != type(other)) or \
           (self.color != other.color) or \
           (self.radius != other.radius):
            return False
        return True

    def __str__(self):
        return (self.color + " ball, radius " + str(self.radius))

    # Accessor methods:
    def getColor(self):
        return self.color

    def getRadius(self):
        return self.radius

    # Mutator methods:
    def setColor(self, color):
        self.color = color

    def setRadius(self, radius):
        self.radius = radius
