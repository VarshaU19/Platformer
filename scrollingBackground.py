  
scroll = 0  #define main variables in scrolling

tiles = math.ceil(1500 / 750) + 1 #here 1 is the constant for removing buffering

while True:
    #append the image to the back of the same image to create scrolling effect
    i = 0 #initialize loop variable
    while (i < tiles): #loop to draw multiple background images
        screen.blit(background, (i * 500 + scroll, 0)) 
        i += 1
        scroll -= 2

    if abs(scroll) > 750: #to reset scroll variable 
        scroll = 0