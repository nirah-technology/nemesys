# **NEMESYS**
-----

![WarLikeCraft - Version](https://img.shields.io/badge/version-0.1.0-informational?style=flat)
![Language - Python](https://img.shields.io/badge/language-python-informational?style=flat)
![Python - Version](https://img.shields.io/badge/python-3.10-informational?style=flat)
![License - TOBEDEFINED](https://img.shields.io/badge/license-TBD-informational?style=flat)
![Graphical Engien - Panda3D](https://img.shields.io/badge/graphic_engine-panda3d-informational?style=flat)

## **SUMMARY**
-----
1. [OVERVIEW](#OVERVIEW)
2. [MODULE COMPILATION](#MODULE_COMPILATION)
2. [MODULE INSTALLATION](#MODULE-INSTALLATION)
2. [MODULE USAGE](#MODULE-USAGE)
2. [PICTURES GENERATOR](#PICTURES_GENERATOR)
3. Comp

## **OVERVIEW**
-----
***`Nemesys`*** is a video game based on the ***`World Of Warcraft`*** video game developped by **`Blizard`** company.

However, ***`Nemesys`*** is not a Massively Multiplayer Online Role-Playing game, but it's an offline/solo playable video game.

## **MODULE COMPILATION**
-----
When we compile this module, a new file using `.whl` extension will be created.
When this last file exists, it can be used/install the `nemesys` module.

```cmd
python setup.py bdist_wheel
```

## **MODULE INSTALLATION**
-----
When we install this module, we can use the `nemesys` module.
```cmd
python -m pip install dist/nemesys-<sersion>-py3-none-any.whl
```

## **MODULE USAGE**
If you want to use the `nemesys` module as executable, yo can use this boilerplate code:

```python
from nemesys import NemesysGame

game: NemesysGame = NemesysGame()
game.start()
```

## **PICTURES GENERATOR**
All pictures of the video game are dynamicaly generated from HTML/CSS sources.
- **HTML/CSS sources**: [resources/assets/pictures/src/styling/styling.html](resources/assets/pictures/src/styling/styling.html)

To generate picture, a Python script must be executed.
- **Python script file**: [tools/python/png-generator.py](tools/python/png-generator.py)

This file will use a module called `html2png` that expose the `HtmlSnapshot` class that and `snapshot(url, html_id, folder_destination, picture_name)` static function.

## **FEATURE**
-----
| Feature | Is Implemented |
|---|:-:|
| TBD | &check; |
| TBD | &cross;  |