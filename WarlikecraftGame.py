from direct.showbase.ShowBase import ShowBase

from warlikecraft.map.maps import World

class WarlikecraftGame(ShowBase):
    def __init__(self):
        super().__init__()
    
    def start(self):
        world: World = World()
        self.run()

if (__name__ == "__main__"):
    game: WarlikecraftGame = WarlikecraftGame()
    game.start()
