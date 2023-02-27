import math
from typing_extensions import Self


class Vector3D:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def multiply(self, num: float) -> Self:
        return Vector3D(self.x * num, self.y * num, self.z * num)

    def divide(self, num: float) -> Self:
        return Vector3D(self.x / num, self.y / num, self.z / num)

    def add_vector(self, vec: Self) -> Self:
        return Vector3D(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def subtract_vector(self, vec: Self) -> Self:
        return Vector3D(self.x - vec.x, self.y - vec.y, self.z - vec.z)

    def get_length(self) -> float:
        return math.sqrt(self.x**2.0 + self.y**2.0 + self.z**2.0)

    def set_magnitude(self, magnitude: float) -> Self:
        length = self.get_length()
        if length > 0:
            self.x = (self.x / length) * magnitude
            self.y = (self.y / length) * magnitude
            self.z = (self.z / length) * magnitude
        return Vector3D(self.x, self.y, self.z)