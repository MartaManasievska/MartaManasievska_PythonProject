import pygame
import os
from project.base_development import BaseDevelopmentScene

class FemaleDevelopmentScene(BaseDevelopmentScene):
    def __init__(self, screen):
        super().__init__(screen)
        self.fade_in_done = False  

        self.current_outfit_path = os.path.join("character_images", "default_female.png")
        
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


        self.draw_character(self.current_outfit_path, position=(250, 120), size=(300, 550))

        buttons = [
            (os.path.join("buttons", "button_outfit_1.png"), os.path.join("character_images", "female_outfit_1.png")),
            (os.path.join("buttons", "button_outfit_2.png"), os.path.join("character_images", "female_outfit_2.png")),
            (os.path.join("buttons", "button_outfit_3.png"), os.path.join("character_images", "female_outfit_3.png")),
            (os.path.join("buttons", "button_outfit_4.png"), os.path.join("character_images", "female_outfit_4.png")),
            (os.path.join("buttons", "button_outfit_5.png"), os.path.join("character_images", "female_outfit_5.png")),
        ]
        
        start_x = self.screen.get_width() - 350
        start_y = 100
        button_spacing = 20
        button_size = (170, 90)

        selected_outfit = self.draw_image_buttons(buttons, start_x, start_y, button_spacing, button_size)
        if selected_outfit:
            print(f"Switching to outfit: {selected_outfit}")  
            self.current_outfit_path = selected_outfit

        button_width = 150
        button_height = 56

        back_button_x, back_button_y = 20, 20  
        continue_button_x = back_button_x + button_width + 20 

        mouse_x, mouse_y = pygame.mouse.get_pos()
        hover_back = back_button_x <= mouse_x <= back_button_x + button_width and back_button_y <= mouse_y <= back_button_y + button_height
        hover_continue = continue_button_x <= mouse_x <= continue_button_x + button_width and back_button_y <= mouse_y <= back_button_y + button_height

        if hover_back or hover_continue:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        self.draw_button(back_button_x, back_button_y, button_width, button_height, "Back", hover=hover_back)
        self.draw_button(continue_button_x, back_button_y, button_width, button_height, "Continue", hover=hover_continue)


        return hover_back, hover_continue
