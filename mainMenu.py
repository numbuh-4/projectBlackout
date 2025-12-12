import pygame
from settings import *
from game import *
from db_connect import *
class MainMenu:
    def __init__(self):
        
        pygame.init()
        pygame.key.set_repeat(0)
        self.run = True
        #define fonts
        self.font = pygame.font.SysFont("arialblack",20)
        self.font_blackout = pygame.font.SysFont("arialblack",40)
        self.font_big = pygame.font.SysFont("arialblack", 60)
        self.font_small = pygame.font.SysFont("arial", 30)
        self.text_color = (0,0,0)
        #//////////////////////////////////////////////
        self.dbConnection = db_connect()
        self.screenWidth = int(RES_WIDTH)
        self.screenHeight = int(RES_HEIGHT)
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.caption = pygame.display.set_caption("main menu")
        self.backgroundImage = pygame.image.load("resources/screens/mainscreen.png").convert()
        self.scaledBackgroundImage = pygame.transform.scale(self.backgroundImage, (self.screenWidth, self.screenHeight))
        #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.defaultScreen = pygame.image.load("resources/screens/defaultscreen.png").convert()
        self.scaleddefaultScreen = pygame.transform.scale(self.defaultScreen, (self.screenWidth, self.screenHeight))
        

    def draw_text(self,text,font,x,y):
        img = font.render(text, True, self.text_color)
        rect = img.get_rect(topleft=(x, y))
        self.screen.blit(img, rect)
        return rect
    
    
    #chatgpt designed
    def underline_text(self, rect, color=(0,0,0), thickness=2):
        # Draw a line just below the rect
        start_pos = (rect.left, rect.bottom -1)
        end_pos = (rect.right, rect.bottom -1)
        pygame.draw.line(self.screen, color, start_pos, end_pos, thickness)
        
    #chatgpt designed
    def _draw_leaderboard_table(self, scores, start_y):
        """Draws the leaderboard data (headers and rows) centered on the screen."""
        
        # These are the relative distances between columns.
        RELATIVE_POSITIONS = [0, 150, 300, 500] 
        HEADER_LABELS = ["Name", "Score", "Round Died", "Date"]
        ROW_HEIGHT = 40
        
        
        TABLE_WIDTH = RELATIVE_POSITIONS[-1]  # 500
        
        
        LEFT_CENTER_OFFSET = (RES_WIDTH / 2) - (TABLE_WIDTH / 2)
        
        #drawing logic STARTS BELOW 
        #Draw Column Headers (Centered)
        for i, label in enumerate(HEADER_LABELS):
            # The true center X position is the offset PLUS the relative position
            x_center = LEFT_CENTER_OFFSET + RELATIVE_POSITIONS[i]
            
            text_surface = self.font_small.render(label, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(x_center, start_y))
            self.screen.blit(text_surface, text_rect)
        
        data_y = start_y + ROW_HEIGHT
        
        #  Draw Data Rows (Centered)
        for row_index, score_data in enumerate(scores):
            current_y = data_y + (row_index * ROW_HEIGHT)
            
            for col_index, value in enumerate(score_data):
                # Use the same calculated center position
                x_center = LEFT_CENTER_OFFSET + RELATIVE_POSITIONS[col_index]
                
                # Render and Center the data value
                text_value = str(value)
                text_surface = self.font_small.render(text_value, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(x_center, current_y))
                self.screen.blit(text_surface, text_rect)
    #chatgpt designed
    def leaderboard(self):
        running = True
            
        title_text = self.font_big.render("SCOREBOARD", True, (255, 0, 0))
        title_rect = title_text.get_rect(center=(RES_WIDTH / 2, 100))
            
        top_scores = self.dbConnection.fetchingLeaderboard()
        while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        running = False
                
                # 2. Drawing
                self.screen.blit(self.scaleddefaultScreen, (0, 0))
                self.screen.blit(title_text, title_rect)
                
                # Call a dedicated method to handle all the table drawing
                self._draw_leaderboard_table(top_scores, 250) # Start Y position is 250
                
                # 3. Update Screen
                pygame.display.update()

    
    #chatgpt designed
    def game_over_screen(self, final_score, round_died_on):
        death_snapshot = self.screen.copy()
        overlay = pygame.Surface((RES_WIDTH, RES_HEIGHT), pygame.SRCALPHA).convert_alpha()
        overlay.fill((0,0,0,128))
        death_snapshot.blit(overlay,(0,0))
        
        
        font_big = pygame.font.SysFont("arialblack", 60)
        font_small = pygame.font.SysFont("arialblack", 30)
        text_you_died = font_big.render("YOU DIED", True, (255, 0, 0))
        
        
        text_menu = font_small.render("Main Menu", True, (255, 255, 255))
        text_retry = font_small.render("Play Again", True, (255, 255, 255))
        text_Save_score = font_small.render("Save Score", True, (255, 255, 255))

        # Center buttons
        menu_rect = text_menu.get_rect(center=(RES_WIDTH/2, 360))
        retry_rect = text_retry.get_rect(center=(RES_WIDTH/2, 420))
        lead_rect = text_Save_score.get_rect(center=(RES_WIDTH/2, 480))
        died_rect = text_you_died.get_rect(center=(RES_WIDTH/2, 250))
        running = True
        # Draw overlay + options
        while running:
            self.screen.blit(death_snapshot, (0,0))
            self.screen.blit(text_you_died, died_rect)
            self.screen.blit(text_menu, menu_rect)
            self.screen.blit(text_retry, retry_rect)
            self.screen.blit(text_Save_score, lead_rect)

            pygame.display.update()

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_rect.collidepoint(mouse):
                        return "menu"
                    if retry_rect.collidepoint(mouse):
                        running = False
                        return "retry"
                        
                    if lead_rect.collidepoint(mouse):
                        name = self.save_score_screen()
                        self.dbConnection.saveToLeaderboard(name,final_score,round_died_on)
                        break
    #chatgpt designed               
    def save_score_screen(self):
        name = ""
        font_big = pygame.font.SysFont("arialblack", 50)
        font_small = pygame.font.SysFont("arialblack", 30)
        running = True
        pygame.event.clear()
        while running:
            self.screen.fill((20, 20, 20))

            title = font_big.render("SAVE SCORE", True, (255, 255, 255))
            prompt = font_small.render("Enter Name:", True, (255, 255, 255))
            name_text = font_small.render(name, True, (0, 255, 0))
            info = font_small.render("Press ENTER to Save", True, (180, 180, 180))

            # Center positions
            self.screen.blit(title, title.get_rect(center=(RES_WIDTH/2, 120)))
            self.screen.blit(prompt, prompt.get_rect(center=(RES_WIDTH/2, 240)))
            self.screen.blit(name_text, name_text.get_rect(center=(RES_WIDTH/2, 300)))
            self.screen.blit(info, info.get_rect(center=(RES_WIDTH/2, 400)))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # typing
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]

                    else:
                        if len(name) < 12:  # Limit name length
                            name += event.unicode 
        return name
    
    
    
    
    
    
    def startGame(self):
       self.dbConnection.fetchingLeaderboard()
       game = Game()
       result, final_score, round_died_on = game.startGame()
       
    
       running = True
       while running:
        if result == "dead":
                choice = self.game_over_screen(final_score, round_died_on)
                
                if choice == "retry":
                    game = Game()
                    result, final_score, round_died_on = game.startGame()
                    continue
                elif choice == "menu":
                    return "menu"
        elif result == "quit":
            return "quit"
            
    
    def start(self):

        while self.run:
            self.screen.blit(self.scaledBackgroundImage, (0,0))
            projcet = self.draw_text("Project", self.font, 100, 90)
            blackout = self.draw_text("BLACKOUT", self.font_blackout, 96, 120)

            new_game = self.draw_text("New Game", self.font, 100, 290)
            settings = self.draw_text("Settings", self.font, 100, 320)
            leaderboard = self.draw_text("Leaderboard", self.font, 100, 350)
            exit = self.draw_text("Exit", self.font, 100, 380)

            mouse_pos = pygame.mouse.get_pos()

            if new_game.collidepoint(mouse_pos):
                self.underline_text(new_game, color=(255, 0, 0))
            if settings.collidepoint(mouse_pos):
                self.underline_text(settings, color=(255, 0, 0))
            if exit.collidepoint(mouse_pos):
                self.underline_text(exit, color=(255, 0, 0))
            if leaderboard.collidepoint(mouse_pos):
                self.underline_text(leaderboard, color=(255, 0, 0))
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if new_game.collidepoint(mouse_pos):
                        print("new game was clicked")
                        result = self.startGame()
                
                        if result == "quit":
                            self.run = False
                        elif result == "menu":
                            pass
                        
                            
                    if settings.collidepoint(mouse_pos):
                        print("your on settings page")
                    if leaderboard.collidepoint(mouse_pos):
                        self.leaderboard()
                    if exit.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
        pygame.quit()
        sys.exit()

mainMenu = MainMenu()
mainMenu.start()
