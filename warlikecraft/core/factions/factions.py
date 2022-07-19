from enum import Enum

class Faction(Enum):
    NEUTRAL=1
    HORDE=2,
    ALLIANCE=3

class SubFactionValue:
    def __init__(self, id: int, faction: Faction, name: str) -> None:
        self.id: int = id
        self.faction: Faction = faction
        self.name: str = name

class SubFaction(Enum):
    LOWER_CITY=SubFactionValue(1, Faction.NEUTRAL, "Lower City")
    SHA_TARI_SKYGUARD=SubFactionValue(1, Faction.NEUTRAL, "Sha'tari Skyguard")
    SHATTERED_SUN_OFFENSIVE=SubFactionValue(1, Faction.NEUTRAL, "Shattered Sun Offensive")
    THE_ALDOR=SubFactionValue(1, Faction.NEUTRAL, "The Aldor")
    THE_SCRERS=SubFactionValue(1, Faction.NEUTRAL, "The Scryers")
    SHA_TAR=SubFactionValue(1, Faction.NEUTRAL, "Sha'tar")