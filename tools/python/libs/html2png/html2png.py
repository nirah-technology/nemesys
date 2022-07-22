import os
from pathlib import Path
import webbrowser
# pip install pillow
from PIL import Image
from time import sleep
from uuid import uuid4

class HtmlSnapshot:
    __PICTURE_FORMAT: str = "png"

    @staticmethod
    def __convert_html_to_png(html_page: str, picture_name: str, element_id: str="main"):
        """Convert an HTML page to a PNG picture.

        Args:
            html_page (Path): HTML file or URL of the page to convert.
            picture_name (str): Name of the picture to generate.
            element_id (str, optional): Element ID in HTML document to convert as picture. Defaults to "main".
        """
        url: str = "{}?id={}&pictureName={}".format(html_page, element_id, picture_name)
        webbrowser.open(url)

    @staticmethod
    def __wait_while_file_is_not_created(file: Path):
        """Suspend the program while the given file doesn't exists.

        Args:
            file (Path): The file to check.
        """
        while (not file.exists()):
            sleep(0.50)
        previous_file_size: int = -1
        file_stats = os.stat(file)
        current_file_size = 0
        while (previous_file_size != current_file_size):
            current_file_size = file_stats.st_size
            sleep(0.50)
            previous_file_size = current_file_size

    @staticmethod
    def __apply_background_transparency(picture: Path, background_color: list[int]=[255, 255, 255]):
        """Apply transparency background on a picture. 

        Args:
            picture (Path): The default picture to process applying packground transparency.
            new_picture_with_transparency (Path, optional): The new picture with transparency enabled. If not defined, default 'picture' will be updated. Defaults to None.
            background_color (list[int], optional): The default background color to convert as transparency. Defaults to [255, 255, 255].
        """
        print(picture)
        image = Image.open(picture)
        image = image.convert("RGBA")
    
        default_picture_pixels = image.getdata()
    
        newData = []
    
        for pixel in default_picture_pixels:
            if ((pixel[0] == background_color[0]) and (pixel[1] == background_color[1]) and (pixel[2] == background_color[2])):
                newData.append((255, 255, 255, 0))
            else:
                newData.append(pixel)
    
        image.putdata(newData)
        image.save(str(picture), HtmlSnapshot.__PICTURE_FORMAT.upper())

    @staticmethod
    def __move_picture(source: Path, destination: Path):
        """Move the picture to an other location.

        Args:
            source (Path): Source file to move to an other location.
            destination (Path): The new location of the file to move.
        """
        with open(source, 'rb') as file_to_read:
            with open(destination, 'wb') as file_to_write:
                file_to_write.write(file_to_read.read())
        os.remove(source)

    @staticmethod
    def snapshot(url: str, html_balise_id: str, picture_destination_folder: Path, picture_name: str, html_background_color: list[int] = [255,255,255], format: str = "png") -> Path:
        """Create a snapshot (picture) of an HTML element.

        Args:
            url (str): URL of the HTML document to use
            html_balise_id (str): Element ID in the HTML document to convert as picture
            picture_destination_folder (Path): Desitnation where store the generated picture
            picture_name (str): Name of the picture to generate
            html_background_color (list[int]): Default background color in HTML document to convert as transparency
            format (str, optional): Picture format. Defaults to "png".

        Returns:
            Path: _description_
        """

        image_name = picture_name if str(picture_name).endswith(".{}".format(HtmlSnapshot.__PICTURE_FORMAT)) else str("{}.{}".format(picture_name, HtmlSnapshot.__PICTURE_FORMAT))
        picture: Path = Path(picture_destination_folder, image_name)
        downloaded_picture_name: str = "{}.{}".format(str(uuid4()), image_name.split('.')[-1])
        temporary_pictute = Path(Path.home(), "Downloads", downloaded_picture_name)

        HtmlSnapshot.__convert_html_to_png(html_page=url, element_id=html_balise_id, picture_name=downloaded_picture_name)
        HtmlSnapshot.__wait_while_file_is_not_created(temporary_pictute)
        HtmlSnapshot.__move_picture(temporary_pictute, picture)
        HtmlSnapshot.__apply_background_transparency(picture=picture)
        
