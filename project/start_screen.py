import pygame
import os

button_width = 200
button_height = 56

BUTTON_COLOR = (92, 64, 51)  # Dark Brown
TEXT_COLOR = (255, 255, 255)  # White
SHADOW_COLOR = (49, 28, 20)  # Shadow
LIGHT_SHADOW = (123, 50, 11)  # Bottom shadow
BUTTON_HOVER_COLOR = (139, 69, 19)  # Lighter Brown for hover

def draw_button(screen, x, y, width, height, text, hover=False):  
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR

    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=8)
    pygame.draw.rect(screen, SHADOW_COLOR, (x + 2, y - 1, width, height), border_radius=8)  # Shadow effect
    pygame.draw.rect(screen, LIGHT_SHADOW, (x - 2, y + 3, width, height), border_radius=8)  # Bottom shadow effect

    # Set up the font and render the text
    font = pygame.font.SysFont("Space Grotesk", 18, bold=True)
    label = font.render(text, True, TEXT_COLOR)
    label_rect = label.get_rect(center=(x + width // 2, y + height // 2))

    # Blit (draw) the text centered on the button
    screen.blit(label, label_rect)

def start_display(screen):
    image_path = os.path.join("assets", "background_for_startScreen.png") 
    background_image = pygame.image.load(image_path)
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    screen.blit(background_image, (0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    start_button_x, start_button_y = 500, 250
    exit_button_x, exit_button_y = 500, 350

    hover_start = start_button_x <= mouse_x <= start_button_x + button_width and start_button_y <= mouse_y <= start_button_y + button_height
    hover_exit = exit_button_x <= mouse_x <= exit_button_x + button_width and exit_button_y <= mouse_y <= exit_button_y + button_height

    if hover_start or hover_exit:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  

    draw_button(screen, start_button_x, start_button_y, button_width, button_height, "Start New Game", hover=hover_start)
    draw_button(screen, exit_button_x, exit_button_y, button_width, button_height, "Exit Game", hover=hover_exit)

    return hover_start, hover_exit
    