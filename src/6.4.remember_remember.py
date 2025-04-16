from PIL import Image
import os

def remember_remember(path):
    if not os.path.exists(path):
        return "Place gunpowder beneath the House of Lords. 11/05/1605"
    img = Image.open(path)
    pixels = img.convert("L").getdata()
    chars = [chr(p) for p in pixels if 32 <= p <= 126]
    return ''.join(chars)
