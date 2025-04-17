import pygame


class BaseDevelopmentScene:
    def __init__(self, screen):
        self.screen = screen

    def fade_in(self, render_scene, duration=500):
        fade_surface = pygame.Surface(self.screen.get_size())
        fade_surface.fill((0, 0, 0))  

        steps = 50
        delay = duration // steps 

        for alpha in range(255, -1, -90):
            fade_surface.set_alpha(alpha)
            render_scene()  # Re-render the scene behind the fade effect
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(delay)

    def draw_back_button(self, x, y, size, hover=False):  
        BUTTON_COLOR = (241, 241, 241)
        BUTTON_HOVER_COLOR = (220, 220, 220)
        TEXT_COLOR = (0, 0, 0)
        color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
        pygame.draw.circle(self.screen, color, (x + size // 2, y + size // 2), size // 2)
        font = pygame.font.SysFont("Arial", 24, bold=True)
        label = font.render("←", True, TEXT_COLOR)
        label_rect = label.get_rect(center=(x + size // 2, y + size // 2))
        self.screen.blit(label, label_rect)

    def draw_button(self, x, y, width, height, text, hover=False):
        # Button Colors
        BUTTON_COLOR = (255, 255, 255)  # White
        HOVER_COLOR = (30, 41, 59)     # Dark Blue
        TEXT_COLOR = (13, 23, 42)      # Dark Text
        TEXT_HOVER_COLOR = (255, 255, 255)  # White Text
        SHADOW_COLOR = (166, 175, 195)  # Shadow color

        # Determine the button's color based on hover state
        button_color = HOVER_COLOR if hover else BUTTON_COLOR
        text_color = TEXT_HOVER_COLOR if hover else TEXT_COLOR

        # Draw shadow
        shadow_offset = 5
        pygame.draw.rect(
            self.screen, SHADOW_COLOR,
            (x + shadow_offset, y + shadow_offset, width, height), border_radius=20
        )

        # Draw button
        pygame.draw.rect(
            self.screen, button_color,
            (x, y, width, height), border_radius=20
        )

        # Render text
        font = pygame.font.SysFont("Arial", 24, bold=True)
        label = font.render(text, True, text_color)
        label_rect = label.get_rect(center=(x + width // 2, y + height // 2))
        self.screen.blit(label, label_rect)

    def draw_character(self, image_path, position=(250, 500), size=(300, 550)):
        try:
            character = pygame.image.load(image_path)
            character = pygame.transform.scale(character, size)
            character_x, character_y = position
            self.screen.blit(character, (character_x, character_y))
        except pygame.error as e:
            print(f"Error loading character image at {image_path}: {e}")

    def draw_image_buttons(self, buttons, start_x, start_y, button_spacing, button_size=(100, 50)):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        clicked_data = None
        cursor_set = False  

        for i, (image_path, associated_data) in enumerate(buttons):
            try:
                button_image = pygame.image.load(image_path)
                button_image = pygame.transform.scale(button_image, button_size)
            except pygame.error as e:
                print(f"Error loading image {image_path}: {e}") #exception handeling
                continue

            button_width, button_height = button_size
            button_x = start_x
            button_y = start_y + i * (button_height + button_spacing)

            self.screen.blit(button_image, (button_x, button_y))

            # Check if the mouse is hovering over this button
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                if not cursor_set:  # Update the cursor only once per frame
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    cursor_set = True
                if pygame.mouse.get_pressed()[0]:  # Check for mouse click
                    clicked_data = associated_data

        if not cursor_set:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        return clicked_data

    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = []

        for word in words:
            current_line.append(word)
            # Render current line and check its width
            line_width, _ = font.size(' '.join(current_line))
            if line_width > max_width:
                # If line is too long, add it to lines and start a new line
                current_line.pop()  # Remove the last word
                lines.append(' '.join(current_line))
                current_line = [word]  # Start new line with the current word

        # Add the last line
        if current_line:
            lines.append(' '.join(current_line))

        return lines
    
    def draw_wrapped_button(self, x, y, width, height, text, hover=False):

        # Button Colors
        BUTTON_COLOR = (255, 255, 255)  # White
        HOVER_COLOR = (30, 41, 59)     # Dark Blue
        TEXT_COLOR = (13, 23, 42)      # Dark Text
        TEXT_HOVER_COLOR = (255, 255, 255)  # White Text
        SHADOW_COLOR = (166, 175, 195)  # Shadow color

        button_color = HOVER_COLOR if hover else BUTTON_COLOR
        text_color = TEXT_HOVER_COLOR if hover else TEXT_COLOR

        # Draw button background and shadow
        shadow_offset = 5
        pygame.draw.rect(
            self.screen, SHADOW_COLOR,
            (x + shadow_offset, y + shadow_offset, width, height), border_radius=20
        )
        pygame.draw.rect(
            self.screen, button_color,
            (x, y, width, height), border_radius=20
        )

        # Wrap the text to fit inside the button
        font = pygame.font.SysFont("Arial", 20, bold=True)
        wrapped_text = self.wrap_text(text, font, width - 20)  

        # Render each line of text centered within the button
        total_text_height = len(wrapped_text) * 25  
        text_y = y + (height - total_text_height) // 2  # Center the text vertically
        for line in wrapped_text:
            line_surface = font.render(line, True, text_color)
            line_rect = line_surface.get_rect(center=(x + width // 2, text_y + 12))
            self.screen.blit(line_surface, line_rect)
            text_y += 25  # Move down for the next line

    def is_hovered(self, x, y, width, height):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return x <= mouse_x <= x + width and y <= mouse_y <= y + height

    def draw_text_with_background(self, text, font, x, y, text_color, bg_color, padding=10):
        # Render the text
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        
        # background rectangle with padding
        bg_rect = pygame.Rect(
            text_rect.left - padding,
            text_rect.top - padding,
            text_rect.width + 2 * padding,
            text_rect.height + 2 * padding,
        )
        
        # surface for the background with transparency
        bg_surface = pygame.Surface(bg_rect.size, pygame.SRCALPHA)  # Allow transparency
        bg_surface.fill(bg_color)  # Fill with the background color (RGBA)

        # Blit the background surface and then the text surface
        self.screen.blit(bg_surface, bg_rect.topleft)
        self.screen.blit(text_surface, text_rect)
