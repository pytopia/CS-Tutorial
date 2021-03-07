class Point:
    def __init__(self, *args):
        self.args = args

    def __abs__(self):
        sum_values = sum([item ** 2 for item in self.args])
        return sum_values ** 0.5

    def __gt__(self, obj):
        return abs(self) > abs(obj)

    def __repr__(self):
        return f"Point{self.args}"

def add(a, b):
    return a + b


__all__ = [Point]