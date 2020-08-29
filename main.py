def on_button_pressed_a():
    p1.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    p1.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

p1: game.LedSprite = None
p1 = game.create_sprite(2, 4)
p2 = game.create_sprite(randint(0, 4), 0)

def on_forever():
    p2.change(LedSpriteProperty.Y, 1)
    basic.pause(500)
    if p1.is_touching(p2):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    if p2.get(LedSpriteProperty.Y) == 4:
        p2.set(LedSpriteProperty.Y, 0)
        p2.set(LedSpriteProperty.X, randint(0, 4))
basic.forever(on_forever)
