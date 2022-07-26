from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

class Game(ShowBase):
    def __init__(self) -> None:
        super().__init__()

    def launch(self):
        panda = self.loader.loadModel('models/panda')
        panda.setPos(-2, 10, 0)
        panda.setScale(0.2, 0.2, 0.2)
        panda.reparentTo(self.render)
        self.setSceneGraphAnalyzerMeter(True)

        # self.disable_mouse()
        self.run()

game: Game = Game()
game.launch()