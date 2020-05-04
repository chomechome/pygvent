import collections


class Color:

    class RGBA(collections.namedtuple('RGBA', 'red green blue alpha')):
        __slots__ = ()

        def __new__(cls, red: int, green: int, blue: int, alpha: int = 255):
            assert 0 <= red <= 255
            assert 0 <= green <= 255
            assert 0 <= blue <= 255
            assert 0 <= alpha <= 255

            return super().__new__(cls, red, green, blue, alpha)

    AERO_BLUE = RGBA(201, 255, 229)
    AFRICAN_VIOLET = RGBA(178, 132, 190)
    AIR_FORCE_BLUE = RGBA(93, 138, 168)
    AIR_SUPERIORITY_BLUE = RGBA(114, 160, 193)
    ALABAMA_CRIMSON = RGBA(175, 0, 42)
    ALICE_BLUE = RGBA(240, 248, 255)
    ALIZARIN_CRIMSON = RGBA(227, 38, 54)
    ALLOY_ORANGE = RGBA(196, 98, 16)
    ALMOND = RGBA(239, 222, 205)
    AMARANTH = RGBA(229, 43, 80)
    AMARANTH_PINK = RGBA(241, 156, 187)
    AMARANTH_PURPLE = RGBA(171, 39, 79)
    AMAZON = RGBA(59, 122, 87)
    AMBER = RGBA(255, 191, 0)
    SAE = RGBA(255, 126, 0)
    AMERICAN_ROSE = RGBA(255, 3, 62)
    AMETHYST = RGBA(153, 102, 204)
    ANDROID_GREEN = RGBA(164, 198, 57)
    ANTI_FLASH_WHITE = RGBA(242, 243, 244)
    ANTIQUE_BRASS = RGBA(205, 149, 117)
    ANTIQUE_BRONZE = RGBA(102, 93, 30)
    ANTIQUE_FUCHSIA = RGBA(145, 92, 131)
    ANTIQUE_RUBY = RGBA(132, 27, 45)
    ANTIQUE_WHITE = RGBA(250, 235, 215)
    AO = RGBA(0, 128, 0)
    APPLE_GREEN = RGBA(141, 182, 0)
    APRICOT = RGBA(251, 206, 177)
    AQUA = RGBA(0, 255, 255)
    AQUAMARINE = RGBA(127, 255, 212)
    ARMY_GREEN = RGBA(75, 83, 32)
    ARSENIC = RGBA(59, 68, 75)
    ARTICHOKE = RGBA(143, 151, 121)
    ARYLIDE_YELLOW = RGBA(233, 214, 107)
    ASH_GREY = RGBA(178, 190, 181)
    ASPARAGUS = RGBA(135, 169, 107)
    ATOMIC_TANGERINE = RGBA(255, 153, 102)
    AUBURN = RGBA(165, 42, 42)
    AUREOLIN = RGBA(253, 238, 0)
    AUROMETALSAURUS = RGBA(110, 127, 128)
    AVOCADO = RGBA(86, 130, 3)
    AZURE = RGBA(0, 127, 255)
    AZURE_MIST = RGBA(240, 255, 255)
    BABY_BLUE = RGBA(137, 207, 240)
    BABY_BLUE_EYES = RGBA(161, 202, 241)
    BABY_PINK = RGBA(244, 194, 194)
    BABY_POWDER = RGBA(254, 254, 250)
    BAKER_MILLER_PINK = RGBA(255, 145, 175)
    BALL_BLUE = RGBA(33, 171, 205)
    BANANA_MANIA = RGBA(250, 231, 181)
    BANANA_YELLOW = RGBA(255, 225, 53)
    BANGLADESH_GREEN = RGBA(0, 106, 78)
    BARBIE_PINK = RGBA(224, 33, 138)
    BARN_RED = RGBA(124, 10, 2)
    BATTLESHIP_GREY = RGBA(132, 132, 130)
    BAZAAR = RGBA(152, 119, 123)
    BEAU_BLUE = RGBA(188, 212, 230)
    BRIGHT_LILAC = RGBA(216, 145, 239)
    BEAVER = RGBA(159, 129, 112)
    BEIGE = RGBA(245, 245, 220)
    BISQUE = RGBA(255, 228, 196)
    BISTRE = RGBA(61, 43, 31)
    BISTRE_BROWN = RGBA(150, 113, 23)
    BITTER_LEMON = RGBA(202, 224, 13)
    BITTER_LIME = RGBA(100, 140, 17)
    BITTERSWEET = RGBA(254, 111, 94)
    BITTERSWEET_SHIMMER = RGBA(191, 79, 81)
    BLACK = RGBA(0, 0, 0)
    BLACK_BEAN = RGBA(61, 12, 2)
    BLACK_LEATHER_JACKET = RGBA(37, 53, 41)
    BLACK_OLIVE = RGBA(59, 60, 54)
    BLANCHED_ALMOND = RGBA(255, 235, 205)
    BLAST_OFF_BRONZE = RGBA(165, 113, 100)
    BLEU_DE_FRANCE = RGBA(49, 140, 231)
    BLIZZARD_BLUE = RGBA(172, 229, 238)
    BLOND = RGBA(250, 240, 190)
    BLUE = RGBA(0, 0, 255)
    BLUE_BELL = RGBA(162, 162, 208)
    BLUE_GRAY = RGBA(102, 153, 204)
    BLUE_GREEN = RGBA(13, 152, 186)
    BLUE_SAPPHIRE = RGBA(18, 97, 128)
    BLUE_VIOLET = RGBA(138, 43, 226)
    BLUE_YONDER = RGBA(80, 114, 167)
    BLUEBERRY = RGBA(79, 134, 247)
    BLUEBONNET = RGBA(28, 28, 240)
    BLUSH = RGBA(222, 93, 131)
    BOLE = RGBA(121, 68, 59)
    BONDI_BLUE = RGBA(0, 149, 182)
    BONE = RGBA(227, 218, 201)
    BOSTON_UNIVERSITY_RED = RGBA(204, 0, 0)
    BOTTLE_GREEN = RGBA(0, 106, 78)
    BOYSENBERRY = RGBA(135, 50, 96)
    BRANDEIS_BLUE = RGBA(0, 112, 255)
    BRASS = RGBA(181, 166, 66)
    BRICK_RED = RGBA(203, 65, 84)
    BRIGHT_CERULEAN = RGBA(29, 172, 214)
    BRIGHT_GREEN = RGBA(102, 255, 0)
    BRIGHT_LAVENDER = RGBA(191, 148, 228)
    BRIGHT_MAROON = RGBA(195, 33, 72)
    BRIGHT_NAVY_BLUE = RGBA(25, 116, 210)
    BRIGHT_PINK = RGBA(255, 0, 127)
    BRIGHT_TURQUOISE = RGBA(8, 232, 222)
    BRIGHT_UBE = RGBA(209, 159, 232)
    BRILLIANT_LAVENDER = RGBA(244, 187, 255)
    BRILLIANT_ROSE = RGBA(255, 85, 163)
    BRINK_PINK = RGBA(251, 96, 127)
    BRITISH_RACING_GREEN = RGBA(0, 66, 37)
    BRONZE = RGBA(205, 127, 50)
    BRONZE_YELLOW = RGBA(115, 112, 0)
    BROWN = RGBA(165, 42, 42)
    BROWN_NOSE = RGBA(107, 68, 35)
    BRUNSWICK_GREEN = RGBA(27, 77, 62)
    BUBBLE_GUM = RGBA(255, 193, 204)
    BUBBLES = RGBA(231, 254, 255)
    BUD_GREEN = RGBA(123, 182, 97)
    BUFF = RGBA(240, 220, 130)
    BULGARIAN_ROSE = RGBA(72, 6, 7)
    BURGUNDY = RGBA(128, 0, 32)
    BURLYWOOD = RGBA(222, 184, 135)
    BURNT_ORANGE = RGBA(204, 85, 0)
    BURNT_SIENNA = RGBA(233, 116, 81)
    BURNT_UMBER = RGBA(138, 51, 36)
    BYZANTINE = RGBA(189, 51, 164)
    BYZANTIUM = RGBA(112, 41, 99)
    CADET = RGBA(83, 104, 114)
    CADET_BLUE = RGBA(95, 158, 160)
    CADET_GREY = RGBA(145, 163, 176)
    CADMIUM_GREEN = RGBA(0, 107, 60)
    CADMIUM_ORANGE = RGBA(237, 135, 45)
    CADMIUM_RED = RGBA(227, 0, 34)
    CADMIUM_YELLOW = RGBA(255, 246, 0)
    CAL_POLY_GREEN = RGBA(30, 77, 43)
    CAMBRIDGE_BLUE = RGBA(163, 193, 173)
    CAMEL = RGBA(193, 154, 107)
    CAMEO_PINK = RGBA(239, 187, 204)
    CAMOUFLAGE_GREEN = RGBA(120, 134, 107)
    CANARY_YELLOW = RGBA(255, 239, 0)
    CANDY_APPLE_RED = RGBA(255, 8, 0)
    CANDY_PINK = RGBA(228, 113, 122)
    CAPRI = RGBA(0, 191, 255)
    CAPUT_MORTUUM = RGBA(89, 39, 32)
    CARDINAL = RGBA(196, 30, 58)
    CARIBBEAN_GREEN = RGBA(0, 204, 153)
    CARMINE = RGBA(150, 0, 24)
    CARMINE_PINK = RGBA(235, 76, 66)
    CARMINE_RED = RGBA(255, 0, 56)
    CARNATION_PINK = RGBA(255, 166, 201)
    CARNELIAN = RGBA(179, 27, 27)
    CAROLINA_BLUE = RGBA(153, 186, 221)
    CARROT_ORANGE = RGBA(237, 145, 33)
    CASTLETON_GREEN = RGBA(0, 86, 63)
    CATALINA_BLUE = RGBA(6, 42, 120)
    CATAWBA = RGBA(112, 54, 66)
    CEDAR_CHEST = RGBA(201, 90, 73)
    CEIL = RGBA(146, 161, 207)
    CELADON = RGBA(172, 225, 175)
    CELADON_BLUE = RGBA(0, 123, 167)
    CELADON_GREEN = RGBA(47, 132, 124)
    CELESTE = RGBA(178, 255, 255)
    CELESTIAL_BLUE = RGBA(73, 151, 208)
    CERISE = RGBA(222, 49, 99)
    CERISE_PINK = RGBA(236, 59, 131)
    CERULEAN = RGBA(0, 123, 167)
    CERULEAN_BLUE = RGBA(42, 82, 190)
    CERULEAN_FROST = RGBA(109, 155, 195)
    CG_BLUE = RGBA(0, 122, 165)
    CG_RED = RGBA(224, 60, 49)
    CHAMOISEE = RGBA(160, 120, 90)
    CHAMPAGNE = RGBA(247, 231, 206)
    CHARCOAL = RGBA(54, 69, 79)
    CHARLESTON_GREEN = RGBA(35, 43, 43)
    CHARM_PINK = RGBA(230, 143, 172)
    CHARTREUSE = RGBA(127, 255, 0)
    CHERRY = RGBA(222, 49, 99)
    CHERRY_BLOSSOM_PINK = RGBA(255, 183, 197)
    CHESTNUT = RGBA(149, 69, 53)
    CHINA_PINK = RGBA(222, 111, 161)
    CHINA_ROSE = RGBA(168, 81, 110)
    CHINESE_RED = RGBA(170, 56, 30)
    CHINESE_VIOLET = RGBA(133, 96, 136)
    CHOCOLATE = RGBA(210, 105, 30)
    CHROME_YELLOW = RGBA(255, 167, 0)
    CINEREOUS = RGBA(152, 129, 123)
    CINNABAR = RGBA(227, 66, 52)
    CINNAMON = RGBA(210, 105, 30)
    CITRINE = RGBA(228, 208, 10)
    CITRON = RGBA(159, 169, 31)
    CLARET = RGBA(127, 23, 52)
    CLASSIC_ROSE = RGBA(251, 204, 231)
    COAL = RGBA(124, 185, 232)
    COBALT = RGBA(0, 71, 171)
    COCOA_BROWN = RGBA(210, 105, 30)
    COCONUT = RGBA(150, 90, 62)
    COFFEE = RGBA(111, 78, 55)
    COLUMBIA_BLUE = RGBA(155, 221, 255)
    CONGO_PINK = RGBA(248, 131, 121)
    COOL_BLACK = RGBA(0, 46, 99)
    COOL_GREY = RGBA(140, 146, 172)
    COPPER = RGBA(184, 115, 51)
    COPPER_PENNY = RGBA(173, 111, 105)
    COPPER_RED = RGBA(203, 109, 81)
    COPPER_ROSE = RGBA(153, 102, 102)
    COQUELICOT = RGBA(255, 56, 0)
    CORAL = RGBA(255, 127, 80)
    CORAL_PINK = RGBA(248, 131, 121)
    CORAL_RED = RGBA(255, 64, 64)
    CORDOVAN = RGBA(137, 63, 69)
    CORN = RGBA(251, 236, 93)
    CORNELL_RED = RGBA(179, 27, 27)
    CORNFLOWER_BLUE = RGBA(100, 149, 237)
    CORNSILK = RGBA(255, 248, 220)
    COSMIC_LATTE = RGBA(255, 248, 231)
    COTTON_CANDY = RGBA(255, 188, 217)
    CREAM = RGBA(255, 253, 208)
    CRIMSON = RGBA(220, 20, 60)
    CRIMSON_GLORY = RGBA(190, 0, 50)
    CYAN = RGBA(0, 255, 255)
    CYBER_GRAPE = RGBA(88, 66, 124)
    CYBER_YELLOW = RGBA(255, 211, 0)
    DAFFODIL = RGBA(255, 255, 49)
    DANDELION = RGBA(240, 225, 48)
    DARK_BLUE = RGBA(0, 0, 139)
    DARK_BLUE_GRAY = RGBA(102, 102, 153)
    DARK_BROWN = RGBA(101, 67, 33)
    DARK_BYZANTIUM = RGBA(93, 57, 84)
    DARK_CANDY_APPLE_RED = RGBA(164, 0, 0)
    DARK_CERULEAN = RGBA(8, 69, 126)
    DARK_CHESTNUT = RGBA(152, 105, 96)
    DARK_CORAL = RGBA(205, 91, 69)
    DARK_CYAN = RGBA(0, 139, 139)
    DARK_ELECTRIC_BLUE = RGBA(83, 104, 120)
    DARK_GOLDENROD = RGBA(184, 134, 11)
    DARK_GRAY = RGBA(169, 169, 169)
    DARK_GREEN = RGBA(1, 50, 32)
    DARK_IMPERIAL_BLUE = RGBA(0, 65, 106)
    DARK_JUNGLE_GREEN = RGBA(26, 36, 33)
    DARK_KHAKI = RGBA(189, 183, 107)
    DARK_LAVA = RGBA(72, 60, 50)
    DARK_LAVENDER = RGBA(115, 79, 150)
    DARK_LIVER = RGBA(83, 75, 79)
    DARK_MAGENTA = RGBA(139, 0, 139)
    DARK_MIDNIGHT_BLUE = RGBA(0, 51, 102)
    DARK_MOSS_GREEN = RGBA(74, 93, 35)
    DARK_OLIVE_GREEN = RGBA(85, 107, 47)
    DARK_ORANGE = RGBA(255, 140, 0)
    DARK_ORCHID = RGBA(153, 50, 204)
    DARK_PASTEL_BLUE = RGBA(119, 158, 203)
    DARK_PASTEL_GREEN = RGBA(3, 192, 60)
    DARK_PASTEL_PURPLE = RGBA(150, 111, 214)
    DARK_PASTEL_RED = RGBA(194, 59, 34)
    DARK_PINK = RGBA(231, 84, 128)
    DARK_POWDER_BLUE = RGBA(0, 51, 153)
    DARK_PUCE = RGBA(79, 58, 60)
    DARK_RASPBERRY = RGBA(135, 38, 87)
    DARK_RED = RGBA(139, 0, 0)
    DARK_SALMON = RGBA(233, 150, 122)
    DARK_SCARLET = RGBA(86, 3, 25)
    DARK_SEA_GREEN = RGBA(143, 188, 143)
    DARK_SIENNA = RGBA(60, 20, 20)
    DARK_SKY_BLUE = RGBA(140, 190, 214)
    DARK_SLATE_BLUE = RGBA(72, 61, 139)
    DARK_SLATE_GRAY = RGBA(47, 79, 79)
    DARK_SPRING_GREEN = RGBA(23, 114, 69)
    DARK_TAN = RGBA(145, 129, 81)
    DARK_TANGERINE = RGBA(255, 168, 18)
    DARK_TAUPE = RGBA(72, 60, 50)
    DARK_TERRA_COTTA = RGBA(204, 78, 92)
    DARK_TURQUOISE = RGBA(0, 206, 209)
    DARK_VANILLA = RGBA(209, 190, 168)
    DARK_VIOLET = RGBA(148, 0, 211)
    DARK_YELLOW = RGBA(155, 135, 12)
    DARTMOUTH_GREEN = RGBA(0, 112, 60)
    DAVY_GREY = RGBA(85, 85, 85)
    DEBIAN_RED = RGBA(215, 10, 83)
    DEEP_CARMINE = RGBA(169, 32, 62)
    DEEP_CARMINE_PINK = RGBA(239, 48, 56)
    DEEP_CARROT_ORANGE = RGBA(233, 105, 44)
    DEEP_CERISE = RGBA(218, 50, 135)
    DEEP_CHAMPAGNE = RGBA(250, 214, 165)
    DEEP_CHESTNUT = RGBA(185, 78, 72)
    DEEP_COFFEE = RGBA(112, 66, 65)
    DEEP_FUCHSIA = RGBA(193, 84, 193)
    DEEP_JUNGLE_GREEN = RGBA(0, 75, 73)
    DEEP_LEMON = RGBA(245, 199, 26)
    DEEP_LILAC = RGBA(153, 85, 187)
    DEEP_MAGENTA = RGBA(204, 0, 204)
    DEEP_MAUVE = RGBA(212, 115, 212)
    DEEP_MOSS_GREEN = RGBA(53, 94, 59)
    DEEP_PEACH = RGBA(255, 203, 164)
    DEEP_PINK = RGBA(255, 20, 147)
    DEEP_PUCE = RGBA(169, 92, 104)
    DEEP_RUBY = RGBA(132, 63, 91)
    DEEP_SAFFRON = RGBA(255, 153, 51)
    DEEP_SKY_BLUE = RGBA(0, 191, 255)
    DEEP_SPACE_SPARKLE = RGBA(74, 100, 108)
    DEEP_TAUPE = RGBA(126, 94, 96)
    DEEP_TUSCAN_RED = RGBA(102, 66, 77)
    DEER = RGBA(186, 135, 89)
    DENIM = RGBA(21, 96, 189)
    DESERT = RGBA(193, 154, 107)
    DESERT_SAND = RGBA(237, 201, 175)
    DESIRE = RGBA(234, 60, 83)
    DIAMOND = RGBA(185, 242, 255)
    DIM_GRAY = RGBA(105, 105, 105)
    DIRT = RGBA(155, 118, 83)
    DODGER_BLUE = RGBA(30, 144, 255)
    DOGWOOD_ROSE = RGBA(215, 24, 104)
    DOLLAR_BILL = RGBA(133, 187, 101)
    DONKEY_BROWN = RGBA(102, 76, 40)
    DRAB = RGBA(150, 113, 23)
    DUKE_BLUE = RGBA(0, 0, 156)
    DUST_STORM = RGBA(229, 204, 201)
    DUTCH_WHITE = RGBA(239, 223, 187)
    EARTH_YELLOW = RGBA(225, 169, 95)
    EBONY = RGBA(85, 93, 80)
    ECRU = RGBA(194, 178, 128)
    EERIE_BLACK = RGBA(27, 27, 27)
    EGGPLANT = RGBA(97, 64, 81)
    EGGSHELL = RGBA(240, 234, 214)
    EGYPTIAN_BLUE = RGBA(16, 52, 166)
    ELECTRIC_BLUE = RGBA(125, 249, 255)
    ELECTRIC_CRIMSON = RGBA(255, 0, 63)
    ELECTRIC_CYAN = RGBA(0, 255, 255)
    ELECTRIC_GREEN = RGBA(0, 255, 0)
    ELECTRIC_INDIGO = RGBA(111, 0, 255)
    ELECTRIC_LAVENDER = RGBA(244, 187, 255)
    ELECTRIC_LIME = RGBA(204, 255, 0)
    ELECTRIC_PURPLE = RGBA(191, 0, 255)
    ELECTRIC_ULTRAMARINE = RGBA(63, 0, 255)
    ELECTRIC_VIOLET = RGBA(143, 0, 255)
    ELECTRIC_YELLOW = RGBA(255, 255, 0)
    EMERALD = RGBA(80, 200, 120)
    EMINENCE = RGBA(108, 48, 130)
    ENGLISH_GREEN = RGBA(27, 77, 62)
    ENGLISH_LAVENDER = RGBA(180, 131, 149)
    ENGLISH_RED = RGBA(171, 75, 82)
    ENGLISH_VIOLET = RGBA(86, 60, 92)
    ETON_BLUE = RGBA(150, 200, 162)
    EUCALYPTUS = RGBA(68, 215, 168)
    FALLOW = RGBA(193, 154, 107)
    FALU_RED = RGBA(128, 24, 24)
    FANDANGO = RGBA(181, 51, 137)
    FANDANGO_PINK = RGBA(222, 82, 133)
    FASHION_FUCHSIA = RGBA(244, 0, 161)
    FAWN = RGBA(229, 170, 112)
    FELDGRAU = RGBA(77, 93, 83)
    FELDSPAR = RGBA(253, 213, 177)
    FERN_GREEN = RGBA(79, 121, 66)
    FERRARI_RED = RGBA(255, 40, 0)
    FIELD_DRAB = RGBA(108, 84, 30)
    FIREBRICK = RGBA(178, 34, 34)
    FIRE_ENGINE_RED = RGBA(206, 32, 41)
    FLAME = RGBA(226, 88, 34)
    FLAMINGO_PINK = RGBA(252, 142, 172)
    FLATTERY = RGBA(107, 68, 35)
    FLAVESCENT = RGBA(247, 233, 142)
    FLAX = RGBA(238, 220, 130)
    FLIRT = RGBA(162, 0, 109)
    FLORAL_WHITE = RGBA(255, 250, 240)
    FLUORESCENT_ORANGE = RGBA(255, 191, 0)
    FLUORESCENT_PINK = RGBA(255, 20, 147)
    FLUORESCENT_YELLOW = RGBA(204, 255, 0)
    FOLLY = RGBA(255, 0, 79)
    FOREST_GREEN = RGBA(34, 139, 34)
    FRENCH_BEIGE = RGBA(166, 123, 91)
    FRENCH_BISTRE = RGBA(133, 109, 77)
    FRENCH_BLUE = RGBA(0, 114, 187)
    FRENCH_FUCHSIA = RGBA(253, 63, 146)
    FRENCH_LILAC = RGBA(134, 96, 142)
    FRENCH_LIME = RGBA(158, 253, 56)
    FRENCH_MAUVE = RGBA(212, 115, 212)
    FRENCH_PINK = RGBA(253, 108, 158)
    FRENCH_PUCE = RGBA(78, 22, 9)
    FRENCH_RASPBERRY = RGBA(199, 44, 72)
    FRENCH_ROSE = RGBA(246, 74, 138)
    FRENCH_SKY_BLUE = RGBA(119, 181, 254)
    FRENCH_WINE = RGBA(172, 30, 68)
    FRESH_AIR = RGBA(166, 231, 255)
    FUCHSIA = RGBA(255, 0, 255)
    FUCHSIA_PINK = RGBA(255, 119, 255)
    FUCHSIA_PURPLE = RGBA(204, 57, 123)
    FUCHSIA_ROSE = RGBA(199, 67, 117)
    FULVOUS = RGBA(228, 132, 0)
    FUZZY_WUZZY = RGBA(204, 102, 102)
    GAINSBORO = RGBA(220, 220, 220)
    GAMBOGE = RGBA(228, 155, 15)
    GENERIC_VIRIDIAN = RGBA(0, 127, 102)
    GHOST_WHITE = RGBA(248, 248, 255)
    GIANTS_ORANGE = RGBA(254, 90, 29)
    GINGER = RGBA(176, 101, 0)
    GLAUCOUS = RGBA(96, 130, 182)
    GLITTER = RGBA(230, 232, 250)
    GO_GREEN = RGBA(0, 171, 102)
    GOLD = RGBA(255, 215, 0)
    GOLD_FUSION = RGBA(133, 117, 78)
    GOLDEN_BROWN = RGBA(153, 101, 21)
    GOLDEN_POPPY = RGBA(252, 194, 0)
    GOLDEN_YELLOW = RGBA(255, 223, 0)
    GOLDENROD = RGBA(218, 165, 32)
    GRANNY_SMITH_APPLE = RGBA(168, 228, 160)
    GRAPE = RGBA(111, 45, 168)
    GRAY = RGBA(128, 128, 128)
    GRAY_ASPARAGUS = RGBA(70, 89, 69)
    GRAY_BLUE = RGBA(140, 146, 172)
    GREEN = RGBA(0, 255, 0)
    GREEN_YELLOW = RGBA(173, 255, 47)
    GRULLO = RGBA(169, 154, 134)
    GUPPIE_GREEN = RGBA(0, 255, 127)
    HAN_BLUE = RGBA(68, 108, 207)
    HAN_PURPLE = RGBA(82, 24, 250)
    HANSA_YELLOW = RGBA(233, 214, 107)
    HARLEQUIN = RGBA(63, 255, 0)
    HARVARD_CRIMSON = RGBA(201, 0, 22)
    HARVEST_GOLD = RGBA(218, 145, 0)
    HEART_GOLD = RGBA(128, 128, 0)
    HELIOTROPE = RGBA(223, 115, 255)
    HELIOTROPE_GRAY = RGBA(170, 152, 169)
    HOLLYWOOD_CERISE = RGBA(244, 0, 161)
    HONEYDEW = RGBA(240, 255, 240)
    HONOLULU_BLUE = RGBA(0, 109, 176)
    HOOKER_GREEN = RGBA(73, 121, 107)
    HOT_MAGENTA = RGBA(255, 29, 206)
    HOT_PINK = RGBA(255, 105, 180)
    HUNTER_GREEN = RGBA(53, 94, 59)
    ICEBERG = RGBA(113, 166, 210)
    ICTERINE = RGBA(252, 247, 94)
    ILLUMINATING_EMERALD = RGBA(49, 145, 119)
    IMPERIAL = RGBA(96, 47, 107)
    IMPERIAL_BLUE = RGBA(0, 35, 149)
    IMPERIAL_PURPLE = RGBA(102, 2, 60)
    IMPERIAL_RED = RGBA(237, 41, 57)
    INCHWORM = RGBA(178, 236, 93)
    INDEPENDENCE = RGBA(76, 81, 109)
    INDIA_GREEN = RGBA(19, 136, 8)
    INDIAN_RED = RGBA(205, 92, 92)
    INDIAN_YELLOW = RGBA(227, 168, 87)
    INDIGO = RGBA(75, 0, 130)
    INTERNATIONAL_KLEIN_BLUE = RGBA(0, 47, 167)
    INTERNATIONAL_ORANGE = RGBA(255, 79, 0)
    IRIS = RGBA(90, 79, 207)
    IRRESISTIBLE = RGBA(179, 68, 108)
    ISABELLINE = RGBA(244, 240, 236)
    ISLAMIC_GREEN = RGBA(0, 144, 0)
    ITALIAN_SKY_BLUE = RGBA(178, 255, 255)
    IVORY = RGBA(255, 255, 240)
    JADE = RGBA(0, 168, 107)
    JAPANESE_CARMINE = RGBA(157, 41, 51)
    JAPANESE_INDIGO = RGBA(38, 67, 72)
    JAPANESE_VIOLET = RGBA(91, 50, 86)
    JASMINE = RGBA(248, 222, 126)
    JASPER = RGBA(215, 59, 62)
    JAZZBERRY_JAM = RGBA(165, 11, 94)
    JELLY_BEAN = RGBA(218, 97, 78)
    JET = RGBA(52, 52, 52)
    JONQUIL = RGBA(244, 202, 22)
    JORDY_BLUE = RGBA(138, 185, 241)
    JUNE_BUD = RGBA(189, 218, 87)
    JUNGLE_GREEN = RGBA(41, 171, 135)
    KELLY_GREEN = RGBA(76, 187, 23)
    KENYAN_COPPER = RGBA(124, 28, 5)
    KEPPEL = RGBA(58, 176, 158)
    KHAKI = RGBA(195, 176, 145)
    KOBE = RGBA(136, 45, 23)
    KOBI = RGBA(231, 159, 196)
    KOMBU_GREEN = RGBA(53, 66, 48)
    KU_CRIMSON = RGBA(232, 0, 13)
    LA_SALLE_GREEN = RGBA(8, 120, 48)
    LANGUID_LAVENDER = RGBA(214, 202, 221)
    LAPIS_LAZULI = RGBA(38, 97, 156)
    LASER_LEMON = RGBA(255, 255, 102)
    LAUREL_GREEN = RGBA(169, 186, 157)
    LAVA = RGBA(207, 16, 32)
    LAVENDER = RGBA(230, 230, 250)
    LAVENDER_BLUE = RGBA(204, 204, 255)
    LAVENDER_BLUSH = RGBA(255, 240, 245)
    LAVENDER_GRAY = RGBA(196, 195, 208)
    LAVENDER_INDIGO = RGBA(148, 87, 235)
    LAVENDER_MAGENTA = RGBA(238, 130, 238)
    LAVENDER_MIST = RGBA(230, 230, 250)
    LAVENDER_PINK = RGBA(251, 174, 210)
    LAVENDER_PURPLE = RGBA(150, 123, 182)
    LAVENDER_ROSE = RGBA(251, 160, 227)
    LAWN_GREEN = RGBA(124, 252, 0)
    LEMON = RGBA(255, 247, 0)
    LEMON_CHIFFON = RGBA(255, 250, 205)
    LEMON_CURRY = RGBA(204, 160, 29)
    LEMON_GLACIER = RGBA(253, 255, 0)
    LEMON_LIME = RGBA(227, 255, 0)
    LEMON_MERINGUE = RGBA(246, 234, 190)
    LEMON_YELLOW = RGBA(255, 244, 79)
    LIBERTY = RGBA(84, 90, 167)
    LICORICE = RGBA(26, 17, 16)
    LIGHT_APRICOT = RGBA(253, 213, 177)
    LIGHT_BLUE = RGBA(173, 216, 230)
    LIGHT_BROWN = RGBA(181, 101, 29)
    LIGHT_CARMINE_PINK = RGBA(230, 103, 113)
    LIGHT_CORAL = RGBA(240, 128, 128)
    LIGHT_CORNFLOWER_BLUE = RGBA(147, 204, 234)
    LIGHT_CRIMSON = RGBA(245, 105, 145)
    LIGHT_CYAN = RGBA(224, 255, 255)
    LIGHT_DEEP_PINK = RGBA(255, 92, 205)
    LIGHT_FUCHSIA_PINK = RGBA(249, 132, 239)
    LIGHT_GOLDENROD_YELLOW = RGBA(250, 250, 210)
    LIGHT_GRAY = RGBA(211, 211, 211)
    LIGHT_GREEN = RGBA(144, 238, 144)
    LIGHT_HOT_PINK = RGBA(255, 179, 222)
    LIGHT_KHAKI = RGBA(240, 230, 140)
    LIGHT_MEDIUM_ORCHID = RGBA(211, 155, 203)
    LIGHT_MOSS_GREEN = RGBA(173, 223, 173)
    LIGHT_ORCHID = RGBA(230, 168, 215)
    LIGHT_PASTEL_PURPLE = RGBA(177, 156, 217)
    LIGHT_PINK = RGBA(255, 182, 193)
    LIGHT_RED_OCHRE = RGBA(233, 116, 81)
    LIGHT_SALMON = RGBA(255, 160, 122)
    LIGHT_SALMON_PINK = RGBA(255, 153, 153)
    LIGHT_SEA_GREEN = RGBA(32, 178, 170)
    LIGHT_SKY_BLUE = RGBA(135, 206, 250)
    LIGHT_SLATE_GRAY = RGBA(119, 136, 153)
    LIGHT_STEEL_BLUE = RGBA(176, 196, 222)
    LIGHT_TAUPE = RGBA(179, 139, 109)
    LIGHT_THULIAN_PINK = RGBA(230, 143, 172)
    LIGHT_YELLOW = RGBA(255, 255, 224)
    LILAC = RGBA(200, 162, 200)
    LIME = RGBA(191, 255, 0)
    LIME_GREEN = RGBA(50, 205, 50)
    LIMERICK = RGBA(157, 194, 9)
    LINCOLN_GREEN = RGBA(25, 89, 5)
    LINEN = RGBA(250, 240, 230)
    LION = RGBA(193, 154, 107)
    LISERAN_PURPLE = RGBA(222, 111, 161)
    LITTLE_BOY_BLUE = RGBA(108, 160, 220)
    LIVER = RGBA(103, 76, 71)
    LIVER_CHESTNUT = RGBA(152, 116, 86)
    LIVID = RGBA(102, 153, 204)
    LUMBER = RGBA(255, 228, 205)
    LUST = RGBA(230, 32, 32)
    MAGENTA = RGBA(255, 0, 255)
    MAGENTA_HAZE = RGBA(159, 69, 118)
    MAGIC_MINT = RGBA(170, 240, 209)
    MAGNOLIA = RGBA(248, 244, 255)
    MAHOGANY = RGBA(192, 64, 0)
    MAIZE = RGBA(251, 236, 93)
    MAJORELLE_BLUE = RGBA(96, 80, 220)
    MALACHITE = RGBA(11, 218, 81)
    MANATEE = RGBA(151, 154, 170)
    MANGO_TANGO = RGBA(255, 130, 67)
    MANTIS = RGBA(116, 195, 101)
    MARDI_GRAS = RGBA(136, 0, 133)
    MAROON = RGBA(128, 0, 0)
    MAUVE = RGBA(224, 176, 255)
    MAUVE_TAUPE = RGBA(145, 95, 109)
    MAUVELOUS = RGBA(239, 152, 170)
    MAYA_BLUE = RGBA(115, 194, 251)
    MEAT_BROWN = RGBA(229, 183, 59)
    MEDIUM_AQUAMARINE = RGBA(102, 221, 170)
    MEDIUM_BLUE = RGBA(0, 0, 205)
    MEDIUM_CANDY_APPLE_RED = RGBA(226, 6, 44)
    MEDIUM_CARMINE = RGBA(175, 64, 53)
    MEDIUM_CHAMPAGNE = RGBA(243, 229, 171)
    MEDIUM_ELECTRIC_BLUE = RGBA(3, 80, 150)
    MEDIUM_JUNGLE_GREEN = RGBA(28, 53, 45)
    MEDIUM_LAVENDER_MAGENTA = RGBA(221, 160, 221)
    MEDIUM_ORCHID = RGBA(186, 85, 211)
    MEDIUM_PERSIAN_BLUE = RGBA(0, 103, 165)
    MEDIUM_PURPLE = RGBA(147, 112, 219)
    MEDIUM_RED_VIOLET = RGBA(187, 51, 133)
    MEDIUM_RUBY = RGBA(170, 64, 105)
    MEDIUM_SEA_GREEN = RGBA(60, 179, 113)
    MEDIUM_SLATE_BLUE = RGBA(123, 104, 238)
    MEDIUM_SPRING_BUD = RGBA(201, 220, 135)
    MEDIUM_SPRING_GREEN = RGBA(0, 250, 154)
    MEDIUM_SKY_BLUE = RGBA(128, 218, 235)
    MEDIUM_TAUPE = RGBA(103, 76, 71)
    MEDIUM_TURQUOISE = RGBA(72, 209, 204)
    MEDIUM_TUSCAN_RED = RGBA(121, 68, 59)
    MEDIUM_VERMILION = RGBA(217, 96, 59)
    MEDIUM_VIOLET_RED = RGBA(199, 21, 133)
    MELLOW_APRICOT = RGBA(248, 184, 120)
    MELLOW_YELLOW = RGBA(248, 222, 126)
    MELON = RGBA(253, 188, 180)
    METALLIC_SEAWEED = RGBA(10, 126, 140)
    METALLIC_SUNBURST = RGBA(156, 124, 56)
    MEXICAN_PINK = RGBA(228, 0, 124)
    MIDNIGHT_BLUE = RGBA(25, 25, 112)
    MIDNIGHT_GREEN = RGBA(0, 73, 83)
    MIKADO_YELLOW = RGBA(255, 196, 12)
    MINDARO = RGBA(227, 249, 136)
    MINT = RGBA(62, 180, 137)
    MINT_CREAM = RGBA(245, 255, 250)
    MINT_GREEN = RGBA(152, 255, 152)
    MISTY_ROSE = RGBA(255, 228, 225)
    MOCCASIN = RGBA(250, 235, 215)
    MODE_BEIGE = RGBA(150, 113, 23)
    MOONSTONE_BLUE = RGBA(115, 169, 194)
    MORDANT_RED_19 = RGBA(174, 12, 0)
    MOSS_GREEN = RGBA(138, 154, 91)
    MOUNTAIN_MEADOW = RGBA(48, 186, 143)
    MOUNTBATTEN_PINK = RGBA(153, 122, 141)
    MSU_GREEN = RGBA(24, 69, 59)
    MUGHAL_GREEN = RGBA(48, 96, 48)
    MULBERRY = RGBA(197, 75, 140)
    MUSTARD = RGBA(255, 219, 88)
    MYRTLE_GREEN = RGBA(49, 120, 115)
    NADESHIKO_PINK = RGBA(246, 173, 198)
    NAPIER_GREEN = RGBA(42, 128, 0)
    NAPLES_YELLOW = RGBA(250, 218, 94)
    NAVAJO_WHITE = RGBA(255, 222, 173)
    NAVY_BLUE = RGBA(0, 0, 128)
    NAVY_PURPLE = RGBA(148, 87, 235)
    NEON_CARROT = RGBA(255, 163, 67)
    NEON_FUCHSIA = RGBA(254, 65, 100)
    NEON_GREEN = RGBA(57, 255, 20)
    NEW_CAR = RGBA(33, 79, 198)
    NEW_YORK_PINK = RGBA(215, 131, 127)
    NON_PHOTO_BLUE = RGBA(164, 221, 237)
    NYANZA = RGBA(233, 255, 219)
    OCEAN_BOAT_BLUE = RGBA(0, 119, 190)
    OCHRE = RGBA(204, 119, 34)
    OFFICE_GREEN = RGBA(0, 128, 0)
    OLD_BURGUNDY = RGBA(67, 48, 46)
    OLD_GOLD = RGBA(207, 181, 59)
    OLD_HELIOTROPE = RGBA(86, 60, 92)
    OLD_LACE = RGBA(253, 245, 230)
    OLD_LAVENDER = RGBA(121, 104, 120)
    OLD_MAUVE = RGBA(103, 49, 71)
    OLD_MOSS_GREEN = RGBA(134, 126, 54)
    OLD_ROSE = RGBA(192, 128, 129)
    OLD_SILVER = RGBA(132, 132, 130)
    OLIVE = RGBA(128, 128, 0)
    OLIVE_DRAB = RGBA(107, 142, 35)
    OLIVINE = RGBA(154, 185, 115)
    ONYX = RGBA(53, 56, 57)
    OPERA_MAUVE = RGBA(183, 132, 167)
    ORANGE = RGBA(255, 165, 0)
    ORANGE_PEEL = RGBA(255, 159, 0)
    ORANGE_RED = RGBA(255, 69, 0)
    ORCHID = RGBA(218, 112, 214)
    ORCHID_PINK = RGBA(242, 141, 205)
    ORIOLES_ORANGE = RGBA(251, 79, 20)
    OTTER_BROWN = RGBA(101, 67, 33)
    OUTER_SPACE = RGBA(65, 74, 76)
    OUTRAGEOUS_ORANGE = RGBA(255, 110, 74)
    OXFORD_BLUE = RGBA(0, 33, 71)
    OU_CRIMSON_RED = RGBA(153, 0, 0)
    PAKISTAN_GREEN = RGBA(0, 102, 0)
    PALATINATE_BLUE = RGBA(39, 59, 226)
    PALATINATE_PURPLE = RGBA(104, 40, 96)
    PALE_AQUA = RGBA(188, 212, 230)
    PALE_BLUE = RGBA(175, 238, 238)
    PALE_BROWN = RGBA(152, 118, 84)
    PALE_CARMINE = RGBA(175, 64, 53)
    PALE_CERULEAN = RGBA(155, 196, 226)
    PALE_CHESTNUT = RGBA(221, 173, 175)
    PALE_COPPER = RGBA(218, 138, 103)
    PALE_CORNFLOWER_BLUE = RGBA(171, 205, 239)
    PALE_GOLD = RGBA(230, 190, 138)
    PALE_GOLDENROD = RGBA(238, 232, 170)
    PALE_GREEN = RGBA(152, 251, 152)
    PALE_LAVENDER = RGBA(220, 208, 255)
    PALE_MAGENTA = RGBA(249, 132, 229)
    PALE_PINK = RGBA(250, 218, 221)
    PALE_PLUM = RGBA(221, 160, 221)
    PALE_RED_VIOLET = RGBA(219, 112, 147)
    PALE_ROBIN_EGG_BLUE = RGBA(150, 222, 209)
    PALE_SILVER = RGBA(201, 192, 187)
    PALE_SPRING_BUD = RGBA(236, 235, 189)
    PALE_TAUPE = RGBA(188, 152, 126)
    PALE_TURQUOISE = RGBA(175, 238, 238)
    PALE_VIOLET_RED = RGBA(219, 112, 147)
    PANSY_PURPLE = RGBA(120, 24, 74)
    PAOLO_VERONESE_GREEN = RGBA(0, 155, 125)
    PAPAYA_WHIP = RGBA(255, 239, 213)
    PARADISE_PINK = RGBA(230, 62, 98)
    PARIS_GREEN = RGBA(80, 200, 120)
    PASTEL_BLUE = RGBA(174, 198, 207)
    PASTEL_BROWN = RGBA(131, 105, 83)
    PASTEL_GRAY = RGBA(207, 207, 196)
    PASTEL_GREEN = RGBA(119, 221, 119)
    PASTEL_MAGENTA = RGBA(244, 154, 194)
    PASTEL_ORANGE = RGBA(255, 179, 71)
    PASTEL_PINK = RGBA(222, 165, 164)
    PASTEL_PURPLE = RGBA(179, 158, 181)
    PASTEL_RED = RGBA(255, 105, 97)
    PASTEL_VIOLET = RGBA(203, 153, 201)
    PASTEL_YELLOW = RGBA(253, 253, 150)
    PATRIARCH = RGBA(128, 0, 128)
    PAYNE_GREY = RGBA(83, 104, 120)
    PEACH = RGBA(255, 229, 180)
    PEACH_ORANGE = RGBA(255, 204, 153)
    PEACH_PUFF = RGBA(255, 218, 185)
    PEACH_YELLOW = RGBA(250, 223, 173)
    PEAR = RGBA(209, 226, 49)
    PEARL = RGBA(234, 224, 200)
    PEARL_AQUA = RGBA(136, 216, 192)
    PEARLY_PURPLE = RGBA(183, 104, 162)
    PERIDOT = RGBA(230, 226, 0)
    PERIWINKLE = RGBA(204, 204, 255)
    PERSIAN_BLUE = RGBA(28, 57, 187)
    PERSIAN_GREEN = RGBA(0, 166, 147)
    PERSIAN_INDIGO = RGBA(50, 18, 122)
    PERSIAN_ORANGE = RGBA(217, 144, 88)
    PERSIAN_PINK = RGBA(247, 127, 190)
    PERSIAN_PLUM = RGBA(112, 28, 28)
    PERSIAN_RED = RGBA(204, 51, 51)
    PERSIAN_ROSE = RGBA(254, 40, 162)
    PERSIMMON = RGBA(236, 88, 0)
    PERU = RGBA(205, 133, 63)
    PHLOX = RGBA(223, 0, 255)
    PHTHALO_BLUE = RGBA(0, 15, 137)
    PHTHALO_GREEN = RGBA(18, 53, 36)
    PICTON_BLUE = RGBA(69, 177, 232)
    PICTORIAL_CARMINE = RGBA(195, 11, 78)
    PIGGY_PINK = RGBA(253, 221, 230)
    PINE_GREEN = RGBA(1, 121, 111)
    PINK = RGBA(255, 192, 203)
    PINK_LACE = RGBA(255, 221, 244)
    PINK_LAVENDER = RGBA(216, 178, 209)
    PINK_PEARL = RGBA(231, 172, 207)
    PINK_SHERBET = RGBA(247, 143, 167)
    PISTACHIO = RGBA(147, 197, 114)
    PLATINUM = RGBA(229, 228, 226)
    PLUM = RGBA(221, 160, 221)
    POMP_AND_POWER = RGBA(134, 96, 142)
    POPSTAR = RGBA(190, 79, 98)
    PORTLAND_ORANGE = RGBA(255, 90, 54)
    POWDER_BLUE = RGBA(176, 224, 230)
    PRINCETON_ORANGE = RGBA(255, 143, 0)
    PRUNE = RGBA(112, 28, 28)
    PRUSSIAN_BLUE = RGBA(0, 49, 83)
    PSYCHEDELIC_PURPLE = RGBA(223, 0, 255)
    PUCE = RGBA(204, 136, 153)
    PUCE_RED = RGBA(114, 47, 55)
    PULLMAN_BROWN = RGBA(100, 65, 23)
    PUMPKIN = RGBA(255, 117, 24)
    PURPLE = RGBA(128, 0, 128)
    PURPLE_HEART = RGBA(105, 53, 156)
    PURPLE_MOUNTAIN_MAJESTY = RGBA(150, 120, 182)
    PURPLE_NAVY = RGBA(78, 81, 128)
    PURPLE_PIZZAZZ = RGBA(254, 78, 218)
    PURPLE_TAUPE = RGBA(80, 64, 77)
    PURPUREUS = RGBA(154, 78, 174)
    QUARTZ = RGBA(81, 72, 79)
    QUEEN_BLUE = RGBA(67, 107, 149)
    QUEEN_PINK = RGBA(232, 204, 215)
    QUINACRIDONE_MAGENTA = RGBA(142, 58, 89)
    RACKLEY = RGBA(93, 138, 168)
    RADICAL_RED = RGBA(255, 53, 94)
    RAJAH = RGBA(251, 171, 96)
    RASPBERRY = RGBA(227, 11, 93)
    RASPBERRY_GLACE = RGBA(145, 95, 109)
    RASPBERRY_PINK = RGBA(226, 80, 152)
    RASPBERRY_ROSE = RGBA(179, 68, 108)
    RAW_UMBER = RGBA(130, 102, 68)
    RAZZLE_DAZZLE_ROSE = RGBA(255, 51, 204)
    RAZZMATAZZ = RGBA(227, 37, 107)
    RAZZMIC_BERRY = RGBA(141, 78, 133)
    RED = RGBA(255, 0, 0)
    RED_BROWN = RGBA(165, 42, 42)
    RED_DEVIL = RGBA(134, 1, 17)
    RED_ORANGE = RGBA(255, 83, 73)
    RED_PURPLE = RGBA(228, 0, 120)
    RED_VIOLET = RGBA(199, 21, 133)
    REDWOOD = RGBA(164, 90, 82)
    REGALIA = RGBA(82, 45, 128)
    RESOLUTION_BLUE = RGBA(0, 35, 135)
    RHYTHM = RGBA(119, 118, 150)
    RICH_BLACK = RGBA(0, 64, 64)
    RICH_BRILLIANT_LAVENDER = RGBA(241, 167, 254)
    RICH_CARMINE = RGBA(215, 0, 64)
    RICH_ELECTRIC_BLUE = RGBA(8, 146, 208)
    RICH_LAVENDER = RGBA(167, 107, 207)
    RICH_LILAC = RGBA(182, 102, 210)
    RICH_MAROON = RGBA(176, 48, 96)
    RIFLE_GREEN = RGBA(68, 76, 56)
    ROAST_COFFEE = RGBA(112, 66, 65)
    ROBIN_EGG_BLUE = RGBA(0, 204, 204)
    ROCKET_METALLIC = RGBA(138, 127, 128)
    ROMAN_SILVER = RGBA(131, 137, 150)
    ROSE = RGBA(255, 0, 127)
    ROSE_BONBON = RGBA(249, 66, 158)
    ROSE_EBONY = RGBA(103, 72, 70)
    ROSE_GOLD = RGBA(183, 110, 121)
    ROSE_MADDER = RGBA(227, 38, 54)
    ROSE_PINK = RGBA(255, 102, 204)
    ROSE_QUARTZ = RGBA(170, 152, 169)
    ROSE_RED = RGBA(194, 30, 86)
    ROSE_TAUPE = RGBA(144, 93, 93)
    ROSE_VALE = RGBA(171, 78, 82)
    ROSEWOOD = RGBA(101, 0, 11)
    ROSSO_CORSA = RGBA(212, 0, 0)
    ROSY_BROWN = RGBA(188, 143, 143)
    ROYAL_AZURE = RGBA(0, 56, 168)
    ROYAL_BLUE = RGBA(65, 105, 225)
    ROYAL_FUCHSIA = RGBA(202, 44, 146)
    ROYAL_PURPLE = RGBA(120, 81, 169)
    ROYAL_YELLOW = RGBA(250, 218, 94)
    RUBER = RGBA(206, 70, 118)
    RUBINE_RED = RGBA(209, 0, 86)
    RUBY = RGBA(224, 17, 95)
    RUBY_RED = RGBA(155, 17, 30)
    RUDDY = RGBA(255, 0, 40)
    RUDDY_BROWN = RGBA(187, 101, 40)
    RUDDY_PINK = RGBA(225, 142, 150)
    RUFOUS = RGBA(168, 28, 7)
    RUSSET = RGBA(128, 70, 27)
    RUSSIAN_GREEN = RGBA(103, 146, 103)
    RUSSIAN_VIOLET = RGBA(50, 23, 77)
    RUST = RGBA(183, 65, 14)
    RUSTY_RED = RGBA(218, 44, 67)
    SACRAMENTO_STATE_GREEN = RGBA(0, 86, 63)
    SADDLE_BROWN = RGBA(139, 69, 19)
    SAFETY_ORANGE = RGBA(255, 103, 0)
    SAFETY_YELLOW = RGBA(238, 210, 2)
    SAFFRON = RGBA(244, 196, 48)
    SAGE = RGBA(188, 184, 138)
    ST_PATRICK_BLUE = RGBA(35, 41, 122)
    SALMON = RGBA(250, 128, 114)
    SALMON_PINK = RGBA(255, 145, 164)
    SAND = RGBA(194, 178, 128)
    SAND_DUNE = RGBA(150, 113, 23)
    SANDSTORM = RGBA(236, 213, 64)
    SANDY_BROWN = RGBA(244, 164, 96)
    SANDY_TAUPE = RGBA(150, 113, 23)
    SANGRIA = RGBA(146, 0, 10)
    SAP_GREEN = RGBA(80, 125, 42)
    SAPPHIRE = RGBA(15, 82, 186)
    SAPPHIRE_BLUE = RGBA(0, 103, 165)
    SATIN_SHEEN_GOLD = RGBA(203, 161, 53)
    SCARLET = RGBA(255, 36, 0)
    SCHAUSS_PINK = RGBA(255, 145, 175)
    SCHOOL_BUS_YELLOW = RGBA(255, 216, 0)
    SCREAMIN_GREEN = RGBA(118, 255, 122)
    SEA_BLUE = RGBA(0, 105, 148)
    SEA_GREEN = RGBA(46, 255, 139)
    SEAL_BROWN = RGBA(50, 20, 20)
    SEASHELL = RGBA(255, 245, 238)
    SELECTIVE_YELLOW = RGBA(255, 186, 0)
    SEPIA = RGBA(112, 66, 20)
    SHADOW = RGBA(138, 121, 93)
    SHADOW_BLUE = RGBA(119, 139, 165)
    SHAMPOO = RGBA(255, 207, 241)
    SHAMROCK_GREEN = RGBA(0, 158, 96)
    SHEEN_GREEN = RGBA(143, 212, 0)
    SHIMMERING_BLUSH = RGBA(217, 134, 149)
    SHOCKING_PINK = RGBA(252, 15, 192)
    SIENNA = RGBA(136, 45, 23)
    SILVER = RGBA(192, 192, 192)
    SILVER_CHALICE = RGBA(172, 172, 172)
    SILVER_LAKE_BLUE = RGBA(93, 137, 186)
    SILVER_PINK = RGBA(196, 174, 173)
    SILVER_SAND = RGBA(191, 193, 194)
    SINOPIA = RGBA(203, 65, 11)
    SKOBELOFF = RGBA(0, 116, 116)
    SKY_BLUE = RGBA(135, 206, 235)
    SKY_MAGENTA = RGBA(207, 113, 175)
    SLATE_BLUE = RGBA(106, 90, 205)
    SLATE_GRAY = RGBA(112, 128, 144)
    SMALT = RGBA(0, 51, 153)
    SMITTEN = RGBA(200, 65, 134)
    SMOKE = RGBA(115, 130, 118)
    SMOKEY_TOPAZ = RGBA(147, 61, 65)
    SMOKY_BLACK = RGBA(16, 12, 8)
    SNOW = RGBA(255, 250, 250)
    SOAP = RGBA(206, 200, 239)
    SONIC_SILVER = RGBA(117, 117, 117)
    SPACE_CADET = RGBA(29, 41, 81)
    SPANISH_BISTRE = RGBA(128, 117, 90)
    SPANISH_CARMINE = RGBA(209, 0, 71)
    SPANISH_CRIMSON = RGBA(229, 26, 76)
    SPANISH_BLUE = RGBA(0, 112, 184)
    SPANISH_GRAY = RGBA(152, 152, 152)
    SPANISH_GREEN = RGBA(0, 145, 80)
    SPANISH_ORANGE = RGBA(232, 97, 0)
    SPANISH_PINK = RGBA(247, 191, 190)
    SPANISH_RED = RGBA(230, 0, 38)
    SPANISH_SKY_BLUE = RGBA(0, 170, 228)
    SPANISH_VIOLET = RGBA(76, 40, 130)
    SPANISH_VIRIDIAN = RGBA(0, 127, 92)
    SPIRO_DISCO_BALL = RGBA(15, 192, 252)
    SPRING_BUD = RGBA(167, 252, 0)
    SPRING_GREEN = RGBA(0, 255, 127)
    STAR_COMMAND_BLUE = RGBA(0, 123, 184)
    STEEL_BLUE = RGBA(70, 130, 180)
    STEEL_PINK = RGBA(204, 51, 102)
    STIL_DE_GRAIN_YELLOW = RGBA(250, 218, 94)
    STIZZA = RGBA(153, 0, 0)
    STORMCLOUD = RGBA(79, 102, 106)
    STRAW = RGBA(228, 217, 111)
    STRAWBERRY = RGBA(252, 90, 141)
    SUNGLOW = RGBA(255, 204, 51)
    SUNRAY = RGBA(227, 171, 87)
    SUNSET = RGBA(250, 214, 165)
    SUNSET_ORANGE = RGBA(253, 94, 83)
    SUPER_PINK = RGBA(207, 107, 169)
    TAN = RGBA(210, 180, 140)
    TANGELO = RGBA(249, 77, 0)
    TANGERINE = RGBA(242, 133, 0)
    TANGERINE_YELLOW = RGBA(255, 204, 0)
    TANGO_PINK = RGBA(228, 113, 122)
    TAUPE = RGBA(72, 60, 50)
    TAUPE_GRAY = RGBA(139, 133, 137)
    TEA_GREEN = RGBA(208, 240, 192)
    TEA_ROSE = RGBA(244, 194, 194)
    TEAL = RGBA(0, 128, 128)
    TEAL_BLUE = RGBA(54, 117, 136)
    TEAL_DEER = RGBA(153, 230, 179)
    TEAL_GREEN = RGBA(0, 130, 127)
    TELEMAGENTA = RGBA(207, 52, 118)
    TERRA_COTTA = RGBA(226, 114, 91)
    THISTLE = RGBA(216, 191, 216)
    THULIAN_PINK = RGBA(222, 111, 161)
    TICKLE_ME_PINK = RGBA(252, 137, 172)
    TIFFANY_BLUE = RGBA(10, 186, 181)
    TIGERS_EYE = RGBA(224, 141, 60)
    TIMBERWOLF = RGBA(219, 215, 210)
    TITANIUM_YELLOW = RGBA(238, 230, 0)
    TOMATO = RGBA(255, 99, 71)
    TOOLBOX = RGBA(116, 108, 192)
    TOPAZ = RGBA(255, 200, 124)
    TRACTOR_RED = RGBA(253, 14, 53)
    TROLLEY_GREY = RGBA(128, 128, 128)
    TROPICAL_RAIN_FOREST = RGBA(0, 117, 94)
    TRUE_BLUE = RGBA(0, 115, 207)
    TUFTS_BLUE = RGBA(65, 125, 193)
    TULIP = RGBA(255, 135, 141)
    TUMBLEWEED = RGBA(222, 170, 136)
    TURKISH_ROSE = RGBA(181, 114, 129)
    TURQUOISE = RGBA(64, 224, 208)
    TURQUOISE_BLUE = RGBA(0, 255, 239)
    TURQUOISE_GREEN = RGBA(160, 214, 180)
    TUSCAN = RGBA(250, 214, 165)
    TUSCAN_BROWN = RGBA(111, 78, 55)
    TUSCAN_RED = RGBA(124, 72, 72)
    TUSCAN_TAN = RGBA(166, 123, 91)
    TUSCANY = RGBA(192, 153, 153)
    TWILIGHT_LAVENDER = RGBA(138, 73, 107)
    TYRIAN_PURPLE = RGBA(102, 2, 60)
    UA_BLUE = RGBA(0, 51, 170)
    UA_RED = RGBA(217, 0, 76)
    UBE = RGBA(136, 120, 195)
    UCLA_BLUE = RGBA(83, 104, 149)
    UCLA_GOLD = RGBA(255, 179, 0)
    UFO_GREEN = RGBA(60, 208, 112)
    ULTRAMARINE = RGBA(18, 10, 143)
    ULTRAMARINE_BLUE = RGBA(65, 102, 245)
    ULTRA_PINK = RGBA(255, 111, 255)
    UMBER = RGBA(99, 81, 71)
    UNBLEACHED_SILK = RGBA(255, 221, 202)
    UNITED_NATIONS_BLUE = RGBA(91, 146, 229)
    UNIVERSITY_OF_CALIFORNIA_GOLD = RGBA(183, 135, 39)
    UNMELLOW_YELLOW = RGBA(255, 255, 102)
    UP_FOREST_GREEN = RGBA(1, 68, 33)
    UP_MAROON = RGBA(123, 17, 19)
    UPSDELL_RED = RGBA(174, 32, 41)
    UROBILIN = RGBA(225, 173, 33)
    USAFA_BLUE = RGBA(0, 79, 152)
    USC_CARDINAL = RGBA(153, 0, 0)
    USC_GOLD = RGBA(255, 204, 0)
    UNIVERSITY_OF_TENNESSEE_ORANGE = RGBA(247, 127, 0)
    UTAH_CRIMSON = RGBA(211, 0, 63)
    VANILLA = RGBA(243, 229, 171)
    VANILLA_ICE = RGBA(243, 143, 169)
    VEGAS_GOLD = RGBA(197, 179, 88)
    VENETIAN_RED = RGBA(200, 8, 21)
    VERDIGRIS = RGBA(67, 179, 174)
    VERMILION = RGBA(227, 66, 52)
    VERONICA = RGBA(160, 32, 240)
    VIOLET = RGBA(143, 0, 255)
    VIOLET_BLUE = RGBA(50, 74, 178)
    VIOLET_RED = RGBA(247, 83, 148)
    VIRIDIAN = RGBA(64, 130, 109)
    VIRIDIAN_GREEN = RGBA(0, 150, 152)
    VIVID_AUBURN = RGBA(146, 39, 36)
    VIVID_BURGUNDY = RGBA(159, 29, 53)
    VIVID_CERISE = RGBA(218, 29, 129)
    VIVID_ORCHID = RGBA(204, 0, 255)
    VIVID_SKY_BLUE = RGBA(0, 204, 255)
    VIVID_TANGERINE = RGBA(255, 160, 137)
    VIVID_VIOLET = RGBA(159, 0, 255)
    WARM_BLACK = RGBA(0, 66, 66)
    WATERSPOUT = RGBA(164, 244, 249)
    WENGE = RGBA(100, 84, 82)
    WHEAT = RGBA(245, 222, 179)
    WHITE = RGBA(255, 255, 255)
    WHITE_SMOKE = RGBA(245, 245, 245)
    WILD_BLUE_YONDER = RGBA(162, 173, 208)
    WILD_ORCHID = RGBA(212, 112, 162)
    WILD_STRAWBERRY = RGBA(255, 67, 164)
    WILD_WATERMELON = RGBA(252, 108, 133)
    WILLPOWER_ORANGE = RGBA(253, 88, 0)
    WINDSOR_TAN = RGBA(167, 85, 2)
    WINE = RGBA(114, 47, 55)
    WINE_DREGS = RGBA(103, 49, 71)
    WISTERIA = RGBA(201, 160, 220)
    WOOD_BROWN = RGBA(193, 154, 107)
    XANADU = RGBA(115, 134, 120)
    YALE_BLUE = RGBA(15, 77, 146)
    YANKEES_BLUE = RGBA(28, 40, 65)
    YELLOW = RGBA(255, 255, 0)
    YELLOW_GREEN = RGBA(154, 205, 50)
    YELLOW_ORANGE = RGBA(255, 174, 66)
    YELLOW_ROSE = RGBA(255, 240, 0)
    ZAFFRE = RGBA(0, 20, 168)
    ZINNWALDITE_BROWN = RGBA(44, 22, 8)