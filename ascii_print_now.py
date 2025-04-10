import libraries as lib 
#==============================================================================================
class ArtConverter:
    
    def __init__(self, path , font_size = 100, koef_distances = 0.4):
        lib.pg.init()
        self.koef_distances = koef_distances
        self.path = path
        self.image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        self.surface = lib.pg.display.set_mode(self.RES)

        self.ASCII_CHARS = '@&$#8=)+<";:-,. '
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)

        self.font = lib.pg.font.SysFont('One world', font_size, bold=True) #выбор шрифта 
        self.CHAR_STEP = int(font_size * self.koef_distances) #чем меньше коэф. тем будет меньше растояние между символами.
        self.RENDERED_ASCII_CHARS = [self.font.render(char, False, 'BLACK') for char in self.ASCII_CHARS] # список символов
                                                                                                        
                                                                                                          

    def draw_converted_image(self):
        char_indices = self.image // self.ASCII_COEFF
        for x in range(0, self.WIDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                char_index = char_indices[x,y]
                if char_index:
                    self.surface.blit(self.RENDERED_ASCII_CHARS[char_index], (x,y))

    def get_image(self):
        self.cv2_image = lib.cv2.imread(self.path)
        transposed_image = lib.cv2.transpose(self.cv2_image)
        gray_image = lib.cv2.cvtColor(transposed_image, lib.cv2.COLOR_BGR2GRAY) 
        return gray_image

    def draw(self):
        self.surface.fill('white')
        self.draw_converted_image()

    def print_ascii_image(self):
        while True:
            for even in lib.pg.event.get():
                if even.type == lib.pg.QUIT:
                    lib.pg.quit()
                    lib.sys.exit()
                    
            self.draw()
            lib.pg.display.flip()
            
