import libraries as lib 
import ascii_print_now as AP
import ascii_save as AS
import button 

if __name__ == '__main__':
    font_size = 20
    koef_distances = 0.6
    
    file = lib.easygui.fileopenbox()
    if not file: lib.sys.exit()
   
    print_ascii = AP.ArtConverter(file, font_size,koef_distances)
    save_ascii = AS.AsciiSave(file,font_size,koef_distances)    
    button.run(print_ascii.WIDTH, print_ascii.HEIGHT, print_ascii.print_ascii_image, save_ascii.save_ascii_image)