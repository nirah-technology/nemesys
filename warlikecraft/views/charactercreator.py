from direct.gui.DirectGui import DirectButton, DirectFrame, DGG, DirectRadioButton

from warlikecraft.characters.gender import Gender

class CharacterCreator:
    def __init__(self) -> None:
        self.__creator_step_1 = DirectFrame(frameColor = (1, 1, 1, 0))
        self.__creator_step_2 = DirectFrame(frameColor = (1, 1, 1, 0))
        self.hide()
        self.__create_gender_block()
        # self.__create_alliance_races_block()
        # self.__create_horde_races_block()
        # self.__create_classes_per_race_block()
        # self.__create_return_main_menu_button()
        # self.__create_continue_button()

        self.__selected_gender: Gender = Gender.MALE
        self.__selected_faction = None
        self.__selected_race = None
        self.__selected_class = None

    def __use_male_gender(self):
        self.__selected_gender = Gender.MALE

    def __use_feminine_gender(self):
        self.__selected_gender = Gender.FEMININE

    def __create_gender_block(self):
    
        gender_panel = DirectFrame(frameColor = (1, 1, 1, 0))
        # gender_panel.setPos
        
        genders_radio_buttons = [
            DirectRadioButton(text='Male', variable=[self.__selected_gender], value=[Gender.MALE],
                            scale=0.05, pos=(-0.4, 0, 0), command=self.__use_male_gender),
            DirectRadioButton(text='Feminine', variable=[self.__selected_gender], value=[Gender.FEMININE],
                            scale=0.05, pos=(0, 0, 0), command=self.__use_feminine_gender)
        ]

        for button in genders_radio_buttons:
            button.setOthers(genders_radio_buttons)
    
    def display(self):
        self.__creator_step_1.show()
        pass

    def hide(self):
        self.__creator_step_2.hide()
        self.__creator_step_1.hide()
        pass