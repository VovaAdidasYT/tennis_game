from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0  :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0  :
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

window_width = 700
window_height = 500
window = display.set_mode((window_width, window_height))
display.set_caption("ТЕННИС")
background = transform.scale(image.load("fon.jpg"), (window_width, window_height))
rocket1 = Player1("rocket.png", 10, 80, 20, 100, 4)
rocket2 = Player2("rocket.png", 670, 80, 20, 100, 4)
ball = GameSprite("ball.png", 200, 200, 50, 50, 50)

speed_x = 3
speed_y = 3

play = True
game = True
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))



while game:
    if play != False:
        window.blit(background,(0, 0))
        rocket1.update()
        rocket2.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
           speed_x *= -1
           speed_y *= 1
      
        if ball.rect.y > window_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            play = False
            window.blit(lose1, (200, 200))
            game = True

        if ball.rect.x >= window_width- 40:
            play = False
            window.blit(lose2, (200, 200))
            game = True


        rocket1.reset()
        rocket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)
    
    for e in event.get():
        if e.type == QUIT:
            game = False