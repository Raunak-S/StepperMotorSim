class Circle:
    def __init__(self, in_name, in_angle, in_circle):
        self.name = in_name
        self.x = 0
        self.y = 0
        self.angle = in_angle
        self.circle = in_circle

    def __str__(self):
        return self.name