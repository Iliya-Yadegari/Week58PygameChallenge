import random

HEIGHT = 450
WIDTH = 800

robot_obj = Actor('robot_win',(250,250))
gem_obj = Actor('gemgreen',(300,400))

robot_obj.score_count = 0

bg = 'space_bg'

pause_switch = False

def draw():
    global pause_switch

    screen.blit(bg,(0,0))
    robot_obj.draw()
    gem_obj.draw()


    screen.draw.text(f'score: {robot_obj.score_count}',(20,400),color = (71,255,14),fontsize = 50)

    if pause_switch == True:
        screen.fill((0,0,0))
        screen.draw.text('Pause',(300,200),color = (71,255,14),fontsize = 100)

def update():
    mov()
    score()

    repeat_fun()

def repeat_fun():
    if robot_obj.right < 0:
        robot_obj.left = WIDTH
    if robot_obj.bottom < 0:
        robot_obj.top = HEIGHT
    if robot_obj.left > WIDTH:
        robot_obj.right = 0
    if robot_obj.top > HEIGHT:
        robot_obj.bottom = 0

def score():
    if robot_obj.colliderect(gem_obj):
        #robot_obj.image = 'robot_win'
        clock.schedule_unique(reset_robot_obj,1.0)
        robot_obj.score_count += 1
        random_x = random.randint(30,770)
        random_y = random.randint(30,420)
        gem_obj.x = random_x
        gem_obj.y = random_y

        #gem_obj.pos = (random_x,random_y)

def mov():
    if keyboard.up:
        robot_obj.top -= 4
        robot_obj.image = 'robot_up'

    if keyboard.down:
        robot_obj.bottom += 4
        robot_obj.image = 'robot_down'

    if keyboard.left:
        robot_obj.left -= 4
        robot_obj.image = 'robot_left'

    if keyboard.right:
        robot_obj.right += 4
        robot_obj.image = 'robot_right'

def reset_robot_obj():
    robot_obj.image = 'robot_win'

def on_key_down(key):
    global pause_switch

    if key == key.ESCAPE and pause_switch == False:
        pause_switch = True
    elif key == key.ESCAPE and pause_switch == True:
        pause_switch = False
