from pathlib import Path
import webbrowser
# pip install pillow
from PIL import Image

def apply_background_transparency(picture: Path, new_picture_with_transparency: Path=None, background_color: list[int]=[255, 255, 255]):
    """Apply transparency background on a picture. 

    Args:
        picture (Path): The default picture to process applying packground transparency.
        new_picture_with_transparency (Path, optional): The new picture with transparency enabled. If not defined, default 'picture' will be updated. Defaults to None.
        background_color (list[int], optional): The default background color to convert as transparency. Defaults to [255, 255, 255].
    """
    picture = Image.open(picture)
    picture = picture.convert("RGBA")
  
    default_picture_pixels = picture.getdata()
  
    newData = []
  
    for pixel in default_picture_pixels:
        if ((pixel[0] == background_color[0]) and (pixel[1] == background_color[1]) and (pixel[2] == background_color[2])):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(pixel)
  
    picture.putdata(newData)
    if (new_picture_with_transparency == None):
        new_picture_with_transparency = picture
    picture.save(new_picture_with_transparency, "PNG")


url = 'https://codefather.tech/blog/'
webbrowser.open(url)
print(dir(webbrowser))

