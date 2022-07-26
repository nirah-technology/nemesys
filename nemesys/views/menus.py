from abc import abstractmethod
from pathlib import Path
from direct.gui.DirectGui import DirectButton, DirectFrame, DGG
from colorama import init, Fore

from nemesys.views.charactercreator import CharacterCreator

init(autoreset=True)

class Menu:
    @abstractmethod
    def display(self):
        """Display the menu.
        """
        raise NotImplementedError()

    @abstractmethod
    def hide(self):
        """Hide the menu.
        """
        raise NotImplementedError()

class MainMenu(Menu):

    def __init__(self, parent) -> None:
        self.__menu = DirectFrame(
            frameColor = (1, 1, 1, 1),
            frameSize=(-1, 1, -1, 1),
            pos=(0, 0, 0))
        self.__menu.setImage("resources/assets/pictures/logon.png")
        self.hide()
        self.__button_textures = (
            parent.loader.loadTexture("resources/assets/pictures/button.png"),
            parent.loader.loadTexture("resources/assets/pictures/button-pressed.png"),
            parent.loader.loadTexture("resources/assets/pictures/button-hover.png"),
            parent.loader.loadTexture("resources/assets/pictures/button-disabled.png")
        )
        self.__create_new_game_button()
        self.__create_continue_game_button()
        self.__create_open_settings_button()
        self.__create_quit_button()


    def __start_new_game(self):
        print("Start new game")
        self.hide()
        character_creator: CharacterCreator = CharacterCreator()
        character_creator.display()

    def __continue_game(self):
        print("Continue game")
        self.hide()

    def __open_game_settings(self):
        print("Open settings")
        self.hide()

    def __create_new_game_button(self):
        new_game_button = DirectButton(text = "New Game",
                   command = self.__start_new_game,
                   pos = (0, 0, 0),
                   parent = self.__menu,
                   scale = 0.1,
                #    text_font = self.font,
                #    clickSound = loader.loadSfx("Sounds/UIClick.ogg"),
                   frameTexture = self.__button_textures,
                   frameSize = (-4, 4, -0.75, 0.75),
                   text_scale = 0.75,
                   relief = DGG.FLAT,
                   text_pos = (0, -0.2))
        new_game_button.setTransparency(True)

    def __create_continue_game_button(self):
        backup_file = Path(Path.home(), ".warlikecreaft", "warlikecreaft.save")

        continue_game_button = DirectButton(text = "Continue Game",
                   command = self.__continue_game,
                   pos = (0, 0, -0.25),
                   parent = self.__menu,
                   scale = 0.1,
                #    text_font = self.font,
                #    clickSound = loader.loadSfx("Sounds/UIClick.ogg"),
                   frameTexture = self.__button_textures,
                   frameSize = (-4, 4, -0.75, 0.75),
                   text_scale = 0.6,
                   relief = DGG.FLAT,
                   text_pos = (0, -0.2))
        continue_game_button.setTransparency(True)
        if (not backup_file.exists()):
            continue_game_button.node().setActive(False)

    def __create_open_settings_button(self):
        game_settings_button = DirectButton(text = "Settings",
                   command = self.__open_game_settings,
                   pos = (0, 0, -0.5),
                   parent = self.__menu,
                   scale = 0.1,
                #    text_font = self.font,
                #    clickSound = loader.loadSfx("Sounds/UIClick.ogg"),
                   frameTexture = self.__button_textures,
                   frameSize = (-4, 4, -0.75, 0.75),
                   text_scale = 0.75,
                   relief = DGG.FLAT,
                   text_pos = (0, -0.2))
        game_settings_button.setTransparency(True)

    def __create_quit_button(self):
        game_settings_button = DirectButton(text = "Quit",
                   command = exit,
                   pos = (0, 0, -0.75),
                   parent = self.__menu,
                   scale = 0.1,
                #    text_font = self.font,
                #    clickSound = loader.loadSfx("Sounds/UIClick.ogg"),
                   frameTexture = self.__button_textures,
                   frameSize = (-4, 4, -0.75, 0.75),
                   text_scale = 0.75,
                   relief = DGG.FLAT,
                   text_pos = (0, -0.2))
        game_settings_button.setTransparency(True)

    def display(self):
        self.__menu.show()

    def hide(self):
        self.__menu.hide()

class PauseMenu(Menu):
    def __init__(self) -> None:
        pass