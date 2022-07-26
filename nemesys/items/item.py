from enum import Enum

from nemesys.utils.color import Color


class QualityValue:
    def __init__(self, id: int, color: Color, description: str) -> None:
        self.id: int = id
        self.color: Color = color
        self.description: str = description

class Quality(Enum):
    POOR=       QualityValue(1, Color(157, 157, 157), "Poor")
    COMMON=     QualityValue(2, Color(255, 255, 255), "Common")
    UNCOMMON=   QualityValue(3, Color(30, 255, 0), "Uncommon")
    RARE=       QualityValue(4, Color(0, 112, 221), "Rare")
    EPIC=       QualityValue(5, Color(163, 53, 238), "Epic")
    LEGENDARY=  QualityValue(6, Color(255, 128, 0), "Legendary")
    ARTIFACT=   QualityValue(7, Color(230, 204, 128), "Artifact")
    HEIRLOOM=   QualityValue(8, Color(0, 204, 255), "Heirloom")

class Item:
    def __init__(self, name: str, quality: Quality=Quality.POOR) -> None:
        self.name: str = name
        self.quality: Quality = quality