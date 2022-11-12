from __future__ import annotations

from dataclasses import dataclass

__VERSION__ = "1.8.7"

from typing import Final


@dataclass
class Channels:
    suggestion_reddit_bot: int = 982353129913851924
    bug_report_reddit_bot: int = 982669110926250004
    suggestion_ogiroid: int = 985554479405490216
    bug_report_ogiroid: int = 985554459948122142
    errors: int = 986531210283069450
    reddit_faq: int = 985908874362093620
    tickets: int = 1005904969737711760
    logs: int = 977581277010100315
    staff_vote: int = 1005741491861344286
    welcome: int = 905183354930995320
    goodbye: int = 905183354930995320  # same as welcome
    starboard: int = 1011210884875550821
    reddit_bot: int = 981613938166890556
    introduction: int = 980049243236597780
    general: int = 897666935708352587
    roles: int = 933102052173828136
    rules: int = 905182869410955355
    uploads: int = 1033712950252408884

    @classmethod
    def dev(cls):
        cls.suggestion_reddit_bot: int = 1007334702442619010
        cls.bug_report_reddit_bot: int = 1007334758214279198
        cls.suggestion_ogiroid: int = 985554479405490216
        cls.bug_report_ogiroid: int = 985554459948122142
        cls.reddit_faq: int = 985908874362093620
        cls.tickets: int = 1003006753564262452
        cls.logs: int = 988162723890217040
        cls.staff_vote: int = 1002132747441152071
        cls.welcome = cls.goodbye = 985961186107461673
        cls.starboard: int = 985936949581865030
        cls.reddit_bot: int = 1012349179810553917
        cls.introduction: int = 1013853473172893837
        cls.general: int = 985729550732394536
        cls.roles: int = 1013853473172893837
        cls.rules: int = 1013853473172893837
        cls.uploads: int = 1013853473172893837
        return cls


@dataclass
class Guilds:
    # Lewis server
    main_guild: int = 897666935708352582

    @classmethod
    def dev(cls):
        # Ogiroid testing server
        cls.main_guild: int = 985234686878023730
        return cls


@dataclass
class Roles:
    staff: int = 980700205328502794
    yt_announcements: int = 1010237178036633670

    @classmethod
    def dev(cls):
        cls.staff: int = 985943266115584010
        cls.yt_announcements: int = 1007202835957563412
        return cls


@dataclass
class Emojis:
    rules: str = "<:rules:1006016761809866752>"
    roles: str = "<:roles:1006016760731926641>"

    @classmethod
    def dev(cls):
        cls.rules: str = "<:emoji_18:1006073757976244244>"
        cls.roles: str = "<:role:990310706874290216>"
        return cls


@dataclass
class Colors:
    invis: int = 0x2F3136
    white: int = 0xFFFFFF


@dataclass
class timings:
    SECOND = 1
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24
    WEEK = DAY * 7
    MONTH = 2592000


def status(stat):
    statuses = {
        "dnd": "<:dnd:1018237238875783359>",
        "online": "<:online:1018237386683068417>",
        "offline": "<:offline:1018237478378934342>",
        "idle": "<:idle:1018240148925857852>",
        "streaming": "<:streaming:879146899809128478>",  # where this emoji
    }
    return statuses[stat]


xp_probability = [
    10,
    10,
    10,
    10,
    11,
    11,
    11,
    11,
    12,
    12,
    12,
    12,
    13,
    13,
    13,
    13,
    14,
    14,
    14,
    14,
    15,
    15,
    15,
    15,
    16,
    16,
    16,
    16,
    17,
    17,
    17,
    17,
    18,
    18,
    18,
    18,
    19,
    19,
    19,
    19,
    20,
    20,
    20,
    20,
    21,
    21,
    21,
    21,
    22,
    22,
    22,
    22,
    23,
    23,
    23,
    23,
    24,
    24,
    24,
    24,
    25,
    25,
    26,
    26,
    27,
    27,
    28,
    28,
    29,
    29,
    30,
    30,
    31,
    31,
    32,
    32,
    33,
    33,
    34,
    34,
    35,
    35,
    36,
    36,
    37,
    37,
    38,
    38,
    39,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
]

LEVELS_AND_XP: Final = {  # credit's for this goes to the mee6 developers as we use the same exp values as them
    0: 0,
    1: 100,
    2: 255,
    3: 475,
    4: 770,
    5: 1_150,
    6: 1_625,
    7: 2_205,
    8: 2_900,
    9: 3_720,
    10: 4_675,
    11: 5_775,
    12: 7_030,
    13: 8_450,
    14: 10_045,
    15: 11_825,
    16: 13_800,
    17: 15_980,
    18: 18_375,
    19: 20_995,
    20: 23_850,
    21: 26_950,
    22: 30_305,
    23: 33_925,
    24: 37_820,
    25: 42_000,
    26: 46_475,
    27: 51_255,
    28: 56_350,
    29: 61_770,
    30: 67_525,
    31: 73_625,
    32: 80_080,
    33: 86_900,
    34: 94_095,
    35: 101_675,
    36: 109_650,
    37: 118_030,
    38: 126_825,
    39: 136_045,
    40: 145_700,
    41: 155_800,
    42: 166_355,
    43: 177_375,
    44: 188_870,
    45: 200_850,
    46: 213_325,
    47: 226_305,
    48: 239_800,
    49: 253_820,
    50: 268_375,
    51: 283_475,
    52: 299_130,
    53: 315_350,
    54: 332_145,
    55: 349_525,
    56: 367_500,
    57: 386_080,
    58: 405_275,
    59: 425_095,
    60: 445_550,
    61: 466_650,
    62: 488_405,
    63: 510_825,
    64: 533_920,
    65: 557_700,
    66: 582_175,
    67: 607_355,
    68: 633_250,
    69: 659_870,
    70: 687_225,
    71: 715_325,
    72: 744_180,
    73: 773_800,
    74: 804_195,
    75: 835_375,
    76: 867_350,
    77: 900_130,
    78: 933_725,
    79: 968_145,
    80: 1_003_400,
    81: 1_039_500,
    82: 1_076_455,
    83: 1_114_275,
    84: 1_152_970,
    85: 1_192_550,
    86: 1_233_025,
    87: 1_274_405,
    88: 1_316_700,
    89: 1_359_920,
    90: 1_404_075,
    91: 1_449_175,
    92: 1_495_230,
    93: 1_542_250,
    94: 1_590_245,
    95: 1_639_225,
    96: 1_689_200,
    97: 1_740_180,
    98: 1_792_175,
    99: 1_845_195,
    100: 1_899_250,
}
MAX_LEVEL: Final = len(LEVELS_AND_XP) - 1
MAX_XP: Final = LEVELS_AND_XP[MAX_LEVEL]

IGNORE_EXCEPTIONS = ["UserBlacklisted"]
morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}
TICKET_PERMS = {
    "send_messages": True,
    "read_messages": True,
    "add_reactions": True,
    "embed_links": True,
    "attach_files": True,
    "read_message_history": True,
    "external_emojis": True,
}
tag_help = {
    "public": {
        "tag get (or /t)": "Gives you the tags value",
        "tag create": "Creates a tag",
        "tag help": "Gives you this help",
        "tag info": "Gives you the tags info (views, owner, etc)",
        "tag list": "Gives you a lists of tags (use the arrows to navigate)",
        "tag claim": "Claims a tag (can only be used if the previous owner is no longer in the server)",
    },
    "owner_only": {
        "tag rename": "Renames a tag",
        "tag edit": "Edits a tag",
        "tag transfer": "Transfers a tag to another user",
        "tag delete": "Deletes a tag",
        "tag alias add": "Adds an alias to a tag",
        "tag alias remove": "Removes an alias from a tag",
    },
}
# noinspection SpellCheckingInspection
COUNTRIES = {
    "🇦🇫": "Afghanistan",
    "🇦🇱": "Albania",
    "🇩🇿": "Algeria",
    "🇦🇩": "Andorra",
    "🇦🇴": "Angola",
    "🇦🇮": "Anguilla",
    "🇦🇬": "Antigua and Barbuda",
    "🇦🇷": "Argentina",
    "🇦🇲": "Armenia",
    "🇦🇺": "Australia",
    "🇦🇹": "Austria",
    "🇦🇿": "Azerbaijan",
    "🇧🇸": "Bahamas",
    "🇧🇭": "Bahrain",
    "🇧🇩": "Bangladesh",
    "🇧🇧": "Barbados",
    "🇧🇾": "Belarus",
    "🇧🇪": "Belgium",
    "🇧🇿": "Belize",
    "🇧🇯": "Benin",
    "🇧🇲": "Bermuda",
    "🇧🇹": "Bhutan",
    "🇧🇴": "Bolivia",
    "🇧🇦": "Bosnia and Herzegovina",
    "🇧🇼": "Botswana",
    "🇧🇷": "Brazil",
    "🇧🇳": "Brunei",
    "🇧🇬": "Bulgaria",
    "🇧🇫": "Burkina Faso",
    "🇧🇮": "Burundi",
    "🇰🇭": "Cambodia",
    "🇨🇲": "Cameroon",
    "🇨🇦": "Canada",
    "🇨🇻": "Cape Verde",
    "🇰🇾": "Cayman Islands",
    "🇨🇫": "Central African Republic",
    "🇹🇩": "Chad",
    "🇨🇱": "Chile",
    "🇨🇳": "China",
    "🇨🇴": "Colombia",
    "🇨🇬": ["Republic of the Congo", "Rep of Congo", "Republic of Congo"],
    "🇨🇩": ["DR Congo", "Democratic Republic of Congo"],
    "🇨🇷": "Costa Rica",
    "🇨🇮": ["Ivory Coast", "cote d ivorie", "Côte d'Ivoire"],
    "🇭🇷": "Croatia",
    "🇨🇺": "Cuba",
    "🇨🇾": "Cyprus",
    "🇨🇿": ["Czechia", "Czech Republic"],
    "🇩🇰": "Denmark",
    "🇩🇯": "Djibouti",
    "🇩🇲": "Dominica",
    "🇩🇴": "Dominican Republic",
    "🇪🇨": "Ecuador",
    "🇪🇬": "Egypt",
    "🇸🇻": "El Salvador",
    "🇬🇶": "Equatorial Guinea",
    "🇪🇷": "Eritrea",
    "🇪🇪": "Estonia",
    "🇸🇿": "Eswatini",
    "🇪🇹": "Ethiopia",
    "🇫🇯": "Fiji",
    "🇫🇮": "Finland",
    "🇫🇷": "France",
    "🇬🇦": "Gabon",
    "🇬🇲": "Gambia",
    "🇬🇪": "Georgia",
    "🇩🇪": "Germany",
    "🇬🇭": "Ghana",
    "🇬🇷": "Greece",
    "🇬🇩": "Grenada",
    "🇬🇺": "Guam",
    "🇬🇹": "Guatemala",
    "🇬🇳": "Guinea",
    "🇬🇼": ["Guinea-Bissau", "guinea bissau"],
    "🇬🇾": "Guyana",
    "🇭🇹": "Haiti",
    "🇭🇳": "Honduras",
    "🇭🇺": "Hungary",
    "🇮🇸": "Iceland",
    "🇮🇳": "India",
    "🇮🇩": "Indonesia",
    "🇮🇷": "Iran",
    "🇮🇶": "Iraq",
    "🇮🇪": "Ireland",
    "🇮🇱": "Israel",
    "🇮🇹": "Italy",
    "🇯🇲": "Jamaica",
    "🇯🇵": "Japan",
    "🇯🇴": "Jordan",
    "🇰🇿": "Kazakhstan",
    "🇰🇪": "Kenya",
    "🇰🇮": "Kiribati",
    "🇰🇵": "North Korea",
    "🇰🇷": "South Korea",
    "🇽🇰": "Kosovo",
    "🇰🇼": "Kuwait",
    "🇰🇬": "Kyrgyzstan",
    "🇱🇦": "Laos",
    "🇱🇻": "Latvia",
    "🇱🇧": "Lebanon",
    "🇱🇸": "Lesotho",
    "🇱🇷": "Liberia",
    "🇱🇾": "Libya",
    "🇱🇮": "Liechtenstein",
    "🇱🇹": "Lithuania",
    "🇱🇺": "Luxembourg",
    "🇲🇬": "Madagascar",
    "🇲🇼": "Malawi",
    "🇲🇾": "Malaysia",
    "🇲🇻": "Maldives",
    "🇲🇱": "Mali",
    "🇲🇹": "Malta",
    "🇲🇷": "Mauritania",
    "🇲🇺": "Mauritius",
    "🇲🇽": "Mexico",
    "🇫🇲": "Micronesia",
    "🇲🇩": "Moldova",
    "🇲🇨": "Monaco",
    "🇲🇳": "Mongolia",
    "🇲🇪": "Montenegro",
    "🇲🇦": "Morocco",
    "🇲🇿": "Mozambique",
    "🇲🇲": "Myanmar",
    "🇳🇦": "Namibia",
    "🇳🇷": "Nauru",
    "🇳🇵": "Nepal",
    "🇳🇱": "Netherlands",
    "🇳🇿": "New Zealand",
    "🇳🇮": "Nicaragua",
    "🇳🇪": "Niger",
    "🇳🇬": "Nigeria",
    "🇳🇺": "Niue",
    "🇲🇰": "North Macedonia",
    "🇳🇴": "Norway",
    "🇴🇲": "Oman",
    "🇵🇰": "Pakistan",
    "🇵🇼": "Palau",
    "🇵🇦": "Panama",
    "🇵🇬": "Papua New Guinea",
    "🇵🇾": "Paraguay",
    "🇵🇪": "Peru",
    "🇵🇭": "Philippines",
    "🇵🇱": "Poland",
    "🇵🇹": "Portugal",
    "🇶🇦": "Qatar",
    "🇷🇴": "Romania",
    "🇷🇺": "Russia",
    "🇷🇼": "Rwanda",
    "🇰🇳": "Saint Kitts and Nevis",
    "🇱🇨": "Saint Lucia",
    "🇲🇫": "Saint Martin",
    "🇻🇨": "Saint Vincent and the Grenadines",
    "🇼🇸": "Samoa",
    "🇸🇲": "San Marino",
    "🇸🇹": "São Tomé and Príncipe",
    "🇸🇦": "Saudi Arabia",
    "🇸🇳": "Senegal",
    "🇷🇸": "Serbia",
    "🇸🇨": "Seychelles",
    "🇸🇱": "Sierra Leone",
    "🇸🇬": "Singapore",
    "🇸🇰": "Slovakia",
    "🇸🇮": "Slovenia",
    "🇸🇧": "Solomon Islands",
    "🇸🇴": "Somalia",
    "🇿🇦": "South Africa",
    "🇪🇸": "Spain",
    "🇱🇰": "Sri Lanka",
    "🇸🇩": "Sudan",
    "🇸🇷": "Suriname",
    "🇸🇪": "Sweden",
    "🇨🇭": "Switzerland",
    "🇸🇾": "Syria",
    "🇹🇼": "Taiwan",
    "🇹🇯": "Tajikistan",
    "🇹🇿": "Tanzania",
    "🇹🇭": "Thailand",
    "🇹🇱": ["Timor-Leste", "timor leste"],
    "🇹🇬": "Togo",
    "🇹🇴": "Tonga",
    "🇹🇹": "Trinidad and Tobago",
    "🇹🇳": "Tunisia",
    "🇹🇷": "Turkey",
    "🇹🇲": "Turkmenistan",
    "🇹🇻": "Tuvalu",
    "🇺🇬": "Uganda",
    "🇺🇦": "Ukraine",
    "🇦🇪": ["United Arab Emirates", "UAE"],
    "🇬🇧": ["United Kingdom", "UK"],
    "🇺🇸": ["United States", "USA"],
    "🇺🇾": "Uruguay",
    "🇺🇿": "Uzbekistan",
    "🇻🇺": "Vanuatu",
    "🇻🇦": ["Vatican City", "Holy See"],
    "🇻🇪": "Venezuela",
    "🇻🇳": "Vietnam",
    "🇾🇪": "Yemen",
    "🇿🇲": "Zambia",
    "🇿🇼": "Zimbabwe",
}

# noinspection SpellCheckingInspection
VALID_CODE_LANGUAGES = [
    "abap",
    "aes",
    "apex",
    "awk",
    "azcli",
    "bat",
    "bicep",
    "c",
    "cameligo",
    "cjam",
    "clojure",
    "cobol",
    "coffeescript",
    "cow",
    "cpp",
    "crystal",
    "csharp",
    "csp",
    "css",
    "d",
    "dart",
    "dash",
    "dockerfile",
    "dragon",
    "ecl",
    "elixir",
    "emacs",
    "erlang",
    "fortran",
    "fsharp",
    "go",
    "golfscript",
    "graphql",
    "groovy",
    "handlebars",
    "haskell",
    "hcl",
    "html",
    "ini",
    "java",
    "javascript",
    "jelly",
    "json",
    "julia",
    "kotlin",
    "less",
    "lexon",
    "liquid",
    "lisp",
    "lua",
    "lolcode",
    "m3",
    "markdown",
    "mips",
    "msdax",
    "mysql",
    "sql",
    "objective-c",
    "nasm",
    "nasm64",
    "nim",
    "ocaml",
    "octave",
    "osabie",
    "paradoc",
    "pascal",
    "pascaligo",
    "perl",
    "pgsql",
    "php",
    "plaintext",
    "ponylang",
    "postiats",
    "powerquery",
    "powershell",
    "prolog",
    "pure",
    "pug",
    "py",
    "pyth",
    "python",
    "python2",
    "qsharp",
    "r",
    "raku",
    "razor",
    "redis",
    "redshift",
    "restructuredtext",
    "rockstar",
    "ruby",
    "rust",
    "sb",
    "scala",
    "scheme",
    "scss",
    "shell",
    "sol",
    "sparql",
    "st",
    "swift",
    "systemverilog",
    "tcl",
    "twig",
    "typescript",
    "vb",
    "verilog",
    "vlang",
    "xml",
    "yaml",
    "yeethon",
    "zig",
]

TRIVIA_CATEGORIES = [
    {"id": 9, "name": "General Knowledge"},
    {"id": 10, "name": "Entertainment: Books"},
    {"id": 11, "name": "Entertainment: Film"},
    {"id": 12, "name": "Entertainment: Music"},
    {"id": 13, "name": "Entertainment: Musicals & Theatres"},
    {"id": 14, "name": "Entertainment: Television"},
    {"id": 15, "name": "Entertainment: Video Games"},
    {"id": 16, "name": "Entertainment: Board Games"},
    {"id": 17, "name": "Science & Nature"},
    {"id": 18, "name": "Science: Computers"},
    {"id": 19, "name": "Science: Mathematics"},
    {"id": 20, "name": "Mythology"},
    {"id": 21, "name": "Sports"},
    {"id": 22, "name": "Geography"},
    {"id": 23, "name": "History"},
    {"id": 24, "name": "Politics"},
    {"id": 25, "name": "Art"},
    {"id": 26, "name": "Celebrities"},
    {"id": 27, "name": "Animals"},
    {"id": 28, "name": "Vehicles"},
    {"id": 29, "name": "Entertainment: Comics"},
    {"id": 30, "name": "Science: Gadgets"},
    {"id": 31, "name": "Entertainment: Japanese Anime & Manga"},
    {"id": 32, "name": "Entertainment: Cartoon & Animations"},
]
