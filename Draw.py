# Author: Amy Salley
# Description:  Creates three random colors and assigns each color to the mouse left
# button, wheel and right button. Draws on a screen with those colors.

import pygame
import random


def random_colors():
    """Define the random colors."""
    color_1 = (random.randrange(0, 255), random.randrange(0,255), random.randrange(0, 255))
    color_2 = (random.randrange(0, 255), random.randrange(0,255), random.randrange(0, 255))
    color_3 = (random.randrange(0, 255), random.randrange(0,255), random.randrange(0, 255))
    return color_1, color_2, color_3


def clear_screen():
    """Erases the screen"""
    black = (0, 0, 0)
    screen.fill(black)
    pygame.display.update()


def instructions():
    """Displays instructions on the screen until screen is clicked. """
    display_instructions = True

    white = (255, 255, 255)
    blue = (66, 135, 245)
    medium_blue = (107, 153, 227)
    light_blue = (179, 203, 242)
    green = (99, 214, 127)

    font = pygame.font.Font("Aller_Lt.ttf", 28)
    font_large = pygame.font.Font("Aller_Lt.ttf", 36)

    title = font_large.render("Welcome to Drag to Draw!", True, green)
    text_1 = font.render("Click a mouse button and slowly drag across the screen to draw", True, blue)
    text_2 = font.render("Click 'n' to select new colors", True, medium_blue)
    text_3 = font.render("Click 'c' to clear the screen", True, light_blue)
    text_4 = font.render("Click anywhere to start", True, white)

    screen.blit(title, [30, 100])
    screen.blit(text_1, [30, 160])
    screen.blit(text_2, [30, 220])
    screen.blit(text_3, [30, 280])
    screen.blit(text_4, [30, 340])
    pygame.display.update()

    while display_instructions:
        for click in pygame.event.get():
            if click.type == pygame.MOUSEBUTTONDOWN:
                clear_screen()
                pygame.display.update()
                display_instructions = False


# Define the size of the screen and the radius of the circles to draw with the "pen"
size = (900, 700)
radius = 10

pygame.init()
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Click and drag to draw")

# Display the instructions
instructions()

color_1, color_2, color_3 = random_colors()

keep_going = True
mouse_pressed = False
key_pressed = False

while keep_going:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            keep_going = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

        if event.type == pygame.KEYDOWN:
            key_pressed = True

    if mouse_pressed:

        # Find the position of the mouse cursor.
        position = pygame.mouse.get_pos()

        # If the left mouse button is pressed, assign the first random color.
        if pygame.mouse.get_pressed()[0]:
            button_color = color_1

        # If the mouse wheel is pressed, assign the second random color.
        elif pygame.mouse.get_pressed()[1]:
            button_color = color_2

        # If the mouse right button is pressed, assign the third random color.
        elif pygame.mouse.get_pressed()[2]:
            button_color = color_3

        # Draw circle on the screen with the corresponding color and mouse position.
        pygame.draw.circle(screen, button_color, position, radius)

    pygame.display.update()

    if pygame.key.get_pressed()[pygame.K_n]:
        color_1, color_2, color_3 = random_colors()

    elif pygame.key.get_pressed()[pygame.K_c]:
        clear_screen()
        pygame.display.update()

pygame.quit()
