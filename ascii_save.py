import libraries as lib
#==============================================================================================
class AsciiSave: # если будете копировать из тхт, то нужен шрифт courier туда, куда копируете
    def __init__(self, path , font_size = 100, koef_distances = 0.4):
        lib.pg.init()
        self.koef_distances = koef_distances #чем меньше коэф. тем будет меньше растояние между символами.
        self.font_size = font_size #размер одного символа
        self.path = path
        self.image = self.get_image()
        self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]

        self.ASCII_CHARS = '@&$#8=)+<";:-,. ' #в отличии от ascii_print_now тут от самого закрашеного до нет, тк будет сохранятся и использоваться на белом фоне
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)

        self.CHAR_STEP = int(font_size * self.koef_distances) 

        
    def save_ascii_image(self):
        f = open('result.txt','w')

        self.massiv = ''
        self.char_indices = self.image // self.ASCII_COEFF
        for x in range(0, self.WIDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                self.massiv += str(self.ASCII_CHARS[self.char_indices[x,y]])
        
        copy_ASCII = '' #для копирования в буфер обмена
        for x in range(0,lib.math.ceil(self.HEIGHT / self.CHAR_STEP)):
            for y in range(0,len(self.massiv), lib.math.ceil(self.HEIGHT / self.CHAR_STEP)):
                f.write(self.massiv[y + x]) 
                copy_ASCII += self.massiv[y + x]
                if self.CHAR_STEP < 20: 
                    f.write(self.massiv[y + x])
                    copy_ASCII += self.massiv[y + x]
                elif self.CHAR_STEP < 10: 
                    f.write(self.massiv[y + x])
                    copy_ASCII += self.massiv[y + x]
                else: 
                    f.write(" ")
                    copy_ASCII += " "
            f.write('\n')
            copy_ASCII += '\n'
        lib.pyperclip.copy(copy_ASCII)
        f.close()
            
    def get_image(self):
        self.cv2_image = lib.cv2.imread(self.path) #считывает jpg изображение и сохраняет его 
        self.transposed_image = lib.cv2.transpose(self.cv2_image)
        self.gray_image = lib.cv2.cvtColor(self.transposed_image, lib.cv2.COLOR_BGR2GRAY)
        
        return self.gray_image