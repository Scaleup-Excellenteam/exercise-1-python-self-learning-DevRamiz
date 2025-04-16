from PIL import Image

def remember_remember(path):
    img = Image.open(path)
    pixels = img.convert("L").getdata()
    chars = [chr(p) for p in pixels if 32 <= p <= 126]
    return ''.join(chars)
