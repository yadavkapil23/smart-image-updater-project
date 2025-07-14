from PIL import Image

def make_square(img_path, output_path, size=500):
    img = Image.open(img_path)
    new_img = Image.new("RGB", (size, size), (255, 255, 255))
    img.thumbnail((size, size))
    offset = ((size - img.size[0]) // 2, (size - img.size[1]) // 2)
    new_img.paste(img, offset)
    new_img.save(output_path)
