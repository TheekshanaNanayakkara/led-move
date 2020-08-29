input.onButtonPressed(Button.A, function on_button_pressed_a() {
    p1.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    p1.change(LedSpriteProperty.X, 1)
})
let p1 : game.LedSprite = null
p1 = game.createSprite(2, 4)
let p2 = game.createSprite(randint(0, 4), 0)
basic.forever(function on_forever() {
    p2.change(LedSpriteProperty.Y, 1)
    basic.pause(500)
    if (p1.isTouching(p2)) {
        music.playTone(262, music.beat(BeatFraction.Whole))
    }
    
    if (p2.get(LedSpriteProperty.Y) == 4) {
        p2.set(LedSpriteProperty.Y, 0)
        p2.set(LedSpriteProperty.X, randint(0, 4))
    }
    
})
