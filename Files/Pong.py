
#==========To run, click the link below================#

########################################################
#http://www.codeskulptor.org/#user30_UCCst1kTrN9cNAS.py#
########################################################


# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_vel=[0,0]
ball_pos=[300,200]
paddle1_vel, paddle2_vel=0,0
pos1,pos2=HEIGHT/2-35,HEIGHT/2-35
player1,player2=0,0
message="RIGHT"

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if(direction=='RIGHT'):
        ball_vel[0]=random.randrange(2,4);
    else:
        ball_vel[0]=-random.randrange(2,4);
    ball_vel[1]=random.randrange(1,2);

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,pos1,pos2,ball_vel,ball_pos  # these are numbers
    global score1, score2  # these are ints
    ball_vel=[0,0]
    ball_pos=[300,200]
    paddle1_vel, paddle2_vel=0,0
    pos1,pos2=HEIGHT/2-35,HEIGHT/2-35
    spawn_ball(message)

def draw(canvas):
    global paddle1_pos, paddle1_vel,paddle2_vel,paddle2_pos, ball_pos,pos1,pos2, ball_vel
    global message,player2,player1
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "aqua")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "aqua")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "aqua")
    canvas.draw_line([0,1],[WIDTH,1],1,"aqua")
    canvas.draw_line([0,HEIGHT-2],[WIDTH,HEIGHT-2],1,'aqua')
    
    # update ball
    pos1+=paddle1_vel
    pos2+=paddle2_vel
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    if(ball_pos[0]+9>=WIDTH-15 and (ball_pos[1]+9<=10+pos1 +10+ 2*35) and ball_pos[1]+9>pos1-10):
        ball_vel[0]=-ball_vel[0]
        ball_vel[0]+=ball_vel[0]/10 
    elif(ball_pos[0]+9>=WIDTH-15):
        message="LEFT"
        player1+=1
        new_game()
        
    if(ball_pos[1]+9==HEIGHT-12):
        ball_vel[1]=-ball_vel[1]
        
    if(ball_pos[1]-9==0+10):
        ball_vel[1]=-ball_vel[1]
        
    if(ball_pos[0]-9<=15 and(ball_pos[1] +9<= 10 + pos2 +10+2*35) and ball_pos[1]+ 9> pos2-10):
        ball_vel[0]=- ball_vel[0] 
        ball_vel[0]+=ball_vel[0]/10
    elif(ball_pos[0]-9<=15):
        message= 'RIGHT'
        player2+=1
        new_game()
        
    
    # draw ball    
    canvas.draw_circle(ball_pos,18,2,'Lime','Lime')
    
    # update paddle's vertical position, keep paddle on the screen

    if(pos1<=0): pos1=0
    if(pos1 + 2*35>=HEIGHT): pos1=HEIGHT-2*35
    if(pos2<=0):pos2=0
    if(pos2+ 2*35>=HEIGHT): pos2= HEIGHT- 2*35
    
    # draw paddles
    
    canvas.draw_line([WIDTH,pos1],[WIDTH,pos1+2*35],18,'BLUE');
    canvas.draw_line([0,pos2],[0,pos2+2*35],18,'BLUE');
    
    # draw scores
    canvas.draw_text(str(player1),[150,80],35,'yellow');
    canvas.draw_text(str(player2),[450,80],35,'yellow')
 
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['s']:
        paddle1_vel=7
    if key==simplegui.KEY_MAP['down']:
        paddle2_vel=7    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=-7
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=-7
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['s']:
        paddle1_vel=0
    if key==simplegui.KEY_MAP['down']:
        paddle2_vel=0        
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=0
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0

def button_handler():
    global ball_vel,ball_pos,paddle1_vel,paddle2_vel,pos1,pos2,player1,player2,message
    ball_vel=[0,0]
    ball_pos=[300,200]
    paddle1_vel, paddle2_vel=0,0
    pos1,pos2=HEIGHT/2-35,HEIGHT/2-35
    player1,player2=0,0
    message="RIGHT"
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("RESET",button_handler)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
