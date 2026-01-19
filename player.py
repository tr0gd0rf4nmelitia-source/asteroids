## import pygame and all the created classes/functions we made to 
## assist in drawing the player character.
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
    # initialize the default value of the player character
    def __init__(self, x, y):
        # pass the x, y, and constant player_radius values to the super class constructor of CircleShape
        super().__init__(x, y, PLAYER_RADIUS)
        # set initial rotational value to 0
        self.rotation = 0
        # set initial position vector of the character sprite to be equal to the initial x and y position.
        self.position = pygame.Vector2(x,y)
        self.shot_cooldown_timer = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # to change player color, could pass a variable color and replace the white string with the color value
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    # update player position when specific keys are pressed. 
    # must be done in individual if statements, otherwise when there is a 
    # simultaneous key press, instead of having the intended result of player move, 
    # the screen and function will only show the highest if pressed statement.
    def update(self, dt):
        self.shot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    # move the player sprite
    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation) 
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self):
        if self.shot_cooldown_timer > 0: 
            return
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(0, 0)
        shot.position = pygame.Vector2(self.position)
        ## shot.rotation = self.rotation
        shot.velocity = pygame.Vector2(0,1)
        rotated_vector = shot.velocity.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
        shot.velocity = rotated_with_speed_vector
        ## shot.position += shot.velocity
