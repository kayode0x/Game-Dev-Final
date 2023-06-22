import pygame
import random


class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(0, 255, 0)):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.width = width

    def update(self, progress):
        progress = min(100, max(0, progress))
        current_width = self.width * (progress / 100)
        self.image = pygame.Surface([current_width, self.rect.height])
        self.image.fill((0, 255, 0))


class Player:
    def __init__(self, car):
        self.car = car
        self.health = 100
        self.progress = 0

    def update(self, keys_pressed):
        self.car.update(keys_pressed)

        if keys_pressed[pygame.K_RIGHT]:  # Progress only when moving right
            # Assume max progress is 100
            self.progress = min(100, self.progress + 0.5)

    def decrease_health(self, amount):
        self.health = max(0, self.health - amount)
        
        
class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.width = width

    def update(self, health):
        health = min(100, max(0, health))
        current_width = self.width * (health / 100)
        self.image = pygame.Surface([current_width, self.rect.height])
        self.image.fill((255, 0, 0))


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('car.png')  # Load the car image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_UP]:  # Drive up
            self.rect.y -= 5
        if keys_pressed[pygame.K_DOWN]:  # Drive down
            self.rect.y += 5
        if keys_pressed[pygame.K_LEFT]:  # Drive left
            self.rect.x -= 5
        if keys_pressed[pygame.K_RIGHT]:  # Drive right
            self.rect.x += 5

        # Boundary detection
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        # self.image = pygame.image.load('ball.png')  # Load the ball image
        self.image = pygame.image.load('ball.png')  # Load the ball image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

        # Boundary detection and "bounce" back
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed = -self.speed


WIDTH, HEIGHT = 800, 600  # Set the dimensions as per your needs
FPS = 60  # Set frames per second as per your needs


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.sprites = pygame.sprite.Group()
        self.health_bar = HealthBar(10, 10, WIDTH - 20, 20)
        self.progress_bar = ProgressBar(
            10, HEIGHT - 30, WIDTH - 20, 20)  # Bottom of the screen
        self.sprites.add(self.health_bar)
        self.sprites.add(self.progress_bar)
        self.level = 1
        # Set font size for the game end message
        self.font = pygame.font.Font(None, 50)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            # Game over condition
            if self.player.health <= 0:
                self.running = False
            elif self.level > 3:
                self.running = False

            self.clock.tick(FPS)

        # Game over or winning message
        if self.player.health <= 0:
            end_text = "Game Over!"
        else:
            end_text = "You survived!"

        text_surf = self.font.render(end_text, True, (255, 255, 255))
        self.screen.blit(text_surf, ((WIDTH - text_surf.get_width()) //
                         2, (HEIGHT - text_surf.get_height()) // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

    def level_up(self):
        self.level += 1
        self.player.progress = 0
        print(f"Level Up! Current Level: {self.level}")

        # Increase the speed of balls
        for sprite in self.sprites:
            if isinstance(sprite, Ball):
                sprite.speed *= 1.5

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys_pressed = pygame.key.get_pressed()
        self.player.update(keys_pressed)

        for sprite in self.sprites:
            if isinstance(sprite, Ball):
                sprite.update()

        # Collision detection
        collided_balls = pygame.sprite.spritecollide(
            self.player.car, self.sprites, False)
        for ball in collided_balls:
            if isinstance(ball, Ball):
                self.player.decrease_health(1)  # Decrease health on collision
                print('Health:', self.player.health)

        self.health_bar.update(self.player.health)
        self.progress_bar.update(self.player.progress)  # Update progress bar

        # Level up if progress is 100 and level is less than 3
        if self.player.progress >= 100 and self.level < 3:
            self.level_up()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def add_sprite(self, sprite):
        self.sprites.add(sprite)

    def set_player(self, player):
        self.player = player
        self.sprites.add(player.car)

game = Game()

# Add the player
car = Car(100, 100)
player = Player(car)
game.set_player(player)

# Add some balls
for i in range(5):
    ball = Ball(random.randint(0, WIDTH), random.randint(
        0, HEIGHT), random.choice([-5, 5]))
    game.add_sprite(ball)

game.run()

pygame.quit()
