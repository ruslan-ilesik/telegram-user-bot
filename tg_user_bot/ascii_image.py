from PIL import Image, ImageDraw, ImageFont
import PIL

from __main__ import app,filters


ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str

@app.on_message(filters.command("img_to_ascii", prefixes=".") & filters.me)
def img_to_ascii(_, msg):
    app.download_media(msg, file_name = './downloads/img_to_ascii.jpg')
    chat_id = msg.chat.id
    msg.delete()
    path = './downloads/img_to_ascii.jpg'
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")
    #convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    #save the string to a file
    font_size = 15
    height = len(ascii_img.split('\n'))*font_size
    img = Image.new('RGB', (img_width*font_size/2, height), color = (255,255,255))
    d = ImageDraw.Draw(img)
    d.text((0,0), ascii_img, fill=(0, 0, 0))
    img.save('./downloads/text_to_ascii.png')
    app.send_photo(chat_id ,'./downloads/text_to_ascii.png')
    