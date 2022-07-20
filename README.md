# **War-Like-Craft**
-----

![WarLikeCraft - Version](https://img.shields.io/badge/version-0.1.0-informational?style=flat)
![Language - Python](https://img.shields.io/badge/language-python-informational?style=flat)
![Python - Version](https://img.shields.io/badge/python-3.10-informational?style=flat)
![License - TOBEDEFINED](https://img.shields.io/badge/license-TBD-informational?style=flat)
![Graphical Engien - Panda3D](https://img.shields.io/badge/graphic_engine-panda3d-informational?style=flat)

## **SUMMARY**
-----
1. Overview
2. Requirements
3. Comp

## **OVERVIEW**
-----
***`War-Like-Craft`*** is a video game based on the ***`World Of Warcraft`*** video game developped by **`Blizard`** company.

However, ***`War-Like-Craft`*** is not a Massively Multiplayer Online Role-Playing game, but it's an offline/solo playable video game.

## **COMPILING**
-----
When we compile this module, a new file using `.whl` extension will be created.
When this last file exists, it can be used/install the `warlikecraft` module.

```cmd
python setup.py bdist_wheel
```

## **INSTALLING**
-----
When we install this module, we can use the `warlikecraft` module.
```cmd
python -m pip install dist/warlikecraft-<sersion>-py3-none-any.whl
```

## **USAGE**
If you want to use the `warlikecraft` module as executable, yo can use this boilerplate code:

```python
from warlikecraft import WarlikecraftGame

game: WarlikecraftGame = WarlikecraftGame()
game.start()
```

## **FEATURE**
-----
| Feature | Is Implemented |
|---|:-:|
| TBD | &check; |
| TBD | &cross;  |