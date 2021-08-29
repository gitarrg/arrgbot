
# IMPORT THIRD PARTY LIBRARIES
import discord

# IMPORT LOCAL LIBRARIES
from arrgbot import emotes


## CORRUPTIONS
CORRUPTION_EMOTES = {}
CORRUPTION_EMOTES["avoidant"] = discord.PartialEmoji(id=713402473968042044, name="Avoidant")
CORRUPTION_EMOTES["deadlymomentum"] = discord.PartialEmoji(id=713402486337175575, name="DeadlyMomentum")
CORRUPTION_EMOTES["echoingvoid"] = discord.PartialEmoji(id=713402498747990118, name="EchoingVoid")
CORRUPTION_EMOTES["expedient"] = discord.PartialEmoji(id=713402519010803813, name="Expedient")
CORRUPTION_EMOTES["glimpseofclarity"] = discord.PartialEmoji(id=713402533040619570, name="GlimpseofClarity")
CORRUPTION_EMOTES["gushingwound"] = discord.PartialEmoji(id=713402549411250177, name="GushingWound")
CORRUPTION_EMOTES["honedmind"] = discord.PartialEmoji(id=713402561159495720, name="HonedMind")
CORRUPTION_EMOTES["ineffabletruth"] = discord.PartialEmoji(id=713402574161576027, name="IneffableTruth")
CORRUPTION_EMOTES["infinitestars"] = discord.PartialEmoji(id=713402587315044362, name="InfiniteStars")
CORRUPTION_EMOTES["masterful"] = discord.PartialEmoji(id=713402599428325417, name="Masterful")
CORRUPTION_EMOTES["racingpulse"] = discord.PartialEmoji(id=713402613445558323, name="RacingPulse")
CORRUPTION_EMOTES["severe"] = discord.PartialEmoji(id=713402626263482529, name="Severe")
CORRUPTION_EMOTES["siphoner"] = discord.PartialEmoji(id=713402641648058469, name="Siphoner")
CORRUPTION_EMOTES["strikethrough"] = discord.PartialEmoji(id=713402655900172389, name="Strikethrough")
CORRUPTION_EMOTES["surgingvitality"] = discord.PartialEmoji(id=713402668621758567, name="SurgingVitality")
CORRUPTION_EMOTES["twilightdevastation"] = discord.PartialEmoji(id=713402684874686475, name="TwilightDevastation")
CORRUPTION_EMOTES["twistedappendage"] = discord.PartialEmoji(id=713402699215011870, name="TwistedAppendage")
CORRUPTION_EMOTES["versatile"] = discord.PartialEmoji(id=713402711839604828, name="Versatile")
CORRUPTION_EMOTES["voidritual"] = discord.PartialEmoji(id=713402745654083596, name="VoidRitual")
CORRUPTION_EMOTES["lashofthevoid"] = discord.PartialEmoji(id=718675065557745724, name="LashOfTheVoid")



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
        return CORRUPTION_EMOTES.get(name)

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
