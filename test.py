from PIL import Image

def emoji_img(emoji):
    return Image.open(
        f"Emojis\\x2\\U+{ord(emoji):04x}.png")
