import pygame
import tkinter
import tkinter.filedialog

def create_game():
    #initilizes the gamestate
    pygame.init()

    #States window width and height, not resizable 
    WIDTH = 800
    HEIGHT = 600

    PROGRAMSTART = False
    Enter_count = 0
    math_decision_made = False

    scrn = pygame.display.set_mode((WIDTH, HEIGHT))
    first_reached = False
    second_reached = False
    third_reached = False
    fourth_reached = False
    fifth_reached = False

    #these variables are changed to alter the final graph

    is_pie = True
    is_percent = True
    is_one_image = True

        # set the pygame window name
    pygame.display.set_caption('Color Makeup Machine')
    imp = pygame.image.load("C:\\Users\\Ben\Color-Makeup-Machine\images\Front_Page.png").convert()
    scrn.blit(imp, (0, 0))

    pygame.display.flip()
    running = True
    while running:
       
        # create the display surface object
        # of specific dimension..e(X, Y).
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == 13:
                    Enter_count = Enter_count +1
                if event.key == pygame.K_g:
                    is_pie = True
                if event.key == pygame.K_n:
                    is_percent = False
                if event.key == pygame.K_p:
                    is_percent = True
                if event.key == pygame.K_b:
                    is_pie = False
                if event.key == pygame.K_1:
                    is_one_image = True
                if event.key == pygame.K_x:
                    is_one_image = False
                if event.key == pygame.K_SPACE:
                    f = prompt_file()
                    pygame.quit()
                    return (f,is_percent, is_pie, is_one_image)
        
    
        if Enter_count == 1 and (not first_reached):
            imp = pygame.image.load("C:\\Users\\Ben\Color-Makeup-Machine\images\Page2_One_orX.png").convert()
            scrn.blit(imp, (0, 0))
            pygame.display.update()
            first_reached = True


        if Enter_count == 2 and (not second_reached):
            imp = pygame.image.load("C:\\Users\\Ben\Color-Makeup-Machine\images\Page3_Percentage_or_Pixel.png").convert()
            scrn.blit(imp, (0, 0))
            pygame.display.update()
            second_reached = True  

        if Enter_count == 3 and (not third_reached):
            imp = pygame.image.load("C:\\Users\\Ben\Color-Makeup-Machine\images\Page4_Pie_or_bar.png").convert()
            scrn.blit(imp, (0, 0))
            pygame.display.update()
            third_reached = True 
        if Enter_count == 4 and (not fourth_reached):
            imp = pygame.image.load("C:\\Users\\Ben\Color-Makeup-Machine\images\Page5_Final.png").convert()
            scrn.blit(imp, (0, 0))
            pygame.display.update()
            fourth_reached = True  
    

        pygame.display.update()

    # Done! Time to quit.

    pygame.quit()


def prompt_file():
        """Create a Tk file dialog and cleanup when finished"""
        top = tkinter.Tk()
        top.withdraw()  # hide window
        file_name = tkinter.filedialog.askopenfilenames(parent=top)
        top.destroy()
        return file_name
