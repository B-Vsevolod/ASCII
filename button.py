import libraries as lib

#==============================================================================================
def NotHaveInButten_print(): print('!!!!!!!!!!!!in code butten don\'t have function_print_ascii!!!!!!!!!!!!')
def NotHaveInButten_save(): print('!!!!!!!!!!!!ALSO in code butten don\'t have function_save_ascii!!!!!!!!!!!!')

def run(width, height, function_print_ascii = NotHaveInButten_print, function_save_ascii = NotHaveInButten_save):
    lib.pg.init()
    screen = lib.pg.display.set_mode((width, height))

    font = lib.pg.font.SysFont('Arial', 40)

    objects = []

    class Button:
        def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.onclickFunction = onclickFunction
            self.onePress = onePress

            self.fillColors = {
                'normal': '#ffffff',
                'hover': '#666666',
                'pressed': '#333333',
            }

            self.buttonSurface = lib.pg.Surface((self.width, self.height))
            self.buttonRect = lib.pg.Rect(self.x, self.y, self.width, self.height)

            self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

            self.alreadyPressed = False

            objects.append(self)

        def process(self):

            mousePos = lib.pg.mouse.get_pos()
            
            self.buttonSurface.fill(self.fillColors['normal'])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors['hover'])

                if lib.pg.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors['pressed'])

                    if self.onePress:
                        self.onclickFunction()

                    elif not self.alreadyPressed:
                        self.onclickFunction()
                        self.alreadyPressed = True

                else:
                    self.alreadyPressed = False

            self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
                self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
            ])
            screen.blit(self.buttonSurface, self.buttonRect)



    customButton = Button(30, 30, width - 60, height/2 - 60, 'Ascii print now', function_print_ascii)
    customButton = Button(30, height/2 + 10, width -60, height/2 - 60, 'Askii save', function_save_ascii)


    while True:
        screen.fill((20, 20, 20))
        for event in lib.pg.event.get():
            if event.type == lib.pg.QUIT:
                lib.pg.quit()
                lib.sys.exit()

        for object in objects:
            object.process()

        lib.pg.display.flip()
       