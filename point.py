class Point:
    def __init__(self, x, y):
        self.point = {"x": x, "y": y}
    
    def __getitem__(self, item):
        return self.point[item]