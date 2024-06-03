from PIL import Image

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def image_to_ascii(image_path, new_width=100):

    image = Image.open(image_path).convert("L")
    
 
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    image = image.resize((new_width, new_height))
    

    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels])
    
  
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:index + new_width] for index in range(0, ascii_str_len, new_width)])
    
    return ascii_img


image_path = 'kitty.png'


ascii_art = image_to_ascii(image_path, new_width=100)
print(ascii_art)

 # execute python pgm_to_ascii.py no terminal