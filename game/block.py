import pygame
import random


class Block:
    def __init__(self, x, y, width, height, color, speed=0):
        self.x = float(x)
        self.y = float(y)
        self.width = float(width)
        self.height = float(height)
        self.color = color
        self.speed = speed
        self.direction = 1

    @property
    def rect(self):
        return pygame.Rect(
            int(self.x),
            int(self.y),
            int(self.width),
            int(self.height)
        )

    def update(self, screen_width):
        if self.speed == 0:
            return

        self.x += self.speed * self.direction

        if self.x <= 20:
            self.x = 20
            self.direction = 1

        elif self.x + self.width >= screen_width - 20:
            self.x = screen_width - 20 - self.width
            self.direction = -1

    def render(self, surface):
        draw_rect = self.rect

        pygame.draw.rect(
            surface,
            self.color,
            draw_rect,
            border_radius=4
        )

        pygame.draw.rect(
            surface,
            (245, 245, 250),
            draw_rect,
            width=2,
            border_radius=4
        )


class Debris:
    def __init__(self, x, y, width, height, color, vx, vy):
        self.x = float(x)
        self.y = float(y)

        self.width = float(width)
        self.height = float(height)

        self.color = color

        self.vx = vx
        self.vy = vy

        self.angle = 0.0
        self.rotation_speed = random.uniform(-8.0, 8.0)

        self.life = 90

    def update(self):
        self.x += self.vx
        self.y += self.vy

        self.vy += 0.35

        self.angle += self.rotation_speed

        self.life -= 1

    def render(self, surface):
        image = pygame.Surface(
            (
                max(1, int(self.width)),
                max(1, int(self.height))
            ),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            image,
            self.color,
            (
                0,
                0,
                int(self.width),
                int(self.height)
            )
        )

        rotated = pygame.transform.rotate(
            image,
            self.angle
        )

        surface.blit(
            rotated,
            (
                int(self.x - rotated.get_width() / 2),
                int(self.y - rotated.get_height() / 2)
            )
        )