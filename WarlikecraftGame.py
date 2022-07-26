from panda3d.core import loadPrcFileData

configVars = """
win-size 1280 720
fullscreen 0
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)

from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight, AmbientLight
from math import sin, cos
import simplepbr


class PointAndAmbientLight(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0, 1)
        self.cam.setPos(0, -12, 0)



        self.light_model = self.loader.loadModel('models/misc/sphere')
        self.light_model.setPos(4, 0, 0)
        self.light_model.reparentTo(self.render)

        
        simplepbr.init()
        self.human = self.loader.loadModel('resources/models/human.gltf')
        self.human.setColor((0.75,0.75,0.75,1))
        self.human.reparentTo(self.render)

        self.map = self.loader.loadModel('resources/models/map')
        self.map.setColor((0.75,0.75,0.75,1))
        self.map.reparentTo(self.render)

        plight = PointLight("plight")
        plight.setShadowCaster(True, 512, 512)
        self.render.setShaderAuto()
        plight.setColor((1,1,1,1))
        self.plnp = self.light_model.attachNewNode(plight)
        # plight.setAttenuation((0, 0, 1))
        self.human.setLight(self.plnp)
        self.map.setLight(self.plnp)

        # alight = AmbientLight("alight")
        # alight.setColor((0.1, 0.1, 0.1, 1))
        # alnp = self.render.attachNewNode(alight)
        # self.human.setLight(alnp)
        # self.map.setLight(alnp)

        self.taskMgr.add(self.move_light, "move-light")

    def move_light(self, task):
        ft = globalClock.getFrameTime()

        self.light_model.setPos(cos(ft)*4, sin(ft)*4, 0)

        return task.cont


game = PointAndAmbientLight()
game.run()