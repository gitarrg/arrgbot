# -*- coding: utf-8 -*-
"""Collection of commonly used Emotes.

A good list of WOW Related Icons can be found here:
https://wow.gamepedia.com/Wowpedia:List_of_mini_icons

"""

import discord

# DEFAULT EMOTES
CONFIRM = "✅"
DECLINE = "❌"
RELOAD = "🔄"
SKIP = "⏭️"
TRASH = "🗑️"
SEND = "✉️"
NEW = "🆕"
GOLD = "💰"
TRADE = "🤝"


GOLD2 = discord.PartialEmoji(id=667911011109699604, name="Gold")


# PEPE EMOTES
PEPESALUTE = discord.PartialEmoji(id=658829912865505280, name="pepesalute")
PEEPOSHRUG = discord.PartialEmoji(id=718959168853114970, name="peepoShrug")
PEPEHELP = discord.PartialEmoji(id=751265054308958219, name="Help")
PEPEPING = discord.PartialEmoji(id=755577531452882944, name="ping")
SADGE = discord.PartialEmoji(id=760304182195650611, name="Sadge")


################################################################################
# World of Wacraft Related Emotes
#

# ROLES
TANK = discord.PartialEmoji(id=710185513545367573, name="Tank")
HEALER = discord.PartialEmoji(id=710185541018189844, name="Healer")
HEAL = HEALER
DPS = discord.PartialEmoji(id=710185554062606346, name="DPS")

## CLASSES
DEATHKNIGHT = discord.PartialEmoji(id=710183948331909212, name="DeathKnight")
HUNTER = discord.PartialEmoji(id=710183962709983283, name="Hunter")
MAGE = discord.PartialEmoji(id=710183976408711248, name="Mage")
MONK = discord.PartialEmoji(id=710183992346804325, name="Monk")
PALADIN = discord.PartialEmoji(id=710184006104252468, name="Paladin")
PRIEST = discord.PartialEmoji(id=710184018645090315, name="Priest")
ROGUE = discord.PartialEmoji(id=710184036512956416, name="Rogue")
SHAMAN = discord.PartialEmoji(id=710184047866806334, name="Shaman")
WARLOCK = discord.PartialEmoji(id=710184060873605150, name="Warlock")
WARRIOR = discord.PartialEmoji(id=710184073447866440, name="Warrior")
DEMONHUNTER = discord.PartialEmoji(id=710184087419355196, name="DemonHunter")
DRUID = discord.PartialEmoji(id=710184134500286617, name="Druid")

MAGE_FIRE = discord.PartialEmoji(id=718673557801926767, name="firemage")   # used when Mastery is on the Vendor

## ARMOR
PLATE = discord.PartialEmoji(id=710191932604678174, name="Plate")
MAIL = discord.PartialEmoji(id=710191784122122344, name="Mail")
LEATHER = discord.PartialEmoji(id=710191900908453973, name="Leather")
CLOTH = discord.PartialEmoji(id=710191815013171225, name="Cloth")


## CURRECNY
ECHOES = discord.PartialEmoji(id=718862724460969994, name="Echoes")
VESSEL = discord.PartialEmoji(id=734397735456866344, name="Vessel")
MEMENTOS = discord.PartialEmoji(id=734397754377371699, name="Mementos")
TORGHAST = discord.PartialEmoji(id=784767773544153129, name="Torghast")


## M+ AFFIXES
AWAKENED = discord.PartialEmoji(id=718570059639029770, name="Awakened")
FORTIFIED = discord.PartialEmoji(id=718570099329597520, name="Fortified")
TYRANNICAL = discord.PartialEmoji(id=718570191729983540, name="Tyrannical")

BOLSTERING = discord.PartialEmoji(id=718570070921707650, name="Bolstering")
BURSTING = discord.PartialEmoji(id=718570079922684018, name="Bursting")
EXPLOSIVE = discord.PartialEmoji(id=718570089196290170, name="Explosive")
GRIEVOUS = discord.PartialEmoji(id=718570108145893448, name="Grievous")
NECROTIC = discord.PartialEmoji(id=718570127813115939, name="Necrotic")
QUAKING = discord.PartialEmoji(id=718570136801640621, name="Quaking")
RAGING = discord.PartialEmoji(id=718570145462616163, name="Raging")
SANGUINE = discord.PartialEmoji(id=718570158389592094, name="Sanguine")
SKITTISH = discord.PartialEmoji(id=718570169680527501, name="Skittish")
TEEMING = discord.PartialEmoji(id=718570180007034971, name="Teeming")
VOLCANIC = discord.PartialEmoji(id=718570203327365193, name="Volcanic")


emotes = {name: emote for name, emote in globals().items() if name.isupper()}
emotes = {name.lower().replace(" ", ""): emote for name, emote in emotes.items()}

def get(name):
    """ShortCut so I can use emotes.get(name)."""
    name = name.lower()
    name = name.replace(" ", "")
    return emotes.get(name)

def gold_str(value):
    """str: gold icon and number text."""
    value = value or 0
    return f"{GOLD} {value:,.0f}"
