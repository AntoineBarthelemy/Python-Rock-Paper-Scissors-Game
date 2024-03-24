"""
Check README.md for details

Created on Thu Mar 21 19:57:50 2024
@author: theobarthelemy
"""

# Import modules and launch them 
import sys
import random
import pygame


pygame.init()

#   Declaration of global variables 
 # Constant
SCREEN_WIDTH, SCREEN_HEIGHT = (1000, 800) # Dynamic behavior for easiest calculations  
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

 # ≠Constant 
# Setup of my game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set the diplay's size or my game
screen.fill(CYAN) # Set the background color to cyan
pygame.display.set_caption("Rock, Paper, Scissors") # Set the windows'title 
clock = pygame.time.Clock() # Controlling the frame rate despite the computer capabilites

win_score = uscore = cscore = 0
score_text = f"Winning Score: {win_score} | Your Score: {uscore} | Computer's Score: {cscore}"
input_text = ''

font = pygame.font.Font('assets/fonts/Oswald-Regular.ttf', 45) # Controll the font of my header
instruction_font = font_input = pygame.font.Font(None, 30)

instruction_text1, instruction_text2, instruction_text3, text, score_surface, input_surface = instruction_font.render('Welcome to Rock, Paper, Scissors Game!', True, BLACK), instruction_font.render('Enter the winning score below and start playing.', True, BLACK), instruction_font.render('Press Enter to confirm your winning score.', True, BLACK), font.render('Rock, Paper, Scissors Game', True, BLACK, CYAN), instruction_font.render(score_text, True, BLACK), font_input.render(input_text, True, BLACK)

input_box = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 25, 300, 50)

textRect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5.5))# Object rect more effectiveness
instruction_rect1 = instruction_text1.get_rect(midtop=(SCREEN_WIDTH // 2, textRect.bottom + 30))
instruction_rect2 = instruction_text2.get_rect(midtop=(SCREEN_WIDTH // 2, instruction_rect1.bottom + 10))
instruction_rect3 = instruction_text3.get_rect(midtop=(SCREEN_WIDTH // 2, instruction_rect2.bottom + 10))
score_rect = score_surface.get_rect(midtop=(SCREEN_WIDTH // 2, instruction_rect3.bottom + 30))

screen.blits(((instruction_text1, instruction_rect1),(instruction_text2, instruction_rect2), (instruction_text3, instruction_rect3), (text, textRect), (score_surface, score_rect), (input_surface, input_box)))

input_active = True

# Logic of the code

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    if win_score == 0:
                        win_score_text = input_text.strip()
                        instruction_text5 = instruction_font.render('The Winning Score is ' + win_score_text, True, BLACK)
                        instruction_rect5 = instruction_text5.get_rect()
                        instruction_rect5.midtop = (screen.get_width() // 2, input_box.bottom + 10)
                        while True:
                            if win_score_text.isdigit():
                                win_score = int(win_score_text)
                                screen.fill(CYAN)
                                screen.blit(instruction_text1, instruction_rect1)
                                screen.blit(instruction_text2, instruction_rect2)
                                screen.blit(instruction_text3, instruction_rect3)
                                #erase the past Winning score in score_text and upload with the new one
                                screen.blit(instruction_text5, instruction_rect5)
                                instruction_text6 = instruction_font.render('Type your choice (Rock/Paper/Scissors) and press Enter to play.', True, BLACK)
                                instruction_rect6 = instruction_text6.get_rect()
                                instruction_rect6.midtop = (screen.get_width() // 2, input_box.top + 85)
                                screen.blit(instruction_text6, instruction_rect6)
                                #refresh the input box
                                #remove the disclaimer 1
                                pygame.display.update()
                                input_text = ''
                                break
                            else:
                                disclaimer_1 = instruction_font.render('Please enter a valid number', True, RED)
                                disclaimer_R1 = disclaimer_1.get_rect()
                                disclaimer_R1.midtop = (screen.get_width() // 2, instruction_rect5.bottom + 10)
                                #refresh the input box
                                screen.blit(disclaimer_1, disclaimer_R1)
                                input_text = ''
                                print("Please enter a valid number.")
                    else:
                        while uscore < win_score and cscore < win_score:
                            while True:
                                player_choice = input_text.strip().capitalize()
                                if player_choice not in ["Rock", "Paper", "Scissors"]:
                                    disclaimer_2 = instruction_font.render('Invalid choice. Please choose Rock, Paper, or Scissors', True, RED)
                                    disclaimer_R2 = disclaimer_2.get_rect()
                                    disclaimer_R2.midtop = (screen.get_width() // 2, instruction_rect5.bottom + 10)
                                    screen.blit(disclaimer_2, disclaimer_R2)
                                    input_text = ''
                                    pygame.display.update()
                                    #refresh the input box
                                    continue
                                    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
                                else:
                                    #refresh the input box
                                    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                                    ComputerP = instruction_font.render('Computer chose: ' + computer_choice, True, PURPLE)
                                    ComputerRP = ComputerP.get_rect()
                                    ComputerRP.midtop = (screen.get_width() // 2, instruction_rect5.bottom + 20)  # Use instruction_rect5 instead of disclaimer_R2
                                    screen.blit(ComputerP, ComputerRP)
                                    pygame.display.update()
                                    print("Computer chose:", computer_choice)
                                    if player_choice == computer_choice:
                                        TieP = instruction_font.render("How Unfortunate, no one wins this round!", True, PURPLE)
                                        TieRP = TieP.get_rect()
                                        TieRP.midtop = (screen.get_width() // 2, input_box.bottom + 80)  
                                        screen.blit(TieP, TieRP)
                                        input_text = ''
                                        #refresh the input box
                                        pygame.display.update()
                                        print("How Unfortunate, no one wins this round!")
                                    elif (player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Scissors" and computer_choice == "Paper") or (player_choice == "Paper" and computer_choice == "Rock"):
                                        uscore += 1
                                        #erase the past uscore in score_text and upload with the new one
                                        YW = instruction_font.render('You win this round ! Your Score is' + str(uscore) + "The Computer's Score:" + str(cscore), True, BLACK)
                                        YWR = YW.get_rect()
                                        YWR.midtop = (screen.get_width() // 2, input_box.bottom + 140)
                                        screen.blit(YW, YWR)
                                        input_text = ''
                                        #refresh the input box
                                        pygame.display.update()
                                        print("You win this round!")
                                    else:
                                        cscore += 1
                                        #erase the past cscore in score_text and upload with the new one
                                        CW = instruction_font.render('You lost this round... Your Score is' + str(uscore) + " And The Computer's Score:" + str(cscore), True, BLACK)
                                        CWR = CW.get_rect()
                                        CWR.midtop = (screen.get_width() // 2, input_box.bottom + 140)
                                        screen.blit(CW, CWR)
                                        input_text = ''
                                        #refresh the input box
                                        pygame.display.update()
                                        print("Computer wins this round!")
                            if uscore > cscore:
                                 WPA = instruction_font.render("You won ! Wanna Play Again ?", True, BLACK)
                                 WPAR = WPA.get_rect()
                                 WPAR.midtop = (screen.get_width() // 2, input_box.bottom + 140)
                                 screen.blit(WPA, WPAR)
                                 pygame.display.update()
                                 print("You are the Winner ! Wanna Play Again?")
                            elif cscore > uscore:
                                 CPA = instruction_font.render("The Computer won ! Wanna Play Again and get your revenge ?", True, BLACK)
                                 CPAR = CPA.get_rect()
                                 CPAR.midtop = (screen.get_width() // 2, input_box.bottom + 140)
                                 screen.blit(CPA, CPAR)
                                 pygame.display.update()
                                 print ("You lost... Wanna play again and get revenge on this evil computer and Play Again?")
                            while True:
                                 input_text = ''
                                 #refresh the input box
                                 again_choice = input_text.strip().capitalize()
                                 if again_choice in ["yes", "no"]:
                                    if again_choice == "yes":
                                        break
                                    elif again_choice == "no":
                                        break
                                 else:
                                    continue
                            if again_choice == "no":
                                 break
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
    input_box_color = BLACK if input_active else RED
    pygame.draw.rect(screen, input_box_color, input_box, 2)
   
    font_input = pygame.font.Font(None, 32)
    input_surface = font_input.render(input_text, True, BLACK)
    screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))
   
    score_text = f"Winning Score: {win_score} | Your Score: {uscore} | Computer's Score: {cscore}"
    score_surface = instruction_font.render(score_text, True, BLACK)
    score_rect = score_surface.get_rect(midtop=(screen.get_width() // 2, instruction_rect3.bottom + 30))
    screen.blit(score_surface, score_rect)
   
    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)