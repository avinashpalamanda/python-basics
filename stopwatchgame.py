# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 0
x = 0
y = 0
tenth = 0
score = "0/0"
set

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #Finding the tenth value
    global tenth
    tenth = t % 10
    tenths = str(tenth)
    #Checking the format of input and converting it into four digit value
    strlenth = str(t)
    n=len(strlenth)    
    if (n==1):
        strlenth= "000" + strlenth
    elif (n==2):
        strlenth= "00" + strlenth
    elif (n==3):
        strlenth= "0" + strlenth
    #Removing the tenth value and converting the string to 3 length
    interim = strlenth[:3]
    interimvalue = int(interim)
    #Finding the first second value
    seconds1 = strlenth[2]
    seconds1value = int(seconds1)
    #Finding the minute value; by subtracting the interim value with the first second value and dividing by 6
    a = interimvalue - seconds1value
    b = float(a)/60
    strb = str(b)
    minutes = strb[0]
    #Finding the second seconds value.
    c = strb[1:5]
    seconds2value = float(c)
    seconds2value = int(round(seconds2value*60))
    seconds2 = str(seconds2value) 
    #Finding whole seconds value.
    secondsvalue = seconds2value + seconds1value
    seconds = str(secondsvalue) 
    #Concatenating the seconds with with 0 if the seconds length is 1.
    secondlen = len(seconds)
    if secondlen == 1:
        seconds = "0" + seconds
    #Return the seconds value.    
    return minutes+":"+seconds+"."+tenths
        
# define event handlers for buttons; "Start", "Stop", "Reset"
#Start Handler.
def Start_Handler():
    global set
    set = True
    timer.start()

#Stop Handler.
def Stop_Handler():
    global tenth,score,set
    global y,x
    if set == True :
        y=y+1
        if tenth == 0:
            x=x+1
    score = str(x)+"/"+str(y) 
    set = False
    timer.stop()
    
#Reset Handler.    
def Reset_Handler():
    global interval,score
    global y
    global x
    x=0
    y=0
    interval = 0
    score = str(x)+"/"+str(y) 
    timer.stop()
    

# define event handler for timer with 0.1 sec interval
def tick():
    global interval
    interval = interval + 1
    if interval > 5999:
        interval = 0

# define draw handler
def draw(canvas):
    canvas.draw_text(format(interval), [55, 105], 40, "Red")
    canvas.draw_text(score, [160, 20], 25, "Red")
    
# create frame
frame = simplegui.create_frame("Home", 200, 200)

# register event handlers
button1 = frame.add_button('Start', Start_Handler,100)
button1 = frame.add_button('Stop', Stop_Handler,100)
button1 = frame.add_button('Reset', Reset_Handler,100)

timer = simplegui.create_timer(100, tick)

frame.set_draw_handler(draw)

# start frame
frame.start()
