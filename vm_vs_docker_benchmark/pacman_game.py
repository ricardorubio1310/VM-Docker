import os
os.environ["SDL_VIDEODRIVER"] = "dummy"  # Forzar modo sin pantalla real

import pygame
import sys
import psutil
import time

pygame.init()

# Performance logging
start_time = time.time()
process = psutil.Process()
cpu_start = psutil.cpu_percent(interval=None)
mem_info_start = process.memory_info().rss / 1024 / 1024  # in MB

# Screen setup
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Pacman")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Pacman setup
x, y = WIDTH // 2, HEIGHT // 2
radius = 20
speed = 5
clock = pygame.time.Clock()

running = True
frame_count = 0
while running and frame_count < 300:  # Run for 10 seconds at 30 FPS
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= speed
    if keys[pygame.K_RIGHT]: x += speed
    if keys[pygame.K_UP]: y -= speed
    if keys[pygame.K_DOWN]: y += speed

    pygame.draw.circle(screen, YELLOW, (x, y), radius)
    pygame.display.flip()
    clock.tick(30)
    frame_count += 1

# End performance logging
end_time = time.time()
cpu_end = psutil.cpu_percent(interval=None)
mem_info_end = process.memory_info().rss / 1024 / 1024

print("\n--- Performance Report ---")
print(f"Execution Time: {end_time - start_time:.2f} seconds")
print(f"Start Memory Usage: {mem_info_start:.2f} MB")
print(f"End Memory Usage: {mem_info_end:.2f} MB")
print(f"CPU Usage: {cpu_end:.2f}%")

pygame.quit()
sys.exit()
