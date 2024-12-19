from PIL import Image

def aplicar_mascara(imagen_mascara, imagen_color):
    img_color = Image.open(imagen_color).convert("RGBA")
    img_mascara = Image.open(imagen_mascara).convert("L")

    #Asegura que las imágenes tengan las mismas dimensiones
    if img_color.size != img_mascara.size:
        img_mascara = img_mascara.resize(img_color.size)

    img_color.putalpha(img_mascara)
    return img_color

imagen_con_mascara = aplicar_mascara("bg_img/middle.png", "example.png")
imagen_con_mascara.save("hola.png")
