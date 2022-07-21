from direct.showbase.ShowBase import ShowBase

from warlikecraft.map.maps import World
from warlikecraft.views.menus import MainMenu, Menu


class WarlikecraftGame(ShowBase):
    def __init__(self):
        super().__init__()
    
    def __initialize(self):
        self.setBackgroundColor(0,0,0)
        # menu: Menu = MainMenu(parent=self)
        # menu.display()

    def start(self):
        self.__initialize()
        self.run()

if (__name__ == "__main__"):
    game: WarlikecraftGame = WarlikecraftGame()
    game.start()
