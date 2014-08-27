#==========To run, click the link below================#

##########################################################
#http://www.codeskulptor.org/#user30_y4d8oRnCY3EEYjU_2.py#
##########################################################

# template for "Stopwatch: The Game"
import simplegui
import random

# define global variables
tot_passes=0
your_passes=0
time_elapsed=0
position=[60,115]
D=0
bc=0
BC=0
A=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global D,bc,BC,A
    D= time_elapsed%10
    bc=time_elapsed//10
    BC=bc%60
    A=bc//60
    return str(A)+':'+str(BC)+'.'+str(D)   
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    
def Stop():
    if timer.is_running():
        timer.stop()
        if BC%5==0 and BC and D==0:
            global your_passes
            your_passes+=1
            
        global tot_passes
        tot_passes+=1
        
def Restart():
    global time_elapsed,tot_passes,your_passes
    time_elapsed=0
    tot_passes=0
    your_passes=0
    timer.stop()
   
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_elapsed
    time_elapsed+=1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time_elapsed),position,35,'BLUE')
    canvas.draw_text(str(your_passes)+'/'+str(tot_passes),[140,28],28,'Yellow')
    canvas.draw_text("Good Luck!!",[55,168],15,'Pink')
    
# create frame
frame= simplegui.create_frame("Frame",200,200)
frame.add_button("Start",Start,100)
frame.add_button("Stop",Stop,100)
frame.add_button("Reset",Restart,100)
frame.set_draw_handler(draw)
timer= simplegui.create_timer(100,timer_handler)

# register event handlers

# start frame
frame.start()

# Please remember to review the grading rubric
