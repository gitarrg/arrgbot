
import arrow


class Expansion:
    """Data container for a WoW-Expansion."""

    def __init__(self, name, release, abbreviations=None, img=""):
        super().__init__()
        self.name = name
        self.release = arrow.get(release, tzinfo="Europe/Paris")
        self.abbreviations = abbreviations or []
        self.img = img


BFA = Expansion(
    "Battle for Azeroth",
    release="2018-08-14",
    abbreviations=["bfa"],
    img="https://wow.zamimg.com/uploads/blog/images/13411-world-of-warcraft-battle-for-azeroth-release-date-is-august-14th.jpg"
)

SHADOWLANDS = Expansion(
    "Shadowlands",
    release="2020-11-23",
    abbreviations=["sl"],
    img="https://scontent-lhr8-2.xx.fbcdn.net/v/t1.6435-9/82158322_10157061179678719_2296017863502200832_n.png?_nc_cat=102&ccb=1-5&_nc_sid=dd9801&efg=eyJpIjoidCJ9&_nc_ohc=iNSUkKzpqU8AX_HlsZ8&_nc_ht=scontent-lhr8-2.xx&oh=ea123b280e8f22c8e16083855d46dc99&oe=615089A3"
)


DRAGONFLIGHT = Expansion(
    "Dragonflight",
    release="2022-11-28",
    abbreviations=["df"],
    img="https://i.imgur.com/U97A6MB.jpeg"
)

