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
    final_descion_made = False
    math_decision_made = False
    is_pie = True
    is_percent = True


    def prompt_file():
        """Create a Tk file dialog and cleanup when finished"""
        top = tkinter.Tk()
        top.withdraw()  # hide window
        file_name = tkinter.filedialog.askopenfilenames(parent=top)
        top.destroy()
        return file_name




    #creates screen
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                

                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == 13:
                    PROGRAMSTART = True
    
            
        
        # Fill the background with white
        screen.fill((32, 42, 68))

        
        if not PROGRAMSTART:
            # Creates the instructions
            text_font = pygame.font.SysFont("any_font", 60)
            text_block = text_font.render(
                "Welcome to the color makeup machine!", False, (200, 100, 0)
            )
            screen.blit(text_block, (10, 50))

            text_font = pygame.font.SysFont("any_font", 20)
            text_block = text_font.render(
                "This program will process all the image files given too it", False, (200, 100, 0)
            )

            screen.blit(text_block, (40, 400))

            text_font = pygame.font.SysFont("any_font", 20)
            text_block = text_font.render(
                "and will then return a graph of the color compisition of those images.", False, (200, 100, 0)
            )
            screen.blit(text_block, (10, 420))
        if PROGRAMSTART:
            screen.fill((32, 42, 68))

            text_font = pygame.font.SysFont("any_font", 20)
            text_block = text_font.render(
                "Click p to have the graph come out as a percetange", False, (200, 100, 0)
            )

            screen.blit(text_block, (40, 400))

            text_font = pygame.font.SysFont("any_font", 20)
            text_block = text_font.render(
                "or click n to have the graph list total number of pixels.", False, (200, 100, 0)
            )
            screen.blit(text_block, (10, 420))

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        math_decision_made = True
                    if event.key == pygame.K_n:
                        is_percent = False
                        math_decision_made = True

        if math_decision_made:
            
            screen.fill((32, 42, 68))

            text_font = pygame.font.SysFont("any_font", 20)
            text_block = text_font.render(
                "Click p to have the graph come out as a pie chart", False, (200, 100, 0)
            )

            screen.blit(text_block, (40, 400))

            text_font = pygame.font.SysFont("any_font", 20)
            text_block = text_font.render(
                "or click b to have the graph come out as a bar graph.", False, (200, 100, 0)
            )
            screen.blit(text_block, (10, 420))

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        final_descion_made = True
                    if event.key == pygame.K_b:
                        is_pie = False
                        final_descion_made = True

        if final_descion_made:
            
            screen.fill((32, 42, 68))

            text_font = pygame.font.SysFont("any_font", 20)
            text_block = text_font.render(
                "Now just click space, and select your images.", False, (200, 100, 0)
            )
            screen.blit(text_block, (40, 400))

            text_font = pygame.font.SysFont("any_font", 20)
            text_block = text_font.render(
                "or click b to have the graph come out as a bar graph.", False, (200, 100, 0)
            )
            screen.blit(text_block, (10, 420))

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        f = prompt_file()
                        return (f,is_percent, is_pie)
        

        #Creates the 

        # Flip the display
        pygame.display.update()

    # Done! Time to quit.

    pygame.quit()


