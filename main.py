import pygame
import sys
from start_screen import start_display
from character_development import CharacterDevelopmentScene
from male_development import MaleDevelopmentScene
from female_development import FemaleDevelopmentScene
from career_choice import CareerChoice
from career_decision_tree import (
    software_eng_tree, lawyer_tree, doctor_tree,
    youtuber_tree, actor_tree, swimmer_tree
)
from career_scene import CareerScene

pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Life Simulation Game")

backgrounds = {
    "Software Engineer": {
        1: "assets/software_day1.png",
        2: "assets/software_day2.png",
        3: "assets/software_day3.png",
        4: "assets/software_day4.png",
        5: "assets/software_day5.png"
    },
    "Lawyer": {
        1: "assets/lawyer_day1.png",
        2: "assets/lawyer_day2.png",
        3: "assets/lawyer_day3.png",
        4: "assets/lawyer_day4.png",
        5: "assets/lawyer_day5.png"
    },
    "Doctor": {
        1: "assets/doctor_day1.png",
        2: "assets/doctor_day2.png",
        3: "assets/doctor_day3.png",
        4: "assets/doctor_day4.png",
        5: "assets/doctor_day5.png"
    },
    "Youtuber": {
        1: "assets/youtuber_day1.png",
        2: "assets/youtuber_day2.png",
        3: "assets/youtuber_day3.png",
        4: "assets/youtuber_day4.png",
        5: "assets/youtuber_day5.png"
    },
    "Actor": {
        1: "assets/actor_day1.png",
        2: "assets/actor_day2.png",
        3: "assets/actor_day3.png",
        4: "assets/actor_day4.png",
        5: "assets/actor_day5.png"
    },
    "Swimmer": {
        1: "assets/swimmer_day1.png",
        2: "assets/swimmer_day2.png",
        3: "assets/swimmer_day3.png",
        4: "assets/swimmer_day4.png",
        5: "assets/swimmer_day5.png"
    }
}

# Scenarios dictionary for all careers
scenarios_by_profession = {
    "Software Engineer": software_eng_tree,
    "Lawyer": lawyer_tree,
    "Doctor": doctor_tree,
    "Youtuber": youtuber_tree,
    "Actor": actor_tree,
    "Swimmer": swimmer_tree
}

character_scene = CharacterDevelopmentScene(screen)
male_scene = MaleDevelopmentScene(screen)
female_scene = FemaleDevelopmentScene(screen)
career_choice_scene = CareerChoice(screen)
career_scene = None  # CareerScene will be created dynamically based on the selected career

running = True
scene = "start"  # Current scene identifier

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if scene == "start":
            hover_start, hover_exit = start_display(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_start:  
                    scene = "selection"
                elif hover_exit: 
                    running = False

        # Character Selection Screen
        elif scene == "selection":
            hover_back, hover_male, hover_female = character_scene.display_scene()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_back:  
                    scene = "start"
                    character_scene.fade_in_done = False
                elif hover_male:  
                    scene = "male"
                    character_scene.fade_in_done = False
                elif hover_female: 
                    scene = "female"
                    character_scene.fade_in_done = False

        # Male Character 
        elif scene == "male":
            hover_back, hover_continue = male_scene.display_scene()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_back:
                    scene = "selection"
                    male_scene.fade_in_done = False
                elif hover_continue:
                    scene = "career_choice"
                    career_choice_scene.fade_in_done = False

        # Female Character 
        elif scene == "female":
            hover_back, hover_continue = female_scene.display_scene()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_back:
                    scene = "selection"
                    female_scene.fade_in_done = False
                elif hover_continue:
                    scene = "career_choice"
                    career_choice_scene.fade_in_done = False

        # Career Choice Screen
        elif scene == "career_choice":
            selected_career = career_choice_scene.display_scene()  # Display career choices
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_career in scenarios_by_profession:
                    career_scene = CareerScene(
                        screen, scenarios_by_profession[selected_career], backgrounds[selected_career]
                    )
                    scene = "career"

        # Career Scene
        elif scene == "career":
            career_scene.render_scene()
            current_day_scenarios = career_scene.decision_tree.get(career_scene.day, [])

            # Check if we've reached the end of the day's scenarios
            if career_scene.current_node_index >= len(current_day_scenarios):
                career_scene.day += 1
                career_scene.current_node_index = 0
                if career_scene.day > 5:
                    print("Game Over - All days completed")
                    running = False 
                else:
                    career_scene.update_background()
    pygame.display.update()

pygame.quit()
sys.exit()
