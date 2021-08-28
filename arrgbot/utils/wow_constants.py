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


################################################################################
# Corruptions

class CorruptionContaminants:
    def __init__(self, name, rank, price, corruption, info):
        super(CorruptionContaminants, self).__init__()
        self.name = name
        self.corruption = corruption
        self.price = price
        self.info = info
        self.rank = rank or 0
        self.rank_str = self.rank * "I"

    @property
    def icon(self):
        name = self.name.lower().replace(" ", "")
        return emotes.emotes.get(name)

    @property
    def full_name(self):
        return f"{self.name} {self.rank_str}" if self.rank else self.name

    @property
    def icon_and_name(self):
        return f"{self.icon} {self.full_name}"



##############
# PASSIVE

SEVERE_1        = CorruptionContaminants("Severe",        1,  3000, 10, "+6% Crit")
SEVERE_2        = CorruptionContaminants("Severe",        2,  4125, 15, "+9% Crit")
SEVERE_3        = CorruptionContaminants("Severe",        3,  5000, 20, "+12% Crit")
EXPEDIENT_1     = CorruptionContaminants("Expedient",     1,  3000, 10, "+6% Haste")
EXPEDIENT_2     = CorruptionContaminants("Expedient",     2,  4125, 15, "+9% Haste")
EXPEDIENT_3     = CorruptionContaminants("Expedient",     3,  5000, 20, "+12% Haste")
EXPEDIENT_7     = CorruptionContaminants("Expedient",     7,  9750, 35, "+24% Haste")
MASTERFUL_1     = CorruptionContaminants("Masterful",     1,  3000, 10, "+6% Mastery")
MASTERFUL_2     = CorruptionContaminants("Masterful",     2,  4125, 15, "+9% Mastery")
MASTERFUL_3     = CorruptionContaminants("Masterful",     3,  5000, 20, f"+12% {emotes.MAGE_FIRE} Combuuuuust")
VERSATILE_1     = CorruptionContaminants("Versatile",     1,  3000, 10, "+6% Vers")
VERSATILE_2     = CorruptionContaminants("Versatile",     2,  4125, 15, "+9% Vers")
VERSATILE_3     = CorruptionContaminants("Versatile",     3,  5000, 20, "+12% Vers")
VOID_RITUAL_1   = CorruptionContaminants("Void Ritual",   1,  4125, 15, "+14 Secondaries")
VOID_RITUAL_2   = CorruptionContaminants("Void Ritual",   2,  7875, 35, "+34 Secondaries")
VOID_RITUAL_3   = CorruptionContaminants("Void Ritual",   3, 13200, 66, "+66 Secondaries")
SIPHONER_1      = CorruptionContaminants("Siphoner",      1,  4250, 15, "+3% Leech")
SIPHONER_2      = CorruptionContaminants("Siphoner",      2,  6300, 30, "+6% Leech")
SIPHONER_3      = CorruptionContaminants("Siphoner",      3,  9000, 45, "+9% Leech")
AVOIDANT_1      = CorruptionContaminants("Avoidant",      1,  4250,  8, "+8% Haste → Avoidance = 💩")
AVOIDANT_2      = CorruptionContaminants("Avoidant",      2,  4250, 12, "+12% Haste → Avoidance = 💩")
AVOIDANT_3      = CorruptionContaminants("Avoidant",      3,  4250, 16, "+16% Haste → Avoidance = 💩")
STRIKETHROUGH_1 = CorruptionContaminants("Strikethrough", 1,  3000, 10, "+2% Crit DMG/Heal")
STRIKETHROUGH_2 = CorruptionContaminants("Strikethrough", 2,  4000, 15, "+3% Crit DMG/Heal")
STRIKETHROUGH_3 = CorruptionContaminants("Strikethrough", 3,  5000, 20, "+4% Crit DMG/Heal")

##############
# ACTIVE: Procs
RACING_PULSE_1    = CorruptionContaminants("Racing Pulse",     1, 4125, 15, "546 Haste Proc")
RACING_PULSE_2    = CorruptionContaminants("Racing Pulse",     2, 5000, 20, "728 Haste Proc")
RACING_PULSE_3    = CorruptionContaminants("Racing Pulse",     3, 7875, 35, "1275 Haste Proc")
HONED_MIND_1      = CorruptionContaminants("Honed Mind",       1, 4125, 15, "392 Mastery Proc")
HONED_MIND_2      = CorruptionContaminants("Honed Mind",       2, 5000, 20, "523 Mastery Proc")
HONED_MIND_3      = CorruptionContaminants("Honed Mind",       3, 7875, 35, "915 Mastery Proc")
SURGINGVITALITY_1 = CorruptionContaminants("Surging Vitality", 1, 4125, 15, "312 Vers Proc")
SURGINGVITALITY_2 = CorruptionContaminants("Surging Vitality", 2, 5000, 20, "416 Vers Proc")
SURGINGVITALITY_3 = CorruptionContaminants("Surging Vitality", 3, 7875, 35, "728 Vers Proc")
DEADLY_MOMENTUM_1 = CorruptionContaminants("Deadly Momentum",  1, 4125, 15, "5x 31 Crit per stack --> 155")
DEADLY_MOMENTUM_2 = CorruptionContaminants("Deadly Momentum",  2, 5000, 20, "5x 41 Crit per stack --> 205")
DEADLY_MOMENTUM_3 = CorruptionContaminants("Deadly Momentum",  3, 7875, 35, "5x 72 Crit per stack --> 360")

# ACTIVE: DMG
TWISTED_APPENDAGE_1   = CorruptionContaminants("Twisted Appendage",    1,  3000, 15, "small hentai")
TWISTED_APPENDAGE_2   = CorruptionContaminants("Twisted Appendage",    2,  6000, 35, "medium hentai")
TWISTED_APPENDAGE_3   = CorruptionContaminants("Twisted Appendage",    3, 13200, 66, "huuuge hentai")
ECHOING_VOID_1        = CorruptionContaminants("Echoing Void",         1,  6250, 25, "0.4% Heath per stack → 🗑️")
ECHOING_VOID_2        = CorruptionContaminants("Echoing Void",         2,  7875, 35, "0.6% Heath per stack → 🗑️")
ECHOING_VOID_3        = CorruptionContaminants("Echoing Void",         3,  0000, 60, "1.0% Heath per stack → 🗑️")
INFINITE_STARS_1      = CorruptionContaminants("Infinite Stars",       1,  5000, 20, "thing that never reaches 10 stacks")
INFINITE_STARS_2      = CorruptionContaminants("Infinite Stars",       2, 10000, 50, "thing that never reaches 10 stacks")
INFINITE_STARS_3      = CorruptionContaminants("Infinite Stars",       3, 15000, 75, "make sure to put that on 485 ilvl gear")
TWILIGHTDEVASTATION_1 = CorruptionContaminants("Twilight Devastation", 1,  5000,  25, "6% Beam")
TWILIGHTDEVASTATION_2 = CorruptionContaminants("Twilight Devastation", 2, 10000, 50, "12% Beam")
TWILIGHTDEVASTATION_3 = CorruptionContaminants("Twilight Devastation", 3, 15000, 75, "18% Beam")
TWILIGHTDEVASTATION_4 = CorruptionContaminants("Twilight Devastation", 4, 20000, 100, "24% Beam")

GUSCHING_WOUND = CorruptionContaminants("Gushing Wound", None, 4125, 15, "might be still valid after nerf?")

LASH_OF_THE_VOID_1 = CorruptionContaminants("Lash of the Void", 1, 50000, 25, "Can only be applied to Weapons")
LASH_OF_THE_VOID_2 = CorruptionContaminants("Lash of the Void", 2, 75000, 50, "Can only be applied to Weapons")

# Random Shit
GLIMPSE_OF_CLARITY = CorruptionContaminants("Glimpse of Clarity", None, 4125, 15, "3sec cooldown reduction for next spell")
INEFFABLE_TRUTH_1 = CorruptionContaminants("Ineffable Truth", 1, 3300, 12, "30% Cooldown Recovery Proc")
INEFFABLE_TRUTH_2 = CorruptionContaminants("Ineffable Truth", 2, 6750, 30, "50% Cooldown Recovery Proc")


CORRUPTION_VENDOR_SETS = {}
CORRUPTION_VENDOR_SETS[1] = [INEFFABLE_TRUTH_1, HONED_MIND_1, STRIKETHROUGH_2, MASTERFUL_2, EXPEDIENT_3, TWISTED_APPENDAGE_3]
CORRUPTION_VENDOR_SETS[2] = [INEFFABLE_TRUTH_2, VOID_RITUAL_1, DEADLY_MOMENTUM_2, MASTERFUL_1, VERSATILE_3, SIPHONER_2, AVOIDANT_2]
CORRUPTION_VENDOR_SETS[3] = [INFINITE_STARS_1, SURGINGVITALITY_1, GLIMPSE_OF_CLARITY, SEVERE_2, RACING_PULSE_3, SIPHONER_3, AVOIDANT_3]
CORRUPTION_VENDOR_SETS[4] = [TWILIGHTDEVASTATION_2, SEVERE_1, STRIKETHROUGH_3, HONED_MIND_3, EXPEDIENT_2, SIPHONER_1]
CORRUPTION_VENDOR_SETS[5] = [INFINITE_STARS_3, RACING_PULSE_2, ECHOING_VOID_2, SEVERE_3, EXPEDIENT_1, TWISTED_APPENDAGE_1]
CORRUPTION_VENDOR_SETS[6] = [TWILIGHTDEVASTATION_3, RACING_PULSE_1, STRIKETHROUGH_1, MASTERFUL_3, SURGINGVITALITY_2, VOID_RITUAL_2, AVOIDANT_1]
CORRUPTION_VENDOR_SETS[7] = [GUSCHING_WOUND, VERSATILE_1, HONED_MIND_2, INFINITE_STARS_2, DEADLY_MOMENTUM_3, VOID_RITUAL_3, ECHOING_VOID_1]
CORRUPTION_VENDOR_SETS[8] = [TWILIGHTDEVASTATION_1, TWISTED_APPENDAGE_2, SURGINGVITALITY_3, DEADLY_MOMENTUM_1, ECHOING_VOID_3, VERSATILE_2]
CORRUPTION_VENDOR_SETS[0] = CORRUPTION_VENDOR_SETS[8]  # <-- make it easier to loop
