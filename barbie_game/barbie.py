import pygame,sys
import random

#sounds
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 512)

#restart 

def restart(_score):
  restart_screen = pygame.display.set_mode((800, 500))
  pygame.font.init()
  restart_font = pygame.font.SysFont('Sans', 60, True, False)
  restart_message = "Press the space key to restart."
  restart_message_obj = restart_font.render(restart_message, True, (255,255,255))
  score_message = "Your score : " + str(_score)
  score_message_obj = restart_font.render(score_message, True, (255,255,0 ))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.init()
        sys.exit()
      if event.type == pygame.KEYDOWN and pygame.K_SPACE:
        return main()
      
    restart_screen.fill(((255 , 182, 193)))
    restart_screen.blit(restart_message_obj, (25,0))
    restart_screen.blit(score_message_obj, (25,100)) 
    pygame.display.update()
#main game function
def main():
  #initilize game
  pygame.init()
  screen_width = 800
  screen_height = 500
  screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("Barbie game")

  #background
  background = pygame.image.load("C:/Users/sunna/OneDrive/Documents/pygame/jump game/image/background.png")
  background = pygame.transform.scale(background, (screen_width, screen_height))

  #barbie
  barbie_width = 60
  barbie_height =60
  barbie = pygame.Rect((screen_width-barbie_width)/2, screen_height-barbie_height, barbie_width, barbie_height )
  barbie_img = pygame.image.load("C:/Users/sunna/OneDrive/Documents/pygame/jump game/image/barbie.png")
  barbie_img = pygame.transform.scale(barbie_img, (barbie_width,barbie_height))
  barbie_y_pos = 0



  #heart
  hearts = []
  heart_width =30
  heart_height = 30
  for i in range(20):  
    heart = pygame.Rect(random.randint(0,screen_width - 30), 0, heart_width, heart_height)
    hearts.append(heart)
  heart_img = pygame.image.load("C:/Users/sunna/OneDrive/Documents/pygame/jump game/image/heart.jpg") 
  heart_img = pygame.transform.scale(heart_img, (heart_width, heart_height))
  heart_y_pos = 0
  heart_speed = 0.3
   
  poop_width = 30
  poop_height = 30
  
  poop = pygame.Rect(random.randint(0,screen_width - 30), 0, poop_width, poop_height)
  poop_img = pygame.image.load("C:/Users/sunna/OneDrive/Documents/pygame/jump game/image/poop.jpg") 
  poop_img = pygame.transform.scale(poop_img, (poop_width, poop_height))
  poop_y_pos = 0
  poop_speed = 0.2

  monster_width = 20
  monster_height = 20
  monster = pygame.Rect(0, screen_height-monster_height,20, 20)
  monster_img = pygame.image.load("C:/Users/sunna/OneDrive/Documents/pygame/jump game/image/monster.jpg")
  monster_img =  pygame.transform.scale(monster_img, (monster_width, monster_height))
  monster_speed = 0.3

  #game speed
  clock = pygame.time.Clock()
  game_speed = 0.5

  # sounds
  jump_sound = pygame.mixer.Sound("C:/Users/sunna/OneDrive/Documents/pygame/jump game/sounds/jump.mp3")
  jump_sound.set_volume(0.1)
  heart_sound = pygame.mixer.Sound("C:/Users/sunna/OneDrive/Documents/pygame/jump game/sounds/heart.mp3")
  heart_sound.set_volume(0.5)

  #font
  font = pygame.font.SysFont('Sans', 30, True, False)
  
  #time 
  start_time = 0
  second =  0
  #score 
  score = 0

  #sound
  pygame.mixer.pre_init(22050, -16, 2, 512)
  pygame.init()
  pygame.mixer.quit()
  pygame.mixer.init(22050, -16, 2, 512)

  #background music
  bgmusic = pygame.mixer.music
  bgmusic.load("C:/Users/sunna/OneDrive/Documents/pygame/jump game/sounds/music.mp3")
  bgmusic.play(-1)
  bgmusic.set_volume(0.3)

  while True :
    dt = clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    keyInput = pygame.key.get_pressed()
    if keyInput[pygame.K_LEFT] and barbie.left >=0:
      barbie.left -= game_speed * dt
    if keyInput[pygame.K_RIGHT] and barbie.right <= screen_width:
      barbie.right += game_speed * dt
    
    #jump
    barbie.top += barbie_y_pos
    barbie_y_pos += 1
    
    if barbie.bottom >=  500:
      barbie_y_pos = 0
      if keyInput[pygame.K_SPACE]:
        barbie_y_pos = - 18
        jump_sound.play()
    
    #falling heart
    for heart in hearts:
      heart.y += random.uniform(0.1, 1) * dt
 
      if heart.bottom > screen_height:
        random_a =random.randint(0,screen_width - 30)
        heart.update(random_a, 0, heart_width, heart_height)
        # heart.x = random_a
        # heart.y = 0

    #collision with heart
      if barbie.colliderect(heart):
        heart_sound.play()
        hearts.remove(heart)
        score +=1
        heart= pygame.Rect(random.randint(0,screen_width - 30), 0, heart_width, heart_height)
        hearts.append(heart)
    #falling poop    
    poop.y += poop_speed * dt

    if poop.bottom > screen_height:
      random_b = random.randint(0,screen_width - 30)
      poop.x = random_b
      poop.y = 0
   # monster move and collision
    monster.right += monster_speed * dt
    if monster.right >= screen_width:
      monster.right = screen_width
      monster_speed *= -1
    elif monster.left <= 0:
      monster_left = 0
      monster_speed *= -1

    #collision with poop
    if barbie.colliderect(poop):
      restart(score)
    if barbie.colliderect(monster):
      restart(score)
    #score 
    score_message =font.render('SCORE: ' + str(score), True, (255 , 182, 193))

    screen.blit(background, (0,0))
    screen.blit(barbie_img, barbie)
    for heart in hearts:
      screen.blit(heart_img, heart)
    screen.blit(poop_img, poop)
    screen.blit(monster_img, monster)
    screen.blit(score_message, (0,0))
   
    pygame.display.update()

  
main()