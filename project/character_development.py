import pygame
import os
from project.base_development import BaseDevelopmentScene

class CharacterDevelopmentScene(BaseDevelopmentScene):
    def __init__(self, screen):
        super().__init__(screen)
        self.fade_in_done = False  

    def display_scene(self):
        if not self.fade_in_done:
            self.fade_in(lambda: self.render_scene(), duration=500)
            self.fade_in_done = True

        return self.render_scene()

    def render_scene(self):
        background_path = os.path.join("assets", "closet.png")
        background = pygame.image.load(background_path)
        background = pygame.transform.scale(background, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background, (0, 0))

        button_width = 150
        button_height = 56
        screen_width = self.screen.get_width()
        button_x_offset = 150
        button_y_position = self.screen.get_height() // 2 - button_height // 2


        male_x = screen_width // 2 - button_x_offset - button_width // 2
        female_x = screen_width // 2 + button_x_offset - button_width // 2

        mouse_x, mouse_y = pygame.mouse.get_pos()

        hover_male = male_x <= mouse_x <= male_x + button_width and button_y_position <= mouse_y <= button_y_position + button_height
        hover_female = female_x <= mouse_x <= female_x + button_width and button_y_position <= mouse_y <= button_y_position + button_height

        self.draw_button(male_x, button_y_position, button_width, button_height, "Male", hover=hover_male)
        self.draw_button(female_x, button_y_position, button_width, button_height, "Female", hover=hover_female)

        # Top-left corner positions for Back and Continue buttons
        back_button_x, back_button_y, back_button_size = 20, 20, 40
        hover_back = back_button_x <= mouse_x <= back_button_x + back_button_size and back_button_y <= mouse_y <= back_button_y + back_button_size

        hover_back = back_button_x <= mouse_x <= back_button_x + button_width and back_button_y <= mouse_y <= back_button_y + button_height
       
        if hover_male or hover_female or hover_back:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        self.draw_button(back_button_x, back_button_y, button_width, button_height, "Back", hover=hover_back)

        return hover_back,hover_male, hover_female
