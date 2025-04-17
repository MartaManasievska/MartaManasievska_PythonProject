import pygame
import os
from project.base_development import BaseDevelopmentScene

class CareerChoice(BaseDevelopmentScene):
    def __init__(self, screen):
        super().__init__(screen)
        self.fade_in_done = False  # Flag to track fade-in completion

    def display_scene(self):
        # Perform fade-in only once
        if not self.fade_in_done:
            self.fade_in(lambda: self.render_scene(), duration=500)
            self.fade_in_done = True

        return self.render_scene()

    def render_scene(self):
        background_path = os.path.join("assets", "career_choice_background.png")
        try:
            background = pygame.image.load(background_path)
            background = pygame.transform.scale(background, (self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(background, (0, 0))
        except pygame.error as e:
            print(f"Error loading background image: {e}")

        button_width = 150
        button_height = 50

        back_button_x, back_button_y = 20, 20

        mouse_x, mouse_y = pygame.mouse.get_pos()

        hover_back = (
            back_button_x <= mouse_x <= back_button_x + button_width
            and back_button_y <= mouse_y <= back_button_y + button_height
        )

        self.draw_button(back_button_x, back_button_y, button_width, button_height, "Back", hover_back)

        # Detect Back button click
        if hover_back and pygame.mouse.get_pressed()[0]:  # Left mouse button
            return "back"
        button_width = 250
        button_height = 50
        spacing_x = 50
        spacing_y = 30

        # Calculate grid position
        grid_width = (2 * button_width) + spacing_x
        grid_height = (3 * button_height) + (2 * spacing_y)
        start_x = (self.screen.get_width() - grid_width) // 2
        start_y = (self.screen.get_height() - grid_height) // 2

        button_labels = ["Software Engineer", "Lawyer", "Doctor", "Youtuber", "Actor", "Swimmer"]

        clicked_button = None

        # Render career buttons
        for i, label in enumerate(button_labels):
            row = i // 2
            col = i % 2
            x = start_x + col * (button_width + spacing_x)
            y = start_y + row * (button_height + spacing_y)

            hover = x <= mouse_x <= x + button_width and y <= mouse_y <= y + button_height

            self.draw_button(x, y, button_width, button_height, label, hover)

            if hover and pygame.mouse.get_pressed()[0]:
                clicked_button = label

        return clicked_button
