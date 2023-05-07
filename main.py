# Import the Pygame library and the random module
import pygame
import pygame.surfarray as surfarray
import matplotlib.pyplot as plt
import random

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define some colors
colors = [(3, 23, 64), (5, 33, 89), (105, 158, 191), (196, 238, 242)]

# Define the size of the rectangles
rect_size = 20

# Define the number of rows and columns based on the screen size and rectangle size
num_rows = screen_height // rect_size
num_cols = screen_width // rect_size

# Draw the rectangles in a rectangular pattern using nested for loops
for row in range(num_rows):
    for col in range(num_cols):
        x = col * rect_size
        y = row * rect_size

        color = colors[(row + col) % len(colors)]

        pygame.draw.rect(screen, color, (x, y, rect_size, rect_size))

# Show the rectangles
pygame.display.flip()
pygame.surfarray.use_arraytype("numpy")
image = surfarray.array3d(screen)

# Display the image using Matplotlib
plt.imshow(image)
plt.axis("off")
plt.show()

# Quit Pygame
pygame.quit()
