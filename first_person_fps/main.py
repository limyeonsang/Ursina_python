from errno import ENOTEMPTY
from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from random import randint, uniform


app = Ursina()

player = FirstPersonController()

Sky()
PointLight(parent=camera, color=color.dark_gray, position=(0,5,-5))
AmbientLight(color=color.rgb(100,100,100))
ground = Entity(model='cube', scale=(100,1,100), collider='box', texture='white_cube')

class Wall(Entity):
    def __init__(self, scale, position, rotation):
        super().__init__(
            model='cube',
            scale=scale,
            position=position,
            rotation=rotation,
            collider='box'
        )

for _ in range(20):
    tree = Wall(
        scale=(randint(2,5),randint(2,7),randint(2,5)),
        position=(randint(-47,47), 1, randint(-47,47)),
        rotation=(randint(-5,5), randint(0,360), randint(-5,5))
    )

class Weapon(Entity):
    def __init__(self, scale, position, rotation):
        super().__init__(
            model='source/gun/obj/AK74_LOD1.obj',
            texture='source/gun/textures/ak74m_2DView.png',
            parent=camera.ui,
            scale=scale,
            position=position,
            rotation=rotation
        )
weapon = Weapon(
    scale=2.4,
    position=(0.8, -0.6),
    rotation=(-10,-15,-5)
)

class Enemy(Entity):
    def __init__(self, scale, position, rotation):
        super().__init__(
            model='source\enemy\low_poly_man.obj',
            texture='source\enemy\low_poly_character_texture.png',
            scale=scale,
            position=position,
            rotation=rotation,
            collider = 'box'
        )

num_of_enemies = 10
enemies = [None]*num_of_enemies
for i in range(num_of_enemies):
    enemy_x_position = uniform(-47,47)
    enemy_z_position = uniform(-47,47)
    enemies[i] = Enemy(
        scale=(0.65,0.5,1),
        position=(enemy_x_position, 0.45, enemy_z_position),
        rotation=(1, randint(0,360), 1)
    )
    enemies[i].animate_x(enemy_x_position+1.2, duration=.8, loop=True)
    #enemies[i].animate_z(enemy_z_position+3.0, duration=.7, loop=True)

def input(key):
    global enemies

    if key=="left mouse down":
        weapon.position=(0.75,-0.55)

        for enemy in enemies:
            if enemy.hovered:
                destroy(enemy)
    else:
        weapon.position=(0.8,-0.6)


app.run()