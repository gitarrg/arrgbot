#pylint: disable=C0326
#pylint: disable=C0301

import discord
from arrgbot import emotes

ROLES = ("Tank", "Healer", "DPS")


# dict[str:str]: ClassName to ArmorType Mappings
CLASS_ARMOR = {
    "Warlock": "Cloth",
    "Mage": "Cloth",
    "Priest": "Cloth",
    "Druid": "Leather",
    "Monk": "Leather",
    "Rogue": "Leather",
    "Demon Hunter": "Leather",
    "Hunter": "Mail",
    "Shaman": "Mail",
    "Death Knight": "Plate",
    "Warrior": "Plate",
    "Paladin": "Plate",
}


CLASSES = list(CLASS_ARMOR.keys())


CLASS_COLOR = {
    "Death Knight":    discord.Color.from_rgb(196, 31,  59),
    "Demon Hunter":    discord.Color.from_rgb(163, 48,  201),
    "Druid":           discord.Color.from_rgb(255, 125, 10),
    "Hunter":          discord.Color.from_rgb(169, 210, 113),
    "Mage":            discord.Color.from_rgb(64,  199, 235),
    "Monk":            discord.Color.from_rgb(0,   255, 150),
    "Paladin":         discord.Color.from_rgb(245, 140, 186),
    "Priest":          discord.Color.from_rgb(254, 254, 254),
    "Rogue":           discord.Color.from_rgb(255, 245, 105),
    "Shaman":          discord.Color.from_rgb(0,   112, 222),
    "Warlock":         discord.Color.from_rgb(135, 135, 237),
    "Warrior":         discord.Color.from_rgb(199, 156, 110),
}


AFFIX_WEEKS = {}
AFFIX_WEEKS[1]  = ["Awakened", "Tyrannical", "Teeming", "Volcanic"]
AFFIX_WEEKS[2]  = ["Awakened", "Fortified", "Bolstering", "Skittish"]
AFFIX_WEEKS[3]  = ["Awakened", "Tyrannical", "Bursting", "Necrotic"]
AFFIX_WEEKS[4]  = ["Awakened", "Fortified", "Sanguine", "Quaking"]
AFFIX_WEEKS[5]  = ["Awakened", "Tyrannical", "Bolstering", "Explosive"]
AFFIX_WEEKS[6]  = ["Awakened", "Fortified", "Bursting", "Volcanic"]
AFFIX_WEEKS[7]  = ["Awakened", "Tyrannical", "Raging", "Necrotic"]
AFFIX_WEEKS[8]  = ["Awakened", "Fortified", "Teeming", "Quaking"]
AFFIX_WEEKS[9]  = ["Awakened", "Tyrannical", "Bursting", "Skittish"]
AFFIX_WEEKS[10] = ["Awakened", "Fortified", "Bolstering", "Grievous"]
AFFIX_WEEKS[11] = ["Awakened", "Tyrannical", "Raging", "Explosive"]
AFFIX_WEEKS[12] = ["Awakened", "Fortified", "Sanguine", "Grievous"]
