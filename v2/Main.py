import pygame
import player as player
import lazer as lazer
import random
import asteroid as asteroid

#---importing key commands---
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    USEREVENT,
    QUIT,
    K_SPACE,
    K_1,
    K_2,
    K_3
)
#---starting pygame---
pygame.init()

#-----------------------------------------------------------------DEFINING VARIABLES AND SCREEN-----------------------------------------------------------------

#---get width and height and set for diff aspect ratios---
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode([width, height])

#---Setting the background and icon on the game---
pygame.display.set_caption("Rocket Racer")
space = pygame.image.load('Space.gif').convert()
rocket = pygame.image.load('Player.gif').convert()
pygame.display.set_icon(rocket)

#---creating a timer---
timer = pygame.time.Clock()
countdown = 10
count_up = 0
text = '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
letters = pygame.font.SysFont('Impact',  40)

#---This is the text for the rounds---
round_text = 'Round: 1'.rjust(3)
font = pygame.font.SysFont('Impact',  40)
#---This is the text on the title screen---a

menu_text = 'Press Space for New Game'.rjust(3)
menu_font = pygame.font.SysFont('Impact',  40)
diff_text = 'Press 1, 2, or 3 for difficulty'.rjust(3)
curr_text = 'Current Difficulty: Medium'.rjust(3)
menu_font = pygame.font.SysFont('Impact',  40)
difficulty = 500

#---this is for creating new asteroids in the future---
new_asteroid = pygame.USEREVENT + 1
pygame.time.set_timer(new_asteroid, 250)

#---creating the player and adding sprites to groups to allow multiple objects to coexist---
player = player.Player()
asteroids = pygame.sprite.Group()
sprites = pygame.sprite.Group()
sprites.add(player)

#---creating the lazers---
new_lazer = pygame.K_SPACE
lazers = pygame.sprite.Group()

#---storing scores of players as seconds alive---
scores = []

#-----------------------------------------------------------------FUNCTIONS-----------------------------------------------------------------
#---game running condition---
running = True 
round_count = 1
max_vel = 2

leader_font = pygame.font.SysFont('Impact',  70)
score_font = pygame.font.SysFont('Impact',  40)
placement = 100
#---leaderboard screen---

def show_leaderboard(rank, player_score):
    show = True

    leaderboard_text = ('Leaderboard').rjust(3)
    player_text = str(player_score)
    rank5 = ("5th: " + str(rank[4])).rjust(3)
    rank4 = ("4th: " + str(rank[3])).rjust(3)
    rank3 = ("3rd: " + str(rank[2])).rjust(3)
    rank2 = ("2nd: " + str(rank[1])).rjust(3)
    rank1 = ("1st: " + str(rank[0])).rjust(3)
    player_show = (str("Your score: " + player_text)).rjust(3)
    
    global space
    global score_font
    global placement

    screen.blit(space, (0, 0))
    screen.blit(leader_font.render(player_show, True, (255, 255, 255)), (width/2 - 170, 100))
    pygame.time.delay(500)
    pygame.display.update()
    screen.blit(leader_font.render(leaderboard_text, True, (255, 255, 255)), (width/2 - 170, 400))
    pygame.time.delay(500)
    pygame.display.update()
    screen.blit(score_font.render(rank1, True, (255, 255, 255)), (width/2 - 70, 500))
    pygame.time.delay(500)
    pygame.display.update()
    screen.blit(score_font.render(rank2, True, (255, 255, 255)), (width/2 - 70, 550))
    pygame.time.delay(500)
    pygame.display.update()
    screen.blit(score_font.render(rank3, True, (255, 255, 255)), (width/2 - 70, 600))
    pygame.time.delay(500)
    pygame.display.update()
    screen.blit(score_font.render(rank4, True, (255, 255, 255)), (width/2 - 70, 650))
    pygame.time.delay(500)
    pygame.display.update()
    screen.blit(score_font.render(rank5, True, (255, 255, 255)), (width/2 - 70, 700))
    pygame.time.delay(500)
    pygame.display.update()
        
    while show == True:
        for event in pygame.event.get():

            #---this will end the game---
            if event.type == pygame.QUIT:
                show = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    show = False
        
    
       

#---edits the leaderboard---
def leaderboard(count_up):
        print("Your score: ", count_up)
        ranks = []
        conv_rank = []
        final_rank = []
        with open('leaderboard.txt', 'r') as reader:
            ranks = reader.readlines()
        for i in ranks:
            conv_rank.append(int(i.strip()))
        for i in conv_rank:
            if (i < int(count_up)):
                conv_rank.pop()
                conv_rank.append(int(count_up))
        conv_rank.sort()
        conv_rank.reverse()
        print(conv_rank)
        with open('leaderboard.txt', 'w') as outfile:
            for i in conv_rank:
                outfile.write(str(i))  
                outfile.write("\n")
        show_leaderboard(conv_rank, count_up)

#---loop that runs for the game to be able to run---
def start(min, max):
    global running
    global space
    global player
    global text
    global countdown
    global sprites
    global round_text
    global count_up
    global round_count
    global max_vel
    global timer


    while (running == True):
        #---adds the background and user to the screen---
        screen.blit(space, (0, 0))
        screen.blit(letters.render(text, True, (255, 255, 255)), (32, 48))
        screen.blit(font.render(round_text, True, (255, 255, 255)), (width/2, 48))

        for event in pygame.event.get():

            #---this will end the game---
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == new_lazer:
                    pew = lazer.lazer()
                    pew.rect = pew.surf.get_rect(center = (player.rect.left + 40, player.rect.top))
                    lazers.add(pew)
                    sprites.add(pew)

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            #---countdown---
            if event.type == pygame.USEREVENT:
                temp = countdown
                countdown -= 1
                text = (str(countdown).rjust(3))
                count_up += 1
                #---every ten seconds, the asteroidsas speed up---
                if countdown == 0:
                    round_count = round_count + 1
                    temp = str(round_count)
                    round_text = (str('Round: '+ temp).rjust(3))
                    min = min * 1.25
                    max = max * 1.5
                    countdown = 10
                    
            #---Create the new asteroid peroidically---
            elif event.type == new_asteroid:
                new_enemy = asteroid.asteroid()
                new_enemy.speed = random.randint(int(min), int(max))
                asteroids.add(new_enemy)
                sprites.add(new_enemy)


        #---checks which key is pressed and performs a task---
        keys = pygame.key.get_pressed()
        player.movePlayer(keys)

        #---Runs and adds objects to the screen---
        for things in sprites:
            screen.blit(things.surf, things.rect)
        
        for lz in lazers:
            screen.blit(lz.surf, lz.rect)

        #---when a player and asteroids collide the game ends--- 
        if pygame.sprite.spritecollideany(player, asteroids):
            player.kill()
            running = False

        for l in lazers: 
            if pygame.sprite.spritecollideany(l, asteroids):
                for a in asteroids:
                    if pygame.sprite.spritecollideany(a, lazers):
                        l.kill()
                        a.kill()

        #---this makes the asteroids move---
        asteroids.update()
        lazers.update()

        #---updates the screen---
        pygame.display.flip()

    leaderboard(count_up)

#---title screen---
def new_game():
    min = 1
    max = 3
    while True:
        
        global menu_text
        global menu_font
        global diff_text
        global curr_text
        global difficultdy
        
        screen.blit(space, (0, 0))
        screen.blit(font.render(menu_text, True, (255, 255, 255)), (width/2 - 200, height/2 - 300))
        screen.blit(font.render(diff_text, True, (255, 255, 255)), (width/2 - 200, height/2 - 100))
        screen.blit(font.render(curr_text, True, (255, 255, 255)), (width/2 - 200, height/2 + 100))

        for event in pygame.event.get():

            #---this will end the game---
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
    
                #---begins a game if you press space---
                if event.key == K_SPACE:
                    start(min, max)
                    return False 

                #---Setting different difficulties for tick rates---
                if event.key == K_1:
                    min = 1
                    max = 2
                    curr_text = 'Current Difficulty: Easy'.rjust(3)
                if event.key == K_2:
                    min = 1
                    max = 3
                    curr_text = 'Current Difficulty: Medium'.rjust(3)
                if event.key == K_3:
                    min = 1
                    max = 5
                    curr_text = 'Current Difficulty: Hard'.rjust(3)
        
        pygame.display.flip()


#-----------------------------------------------------------------RUN STATEMENTS-----------------------------------------------------------------

#---this begins the program---

new_game()



#-----------------------------------------------------------------WORKS CITED-----------------------------------------------------------------
''' Title: PyGame: A Primer on Game Programming in Python
Author: Jon Fincher
Date: 2016
Code Version: 1.0
Availability: https://realpython.com/pygame-a-primer/#:~:text=pygame%20is%20a%20Python%20wrapper,for%20the%20stalled%20PySDL%20project.
'''