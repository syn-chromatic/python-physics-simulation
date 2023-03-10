import random

from components.shape import Shape
from components.particle import Particle
from components.color import RGBA
from components.vertices import SphereShape, CubeShape, ParticleCircle


def get_center_cube():
    mass = 10_000_000
    shape = CubeShape().get_shape()
    color = RGBA(0.8, 0.3, 0.3, 1.0)
    scale = mass / 250_000

    body = Shape(shape)
    body.set_color(color)
    body.physics.set_mass(mass)
    body.physics.set_scale(scale)
    body.physics.set_spin_velocity(50, 50, 0)
    return body


def get_center_sphere():
    mass = 10_000_000
    shape = SphereShape(10, 10, 10).get_shape()
    color = RGBA(0.8, 0.3, 0.3, 1.0)
    scale = mass / 250_000

    body = Shape(shape)
    body.set_color(color)
    body.physics.set_mass(mass)
    body.physics.set_scale(scale)
    body.physics.set_spin_velocity(50, 50, 0)
    return body


def get_cube_t1():
    px = random.uniform(-50, -40)
    py = random.uniform(-50, -40)
    pz = 0

    mass = random.uniform(50, 100)
    shape = CubeShape().get_shape()
    scale = mass / 20

    body = Shape(shape)
    body.physics.set_position(px, py, pz)
    body.physics.set_velocity(10, 30, 5)
    body.physics.set_mass(mass)
    body.physics.set_scale(scale)
    return body


def get_particle_t1():
    px = 0
    py = 10
    pz = 0

    mass = 30
    shape = [(0.0, 0.0, 0.0)]
    scale = mass

    vx = 1000
    vy = 0

    body = Particle(shape)
    body.physics.set_position(px, py, pz)
    body.physics.set_velocity(vx, vy, 0)
    body.physics.set_mass(mass)
    body.physics.set_scale(scale)
    return body


def get_particle_t2():
    px = -300
    py = -20
    pz = 0

    mass = 30
    shape = [(0.0, 0.0, 0.0)]
    scale = mass

    vx = 1000
    vy = 0

    body = Particle(shape)
    body.physics.set_position(px, py, pz)
    body.physics.set_velocity(vx, vy, 0)
    body.physics.set_mass(mass)
    body.physics.set_scale(scale)
    return body


def get_particle_t3():
    px = 150
    py = 10
    pz = 0

    mass = 30
    shape = CubeShape().get_shape()
    scale = 10

    color = RGBA(0.8, 0.2, 0.2, 1.0)

    body = Particle(shape)
    body.physics.set_position(px, py, pz)
    body.physics.set_velocity(-10000, 0, 0)
    body.physics.set_mass(mass)
    body.physics.set_scale(scale)
    body.set_color(color)
    return body


def get_particle_t4(px, py):
    pz = 0

    mass = 30
    shape = [(0.0, 0.0, 0.0)]
    scale = mass

    vx = 500
    vy = 0

    body = Particle(shape)
    body.physics.set_position(px, py, pz)
    body.physics.set_velocity(vx, vy, 0)
    body.physics.set_mass(mass)
    body.physics.set_scale(scale)
    return body


def get_particle_t5(px, py):
    pz = 0

    mass = 30
    shape = [(0.0, 0.0, 0.0)]
    scale = mass

    vx = -20_000
    vy = 80_000

    body = Particle(shape)
    body.physics.set_position(px, py, pz)
    body.physics.set_velocity(vx, vy, 0)
    body.physics.set_mass(mass)
    body.physics.set_scale(scale)
    return body


def get_particle_t6() -> Particle:
    px = random.uniform(-200, -60)
    py = random.uniform(-50, -100)
    pz = 0

    mass = random.uniform(1, 5)
    shape = [(0.0, 0.0, 0.0)]
    scale = mass

    body = Particle(shape)
    body.physics.set_position(px, py, pz)
    body.physics.set_velocity(-10, -30, 0)
    body.physics.set_mass(mass)
    body.physics.set_scale(scale)
    return body


def get_particle_t7(px: float, py: float) -> list[Particle]:
    particles = ParticleCircle(20).generate(px, py)
    bodies = []

    for particle in particles:
        px = particle[0]
        py = particle[1]
        pz = 0

        mass = particle[2]
        shape = [(0.0, 0.0, 0.0)]
        scale = particle[2]

        body = Particle(shape)
        body.physics.set_position(px, py, pz)
        body.physics.set_velocity(0, 0, 0)
        body.physics.set_mass(mass)
        body.physics.set_scale(scale)
        bodies.append(body)
    return bodies
