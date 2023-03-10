import math

from components.vector_3d import Vector3D
from components.utils import clamp_float


class CameraBase:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._camera_position = Vector3D()
        self._near_plane = 100.0
        self._far_plane = 200.0
        self._yaw = 0.0
        self._pitch = 0.0
        self._previous_pointer = (width / 2.0, height / 2.0)


class Camera(CameraBase):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)

    def handle_mouse_movement(self, x: float, y: float) -> None:
        px = self._previous_pointer[0]
        py = self._previous_pointer[1]

        dx = x - px
        dy = y - py

        sensitivity = 0.5
        self._yaw += dx * sensitivity
        self._pitch += dy * sensitivity
        self._previous_pointer = (x, y)

    def interpolate_scale(self, position: Vector3D, scale: float) -> float:
        pz = position.z
        near_plane = self._near_plane
        far_plane = self._far_plane

        if (pz + scale) < 0:
            return 0

        interpolation_value = (pz + near_plane) / (far_plane - near_plane)
        interpolated_scale = (pz + scale) * interpolation_value
        return interpolated_scale

    def calculate_yaw_projection(self, position: Vector3D) -> Vector3D:
        yaw_radians = math.radians(self._yaw)
        yaw_cos = math.cos(yaw_radians)
        yaw_sin = math.sin(yaw_radians)

        px = position.x
        py = position.y
        pz = position.z

        yaw_x = (px * yaw_cos) - (pz * yaw_sin)
        yaw_y = py
        yaw_z = (px * yaw_sin) + (pz * yaw_cos)

        yaw_vector = Vector3D(yaw_x, yaw_y, yaw_z)
        return yaw_vector

    def calculate_pitch_projection(self, position: Vector3D) -> Vector3D:
        pitch_radians = math.radians(self._pitch)
        pitch_cos = math.cos(pitch_radians)
        pitch_sin = math.sin(pitch_radians)

        px = position.x
        py = position.y
        pz = position.z

        pitch_x = px
        pitch_y = (py * pitch_cos) - (pz * pitch_sin)
        pitch_z = (py * pitch_sin) + (pz * pitch_cos)

        pitch_vector = Vector3D(pitch_x, pitch_y, pitch_z)
        return pitch_vector

    def calculate_perspective_projection(self, position: Vector3D):
        near_plane = self._near_plane
        far_plane = self._far_plane

        px = position.x
        py = position.y
        pz = position.z

        x = (px * near_plane) / pz
        y = (py * near_plane) / pz

        z = (far_plane + near_plane) / (near_plane - far_plane)
        w = -pz / (far_plane - near_plane)

        xprj = x * w
        yprj = y * w
        zprj = z * w

        projected_vector = Vector3D(xprj, yprj, zprj)
        return projected_vector

    def get_perspective_projection(self, position: Vector3D):
        position = self.calculate_yaw_projection(position)
        position = self.calculate_pitch_projection(position)

        if position.z == 0.0:
            return position

        position = self.calculate_perspective_projection(position)
        return position

    def increment_distance(self, increment: float):
        near_plane = self._near_plane
        far_plane = self._far_plane

        if (near_plane + increment) >= 0.0:
            near_plane += increment
            far_plane += increment
            self._near_plane = clamp_float(near_plane, 0.0, float("inf"))
            self._far_plane = clamp_float(far_plane, 0.0, float("inf"))
