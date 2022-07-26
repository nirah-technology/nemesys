from panda3d.core import loadPrcFile

from direct.showbase.ShowBase import ShowBase

from nemesys.map.maps import World
from nemesys.views.menus import MainMenu, Menu

loadPrcFile("conf.prc")

class NemesysGame(ShowBase):
    def __init__(self):
        super().__init__()
    
    def __initialize(self):
        self.setBackgroundColor(0,0,0)
        menu: Menu = MainMenu(parent=self)
        menu.display()

    def start(self):
        self.__initialize()
        self.run()

if (__name__ == "__main__"):
    game: NemesysGame = NemesysGame()
    game.start()
