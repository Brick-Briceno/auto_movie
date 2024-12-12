from PIL import Image, ImageDraw, ImageFont
from kerning_letters import *
import emojis_data

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

def txt_to_img(text, size=36, font="", color=(255, 255, 255),
               stroke_color=(0, 0, 0), stroke_width=0):
    img = Image.new("RGBA", (2000, 2000), (255, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, 32)
    x, y = 20, 0
    if stroke_width != 0: draw.text(
        (x, y), text[0], font=font, fill=stroke_color,
        stroke_width=stroke_width)
    draw.text((x, y), text[0], font=font, fill=color, spacing=8)
    for i, char in enumerate(text[1:]):
        if char == " ":
            x += 10 #spaces px
            continue
        char_px = 20
        #calculate pixels
        if text[i]+char in kerning_letters.keys():
            char_px = kerning_letters[text[i]+char]
        elif text[i] in subtract_by_one_letter.keys():
            char_px = subtract_by_one_letter[text[i]]
        x += char_px

        #print(f"U+{ord(char):04x}")
        if f"U+{ord(char):04x}" in emojis_data.emojis.keys():
            emoji = Image.open(emojis_data.emojis[f"U+{ord(char):04x}"])
            emoji = emoji.resize((34, int(34*(emoji.height/emoji.width))))
            img.paste(emoji, (x+5, y+4))
            x += 10
            continue

        if stroke_width != 0: draw.text(
            (x, y), char, font=font, fill=stroke_color,
            stroke_width=stroke_width)
        #text
        draw.text((x, y), char, font=font, fill=color, spacing=8)
    return img, x

def make_text(text, font, stroke_width=0):
    text += "\n."
    array_lines_img = []
    array_lines_px = []
    for i, line in enumerate(fit_text(text, 26).split("\n")):
        img, x = txt_to_img(line, 34, font, stroke_width=stroke_width)
        array_lines_img.append(img)
        array_lines_px.append(x)

    end = Image.new("RGBA", (max(array_lines_px)+20, 5+i*40), (255, 0, 0, 0))
    for img, px, i in zip(array_lines_img, array_lines_px, range(len(array_lines_px))):
        end.paste(img, ((max(array_lines_px)-px)//2, i*40))
    end.save("subs.png")


text = "POV: Your AirPods died at the gym 🥴🤧"
#text = "To fix this, you need to convert the image to RGB mode before saving it as a JPEG. Here's the modified code:"
#text = "Hello friends of YouTube\nI hope you are doing great"

make_text(text, "fonts/proxima-nova-7.ttf", 2.5)
