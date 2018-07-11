# template for "Stopwatch: The Game"
import simplegui
# define global variables
t = 0
A = 0
B = 0
C = 0
D = 0
x = 0 #number of times stopped on a whole number
y = 0 #number of times stop is pressed. 
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A,B,C,D
    A = t//600
    if len(str(t%600)) == 3:
        B = str(t%600)[0]
        C = str(t%600)[1]
        D = str(t%600)[2]
    elif len(str(t%600)) == 2:
        B = 0
        C = str(t%600)[0]
        D = str(t%600)[1]
    elif len(str(t%600)) == 1:
        B = 0
        C = 0
        D = str(t%600)[0]
    else:
        B = 0
        C = 0
        D = 0
    print str(A)+":"+str(B)+str(C)+"."+str(D)
    return str(A)+":"+str(B)+str(C)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
z = True
def start():
    global z
    z = True
    timer.start()
def stop():
    global D,y,x,z
    if z == True:
        y = y+1
        z = False
        if (int(D) == 0):
            x = x+1            
        else:
            x = x         
    else:
        x = x 
        y = y
    timer.stop()
def restart():
    timer.stop()
    global t,x,y 
    t = 0
    x = 0 
    y = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    print t
    t = t+1

#number of times stop is pressed on a whole number

    
# define draw handler
def draw(canvas):
    global t,A,B,C,D,x
    canvas.draw_text(str(format(t)),[75,105],25,"White")
    canvas.draw_text(str(x)+"/"+str(y),[160,30],25,"White")
# create frame
frame = simplegui.create_frame("stop watch",200,200)
timer = simplegui.create_timer(100,tick)
# register event handlers
frame.set_draw_handler(draw)
frame.add_button("start",start,50)
frame.add_button("stop",stop,50)
frame.add_button("restart",restart,50)
# start frame
frame.start()
timer.start()
# Please remember to review the grading rubric
