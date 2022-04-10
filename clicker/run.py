from ursina import * 
import random

app = Ursina()

window.borderless = False
window.color = color._20

def walk():
    go_adv.enabled = False
    invoke(find_egg, delay=random.randint(3,5))    

go_adv = Button(text="GOGOGO", scale=0.3)
go_adv.on_click = walk 

egg_life = random.randint(100,101)
egg_life_text = Text(text=str(egg_life), y=0.35, scale=2)
egg_life_text.text = ""    

def find_egg():
    global egg_life, egg_life_text
    egg_life_text.text = str(egg_life)

    egg = Button(text="hit me!", scale=random.randint(2,5)*0.1, icon="./assets/egg.png")
    egg.on_click = hit

def hit():
    global egg_life, egg_life_text
    egg_life -= 1
    egg_life_text.text = str(egg_life)

    if egg_life==0:
        reward()

def reward():
    monster_reward = Button(scale=1, icon="./assets/monster1.png")

app.run()