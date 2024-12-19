from PIL import Image, ImageDraw, ImageFont
from kerning_letters import *
import emojis_data

#load background data
mask = Image.open("mask.png")

def hex_to_rgb(hexa):
    #obvio se puede empezar con un # u otra cosa :v
    if len(hexa) == 7:
        return int(hexa[1:3],16), int(hexa[3:5],16), int(hexa[5:],16), 255
    elif len(hexa) == 4:
        return int(hexa[1],16)*17, int(hexa[2],16)*17, int(hexa[3],16)*17, 255
    elif len(hexa) == 9:
        return int(hexa[1:3],16), int(hexa[3:5],16), int(hexa[5:7],16), int(hexa[7:],16)
    elif len(hexa) == 5:
        return int(hexa[1],16)*17, int(hexa[2],16)*17, int(hexa[3],16)*17, int(hexa[4],16)*17
    else: raise TypeError(f"This is not an RGB hex code:{hexa}")

def fit_text(text, max_length=20):
    words = text.split(" ")
    line, result = "", ""
    for word in words:
        if len(line) + len(word) + 1 <= max_length:
            line += word + " "
        else:
            result += line.strip() + "\n"
            line = word + " "
    result += line.strip()
    return result

def merge_with_transparency(background, top, position):
    #Make sure both images have the same mode (RGBA for transparency)
    background = background.convert('RGBA')
    top = top.convert('RGBA')
    #Create a copy of the background to avoid modifying the original
    merged_image = background.copy()
    #Paste the top image onto the background at the specified position
    merged_image.paste(top, position, top) #The top mask handles transparency

    return merged_image

def txt_to_img(text, font, font_size=48, color=(255, 255, 255),
               stroke_color=(0, 0, 0), stroke_width=0):
    img = Image.new("RGBA", (2000, 2000), (255, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, font_size)
    x, y = 20, 0
    base = font_size*(1/32)
    if stroke_width != 0: draw.text(
        (x, y), text[0], font=font, fill=stroke_color,
        stroke_width=stroke_width)
    draw.text((x, y), text[0], font=font, fill=color, spacing=8)
    for i, char in enumerate(text[1:]):
        if char == " ":
            x += int(10*base) #spaces px
            continue
        char_px = int(10*base)
        #calculate pixels
        if text[i]+char in kerning_letters.keys():
            char_px = kerning_letters[text[i]+char]
        elif text[i] in subtract_by_one_letter.keys():
            char_px = subtract_by_one_letter[text[i]]
        x += int(char_px*base)

        if f"U+{ord(char):04x}" in emojis_data.emojis.keys():
            emoji = Image.open(emojis_data.emojis[f"U+{ord(char):04x}"])
            emoji = emoji.resize((int(34*base), int(int(34*base)*(emoji.height/emoji.width))))
            #img = merge_with_transparency(img, emoji, (x-15, y+4))
            img = merge_with_transparency(img, emoji, (x-int(9*base), int(9-y*base)))
            x += int(base)*18
            continue
        elif not char.isascii():
            print(f"Character U+{ord(char):04x} not found")

        if stroke_width != 0: draw.text(
            (x, y), char, font=font, fill=stroke_color,
            stroke_width=stroke_width)
        #text
        draw.text((x, y), char, font=font, fill=color, spacing=8)
    return img, x

def make_text(text, font, font_size=60, color="#000", stroke_width=0,
              stroke_color="#000", background=False):
    text += "\n."
    array_lines_img = []
    array_lines_px = []
    color = hex_to_rgb(color)
    stroke_color = hex_to_rgb(stroke_color)
    text = text.replace("w ", "w  ")
    base = font_size*(1/32)
    for i, line in enumerate(fit_text(text, 26).split("\n")):
        img, x = txt_to_img(line, font, font_size, stroke_width=stroke_width,
                            color=color, stroke_color=stroke_color)
        array_lines_img.append(img)
        array_lines_px.append(x)
    
    array_lines_img.pop()
    array_lines_px.pop()

    end = Image.new("RGBA", (max(array_lines_px)+int(22*base), 5+i*int(40*base)), (255, 0, 0, 0))
    for img, px, i in zip(array_lines_img, array_lines_px, range(len(array_lines_px))):
        end = merge_with_transparency(end, img, ((max(array_lines_px)-px)//2, i*int(40*base)))

    if background:
        background = hex_to_rgb(background)
        x, y = end.size
        the_end = Image.new("RGBA", (x+18, y-8), (0, 0, 0, 0))
        #create mask
        for i, z in enumerate(array_lines_px):
            z *= 1.01
            z = int(z)
            layer = mask.resize((z+35, 90))
            the_end = merge_with_transparency(the_end, layer, ((10+(max(array_lines_px)-z)//2), -7+(i*73)))
        #Blend text with background
        the_end = merge_with_transparency(the_end, end, (0, 0))

        return the_end
    return end
