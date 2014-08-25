
#==========To run, click the link below================#

########################################################
#http://www.codeskulptor.org/#user30_WDvJQYIOfSkdPRA.py#
########################################################


# implementation of card game - Memory

import simplegui
import random

secret_list=[0,1,2,3,4,5,6,7]
exposed=[False]
turns=0
state=0
prev1,prev2=-1,-2

# helper function to initialize globals
def new_game():
    global secret_list,exposed,state,turns
    turns=0
    state=0
    secret_list*=2
    random.shuffle(secret_list)
    exposed*=16
    for i in range(0,16):
        exposed[i]=False
    pass  
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global prev2,prev1,exposed,turns
    CARD_CLICKED_NO=pos[0] // 50
    
    if(not exposed[CARD_CLICKED_NO]):    
        global state
        if state == 0:
            state = 1
            
        elif state == 1:
            state = 2
            turns+=1
            if secret_list[prev2]==secret_list[CARD_CLICKED_NO]:
                exposed[prev2]=True
                
        else:
            if(prev1!=prev2 and secret_list[prev2]!=secret_list[prev1]):
                exposed[prev1]=False
                exposed[prev2]=False
            state = 1
            
        exposed[CARD_CLICKED_NO]=True
        prev1=prev2
        prev2=CARD_CLICKED_NO   
    
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(0,16):        
        if(not exposed[i]):
            canvas.draw_polyline([[i*50,0],[(i+1)*50,0],[(i+1)*50,100],[i*50,100]],100,'aqua')            
        else :
            canvas.draw_polyline([[i*50,0],[(i+1)*50,0],[(i+1)*50,100],[i*50,100]],100,'red') 	            
            canvas.draw_text(str(secret_list[i]),[i*50+15,60],40,'black')
        canvas.draw_polyline([[i*50,0],[(i+1)*50,0],[(i+1)*50,100],[i*50,100]],4,'black') 
        label.set_text(str(turns))

        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
# Always remember to review the grading rubric