import pygame
import sys
from base_development import BaseDevelopmentScene

class CareerScene(BaseDevelopmentScene):
    def __init__(self, screen, decision_tree, backgrounds):
        super().__init__(screen)
        self.moral = 50
        self.performance = 50
        self.day = 1
        self.situations_completed = 0
        self.current_node_index = 0
        self.decision_tree = decision_tree
        self.backgrounds = backgrounds
            
        self.background = None
        self.update_background()  
        
        self.left_button_rect = None
        self.right_button_rect = None
        self.can_click = True  # Flag to prevent multiple rapid clicks

    def update_background(self):
        default_background = "assets/default_background.png"
        
        # Handle nested dictionaries (use current day to get background path)
        if isinstance(self.backgrounds, dict):
            background_image_path = self.backgrounds.get(self.day, default_background)
        else:
            background_image_path = default_background  # Fallback for incorrect structure

        try:
            self.background = pygame.image.load(background_image_path)
            self.background = pygame.transform.scale(self.background, self.screen.get_size())
        except pygame.error as e:
            print(f"Error loading background image: {e}. Using default background.")
            self.background = pygame.Surface(self.screen.get_size())
            self.background.fill((50, 50, 50))  

    def render_scene(self):
        self.screen.blit(self.background, (0, 0))

        # Display stats
        font = pygame.font.SysFont("Arial", 24, bold=True)
        self.draw_text_with_background(f"Moral: {self.moral}%", font, 20, 20, (0, 0, 0), (255, 255, 255, 150), 5)
        self.draw_text_with_background(f"Day: {self.day}", font, 20, 60, (0, 0, 0), (255, 255, 255, 150), 5)
        self.draw_text_with_background(f"Job Performance: {self.performance}%", font,
                                    self.screen.get_width() - 300, 20, (0, 0, 0), (255, 255, 255, 150), 5)

        # Access current scenario node
        current_day_scenarios = self.decision_tree.get(self.day, [])
        if self.current_node_index >= len(current_day_scenarios):
            self.switch_to_next_day()
            return

        current_node = current_day_scenarios[self.current_node_index]

        # Display the scenario text
        situation_font = pygame.font.SysFont("Arial", 28, bold=True)
        wrapped_text = self.wrap_text(current_node.text, situation_font, self.screen.get_width() - 100)
        text_y = self.screen.get_height() // 2 - 150
        for line in wrapped_text:
            self.draw_text_with_background(line, situation_font, 50, text_y, (255, 255, 255), (0, 0, 0, 128), 10)
            text_y += 40

        # Button dimensions and positions
        button_width, button_height = 300, 150
        button_y = self.screen.get_height() // 2 + 100  # Slightly below center
        left_button_x = self.screen.get_width() // 2 - button_width - 100
        right_button_x = self.screen.get_width() // 2 + 100

        mouse_pos = pygame.mouse.get_pos()
        left_button_rect = pygame.Rect(left_button_x, button_y, button_width, button_height)
        right_button_rect = pygame.Rect(right_button_x, button_y, button_width, button_height)

        hover_left = left_button_rect.collidepoint(mouse_pos)
        hover_right = right_button_rect.collidepoint(mouse_pos)

        # Draw buttons with hover effect
        self.draw_wrapped_button(left_button_x, button_y, button_width, button_height,
                                current_node.left.text if current_node.left else "No Option", hover=hover_left)
        self.draw_wrapped_button(right_button_x, button_y, button_width, button_height,
                                current_node.right.text if current_node.right else "No Option", hover=hover_right)

        # Set cursor based on hover state
        if hover_left or hover_right:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Event handling for button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                if hover_left and current_node.left:
                    self.handle_choice(current_node.left)
                elif hover_right and current_node.right:
                    self.handle_choice(current_node.right)



    def is_hovered_rect(self, rect):
        return rect.collidepoint(pygame.mouse.get_pos())

    def handle_choice(self, next_node):
        if next_node:
            self.moral += next_node.moral_effect
            self.performance += next_node.performance_effect
            print(next_node.outcome_text) 
            self.situations_completed += 1
            self.current_node_index += 1

            if self.moral <= 0:
                self.game_over("quit")
            elif self.performance <= 0:
                self.game_over("fired")

            # Switch to next day after 3 scenarios
            if self.situations_completed >= 3:
                self.switch_to_next_day()
        else:
            print("No further options available. Please choose a valid option.")

    def switch_to_next_day(self):
        print(f"Day {self.day} completed! Moving to Day {self.day + 1}.")
        self.day += 1
        self.situations_completed = 0
        self.current_node_index = 0
        if self.day > 5:  
            self.game_over("success")
        else:
            self.update_background()

    def game_over(self, reason):
        """Handle game-ending conditions."""
        if reason == "quit":
            print("You quit the job and fell into depression. Morale hit 0.")
        elif reason == "fired":
            print("You got fired! Job performance hit 0.")
        elif reason == "success":
            print("Congratulations! You successfully completed all 5 days.")
            print(f"Final Stats: Moral: {self.moral}% | Job Performance: {self.performance}%")
            self.display_final_output()

        pygame.quit()
        sys.exit()

    def display_final_output(self):
        self.screen.fill((0, 0, 0)) 
        font = pygame.font.SysFont("Arial", 48, bold=True)

        success_text = font.render("Congratulations! You completed the 5 days!", True, (255, 255, 255))
        moral_text = font.render(f"Final Moral: {self.moral}%", True, (255, 255, 255))
        performance_text = font.render(f"Final Job Performance: {self.performance}%", True, (255, 255, 255))

        success_rect = success_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 50))
        moral_rect = moral_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        performance_rect = performance_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50))

        self.screen.blit(success_text, success_rect)
        self.screen.blit(moral_text, moral_rect)
        self.screen.blit(performance_text, performance_rect)

        pygame.display.update() 

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
