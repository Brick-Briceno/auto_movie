
def test_emoji(char="🤩"):
    print(f"U+{ord(char):04x}")

emojis = {
    "🙂": "Emojis/iphone/emoji 95.png",
    "🙃": "Emojis/iphone/emoji 928.png",
    "☹": "Emojis/iphone/emoji 1457.png",
    "🙁": "Emojis/iphone/emoji 1023.png",
    "🙄": "Emojis/iphone/emoji 1566.png",
    "🤐": "Emojis/iphone/emoji 3261.png",
    "🤑": "Emojis/iphone/emoji 1836.png",
    "🤒": "Emojis/iphone/emoji 2442.png",
    "🤓": "Emojis/iphone/emoji 168.png",
    "🤔": "Emojis/iphone/emoji 3738.png",
    "🤕": "Emojis/iphone/emoji 675.png",
    "🤖": "Emojis/iphone/",
    "🤗": "Emojis/iphone/emoji 1314.png",
    "🤠": "Emojis/iphone/emoji 1985.png",
    "🤡": "Emojis/iphone/emoji 2117.png",
    "🎅": "Emojis/iphone/emoji 3224.png",
    "🤢": "Emojis/iphone/emoji 3150.png",
    "🤣": "Emojis/iphone/emoji 390.png",
    "🤤": "Emojis/iphone/emoji 2866.png",
    "🤥": "Emojis/iphone/emoji 3001.png",
    "🤦": "Emojis/iphone/",
    "🤧": "Emojis/iphone/emoji 1592.png",
    "🤨": "Emojis/iphone/emoji 2329.png",
    "🤩": "Emojis/iphone/emoji 1244.png",
    "🤪": "Emojis/iphone/emoji 588.png",
    "🤫": "Emojis/iphone/emoji 2101.png",
    "🤬": "Emojis/iphone/emoji 1242.png",
    "🤭": "Emojis/iphone/",
    "🤮": "Emojis/iphone/emoji 3415.png",
    "🤯": "Emojis/iphone/",
    "😀": "Emojis/iphone/emoji 2812.png",
    "😁": "Emojis/iphone/emoji 1243.png",
    "😂": "Emojis/iphone/emoji 1622.png",
    "😃": "Emojis/iphone/emoji 640.png",
    "😄": "Emojis/iphone/emoji 3915.png",
    "😅": "Emojis/iphone/emoji 1596.png",
    "😆": "Emojis/iphone/emoji 2389.png",
    "😇": "Emojis/iphone/emoji 1343.png",
    "😈": "Emojis/iphone/",
    "😉": "Emojis/iphone/emoji 1039.png",
    "😊": "Emojis/iphone/emoji 1078.png", #emoji 1467.png ???
    "😋": "Emojis/iphone/emoji 2392.png",
    "😌": "Emojis/iphone/emoji 1045.png",
    "😍": "Emojis/iphone/emoji 3317.png",
    "😎": "Emojis/iphone/emoji 2280.png",
    "😏": "Emojis/iphone/emoji 830.png",
    "😐": "Emojis/iphone/emoji 3900.png",
    "😑": "Emojis/iphone/emoji 1290.png",
    "😒": "Emojis/iphone/",
    "😓": "Emojis/iphone/emoji 773.png",
    "😔": "Emojis/iphone/emoji 950.png",
    "😕": "Emojis/iphone/emoji 637.png",
    "😖": "Emojis/iphone/emoji 3807.png",
    "😗": "Emojis/iphone/emoji 1184.png",
    "😘": "Emojis/iphone/emoji 2138.png",
    "😙": "Emojis/iphone/emoji 2262.png",
    "😚": "Emojis/iphone/emoji 777.png",
    "😛": "Emojis/iphone/emoji 2794.png",
    "😜": "Emojis/iphone/emoji 1558.png",
    "😝": "Emojis/iphone/",
    "😞": "Emojis/iphone/emoji 1317.png",
    "😟": "Emojis/iphone/emoji 3198.png",
    "😠": "Emojis/iphone/emoji 3209.png",
    "😡": "Emojis/iphone/emoji 1697.png",
    "😢": "Emojis/iphone/emoji 3445.png",
    "😣": "Emojis/iphone/emoji 3953.png",
    "😤": "Emojis/iphone/emoji 3239.png",
    "😥": "Emojis/iphone/emoji 3445.png",
    "😦": "Emojis/iphone/emoji 3272.png",
    "😧": "Emojis/iphone/",
    "😰": "Emojis/iphone/emoji 296.png",
    "😨": "Emojis/iphone/emoji 24.png",
    "😩": "Emojis/iphone/emoji 1914.png",
    "😪": "Emojis/iphone/emoji 377.png",
    "😫": "Emojis/iphone/emoji 3332.png",
    "😬": "Emojis/iphone/emoji 3202.png",
    "😭": "Emojis/iphone/",
    "😮": "Emojis/iphone/emoji 3136.png",
    "😯": "Emojis/iphone/emoji 731.png",
    "😱": "Emojis/iphone/emoji 182.png",
    "😲": "Emojis/iphone/emoji 243.png",
    "😳": "Emojis/iphone/emoji 3681.png",
    "😴": "Emojis/iphone/emoji 1014.png",
    "😵": "Emojis/iphone/emoji 789.png",
    "😶": "Emojis/iphone/emoji 2022.png",
    "😷": "Emojis/iphone/emoji 1559.png",
    "👿": "Emojis/iphone/emoji 220.png",
    "💀": "Emojis/iphone/emoji 485.png",
    "🥰": "Emojis/iphone/emoji 3379.png",
    "🥱": "Emojis/iphone/emoji 1262.png",
    "🥳": "Emojis/iphone/",
    "🥴": "Emojis/iphone/",
    "🥵": "Emojis/iphone/emoji 2693.png",
    "🥶": "Emojis/iphone/emoji 2009.png",
    "🥺": "Emojis/iphone/emoji 2091.png",
    "🧐": "Emojis/iphone/emoji 3271.png",
    "😸": "Emojis/iphone/emoji 2110.png",
    "😹": "Emojis/iphone/",
    "😺": "Emojis/iphone/",
    "😻": "Emojis/iphone/emoji 2586.png",
    "😼": "Emojis/iphone/emoji 2053.png",
    "😽": "Emojis/iphone/emoji 3664.png",
    "😾": "Emojis/iphone/emoji 963.png",
    "😿": "Emojis/iphone/emoji 135.png",
    "🙀": "Emojis/iphone/emoji 3636.png",
    "\u200d": "Emojis/iphone/",
    "‼": "Emojis/iphone/",
    "⁉": "Emojis/iphone/",
    "ℹ": "Emojis/iphone/",
    "↔": "Emojis/iphone/",
    "↕": "Emojis/iphone/",
    "↖": "Emojis/iphone/",
    "↗": "Emojis/iphone/",
    "↘": "Emojis/iphone/",
    "↙": "Emojis/iphone/",
    "↩": "Emojis/iphone/",
    "↪": "Emojis/iphone/",
    "⌚": "Emojis/iphone/",
    "⌛": "Emojis/iphone/",
    "⌨": "Emojis/iphone/",
    "⏏": "Emojis/iphone/",
    "⏩": "Emojis/iphone/",
    "⏪": "Emojis/iphone/",
    "⏫": "Emojis/iphone/",
    "⏬": "Emojis/iphone/",
    "⏭": "Emojis/iphone/",
    "⏮": "Emojis/iphone/",
    "⏯": "Emojis/iphone/",
    "⏰": "Emojis/iphone/",
    "⏱": "Emojis/iphone/",
    "⏲": "Emojis/iphone/",
    "⏳": "Emojis/iphone/",
    "⏸": "Emojis/iphone/",
    "⏹": "Emojis/iphone/",
    "⏺": "Emojis/iphone/",
    "Ⓜ": "Emojis/iphone/",
    "▪": "Emojis/iphone/",
    "▫": "Emojis/iphone/",
    "▶": "Emojis/iphone/",
    "◀": "Emojis/iphone/",
    "◻": "Emojis/iphone/",
    "◼": "Emojis/iphone/",
    "◽": "Emojis/iphone/",
    "◾": "Emojis/iphone/",
    "☀": "Emojis/iphone/emoji 3901.png",
    "☁": "Emojis/iphone/",
    "☂": "Emojis/iphone/",
    "☃": "Emojis/iphone/",
    "☄": "Emojis/iphone/",
    "☎": "Emojis/iphone/",
    "☑": "Emojis/iphone/",
    "☔": "Emojis/iphone/",
    "☕": "Emojis/iphone/",
    "☘": "Emojis/iphone/",
    "☝": "Emojis/iphone/",
    "☠": "Emojis/iphone/emoji 821.png",
    "☢": "Emojis/iphone/",
    "☣": "Emojis/iphone/",
    "☦": "Emojis/iphone/",
    "☪": "Emojis/iphone/",
    "☮": "Emojis/iphone/",
    "☯": "Emojis/iphone/",
    "☸": "Emojis/iphone/",
    "☺": "Emojis/iphone/",
    "♀": "Emojis/iphone/",
    "♂": "Emojis/iphone/",
    "♈": "Emojis/iphone/",
    "♉": "Emojis/iphone/",
    "♊": "Emojis/iphone/",
    "♋": "Emojis/iphone/",
    "♌": "Emojis/iphone/",
    "♍": "Emojis/iphone/",
    "♎": "Emojis/iphone/",
    "♏": "Emojis/iphone/",
    "♐": "Emojis/iphone/",
    "♑": "Emojis/iphone/",
    "♒": "Emojis/iphone/",
    "♓": "Emojis/iphone/",
    "♟": "Emojis/iphone/",
    "♥": "Emojis/iphone/emoji 3523.png",
    "♨": "Emojis/iphone/",
    "♻": "Emojis/iphone/",
    "♾": "Emojis/iphone/",
    "♿": "Emojis/iphone/",
    "⚒": "Emojis/iphone/",
    "⚓": "Emojis/iphone/",
    "⚔": "Emojis/iphone/",
    "⚕": "Emojis/iphone/",
    "⚖": "Emojis/iphone/",
    "⚗": "Emojis/iphone/",
    "⚙": "Emojis/iphone/",
    "⚛": "Emojis/iphone/emoji 1318.png",
    "⚜": "Emojis/iphone/",
    "⚠": "Emojis/iphone/",
    "⚡": "Emojis/iphone/emoji 3397.png",
    "⚧": "Emojis/iphone/",
    "⚪": "Emojis/iphone/",
    "⚫": "Emojis/iphone/",
    "⚰": "Emojis/iphone/",
    "⚱": "Emojis/iphone/",
    "⚽": "Emojis/iphone/",
    "⚾": "Emojis/iphone/",
    "⛄": "Emojis/iphone/",
    "⛅": "Emojis/iphone/",
    "⛈": "Emojis/iphone/",
    "⛎": "Emojis/iphone/",
    "⛏": "Emojis/iphone/",
    "⛑": "Emojis/iphone/",
    "⛓": "Emojis/iphone/",
    "⛔": "Emojis/iphone/",
    "⛩": "Emojis/iphone/",
    "⛪": "Emojis/iphone/",
    "⛰": "Emojis/iphone/",
    "⛱": "Emojis/iphone/",
    "⛲": "Emojis/iphone/",
    "⛳": "Emojis/iphone/",
    "⛴": "Emojis/iphone/",
    "⛵": "Emojis/iphone/",
    "⛷": "Emojis/iphone/",
    "⛸": "Emojis/iphone/",
    "⛹": "Emojis/iphone/",
    "⛺": "Emojis/iphone/",
    "⛽": "Emojis/iphone/",
    "✂": "Emojis/iphone/",
    "✅": "Emojis/iphone/",
    "✈": "Emojis/iphone/",
    "✉": "Emojis/iphone/",
    "✊": "Emojis/iphone/emoji 795.png",
    "✋": "Emojis/iphone/",
    "✌": "Emojis/iphone/",
    "✍": "Emojis/iphone/",
    "✏": "Emojis/iphone/",
    "✒": "Emojis/iphone/",
    "✔": "Emojis/iphone/",
    "✖": "Emojis/iphone/",
    "✝": "Emojis/iphone/",
    "✡": "Emojis/iphone/",
    "✨": "Emojis/iphone/emoji 2825.png",
    "✳": "Emojis/iphone/",
    "✴": "Emojis/iphone/",
    "❄": "Emojis/iphone/",
    "❇": "Emojis/iphone/",
    "❌": "Emojis/iphone/",
    "❎": "Emojis/iphone/",
    "❓": "Emojis/iphone/",
    "❔": "Emojis/iphone/",
    "❕": "Emojis/iphone/",
    "❗": "Emojis/iphone/",
    "❣": "Emojis/iphone/",
    "❤": "Emojis/iphone/emoji 3523.png",
    "➕": "Emojis/iphone/",
    "➖": "Emojis/iphone/",
    "➗": "Emojis/iphone/",
    "➡": "Emojis/iphone/",
    "➰": "Emojis/iphone/",
    "➿": "Emojis/iphone/",
    "⤴": "Emojis/iphone/",
    "⤵": "Emojis/iphone/",
    "⬅": "Emojis/iphone/",
    "⬆": "Emojis/iphone/",
    "⬇": "Emojis/iphone/",
    "⬛": "Emojis/iphone/",
    "⬜": "Emojis/iphone/",
    "⭐": "Emojis/iphone/emoji 3784.png",
    "⭕": "Emojis/iphone/",
    "〰": "Emojis/iphone/",
    "〽": "Emojis/iphone/",
    "㊗": "Emojis/iphone/",
    "㊙": "Emojis/iphone/",
    "🀄": "Emojis/iphone/",
    "🃏": "Emojis/iphone/",
    "🅰": "Emojis/iphone/",
    "🅱": "Emojis/iphone/",
    "🅾": "Emojis/iphone/",
    "🅿": "Emojis/iphone/",
    "🆎": "Emojis/iphone/",
    "🆑": "Emojis/iphone/",
    "🆒": "Emojis/iphone/",
    "🆓": "Emojis/iphone/",
    "🆔": "Emojis/iphone/",
    "🆕": "Emojis/iphone/",
    "🆖": "Emojis/iphone/",
    "🆗": "Emojis/iphone/",
    "🆘": "Emojis/iphone/",
    "🆙": "Emojis/iphone/",
    "🆚": "Emojis/iphone/",
    "🈁": "Emojis/iphone/",
    "🈂": "Emojis/iphone/",
    "🈚": "Emojis/iphone/",
    "🈯": "Emojis/iphone/",
    "🈲": "Emojis/iphone/",
    "🈳": "Emojis/iphone/",
    "🈴": "Emojis/iphone/",
    "🈵": "Emojis/iphone/",
    "🈶": "Emojis/iphone/",
    "🈷": "Emojis/iphone/",
    "🈸": "Emojis/iphone/",
    "🈹": "Emojis/iphone/",
    "🈺": "Emojis/iphone/",
    "🉐": "Emojis/iphone/",
    "🉑": "Emojis/iphone/",
    "🌀": "Emojis/iphone/",
    "🌁": "Emojis/iphone/",
    "🌂": "Emojis/iphone/",
    "🌃": "Emojis/iphone/",
    "🌄": "Emojis/iphone/",
    "🌅": "Emojis/iphone/emoji 3937.png",
    "🌆": "Emojis/iphone/",
    "🌇": "Emojis/iphone/",
    "🌈": "Emojis/iphone/emoji 2768.png",
    "🌉": "Emojis/iphone/",
    "🌊": "Emojis/iphone/emoji 2246.png",
    "🌋": "Emojis/iphone/emoji 1415.png",
    "🌌": "Emojis/iphone/",
    "🌍": "Emojis/iphone/",
    "🌎": "Emojis/iphone/",
    "🌏": "Emojis/iphone/",
    "🌐": "Emojis/iphone/",
    "🌑": "Emojis/iphone/",
    "🌒": "Emojis/iphone/",
    "🌓": "Emojis/iphone/",
    "🌔": "Emojis/iphone/",
    "🌕": "Emojis/iphone/",
    "🌖": "Emojis/iphone/",
    "🌗": "Emojis/iphone/",
    "🌘": "Emojis/iphone/",
    "🌙": "Emojis/iphone/emoji 2222.png",
    "🌝": "Emojis/iphone/emoji 3761.png",
    "🌚": "Emojis/iphone/emoji 3585.png",
    "🌛": "Emojis/iphone/",
    "🌜": "Emojis/iphone/",
    "🌞": "Emojis/iphone/",
    "🌟": "Emojis/iphone/",
    "🌠": "Emojis/iphone/",
    "🌡": "Emojis/iphone/",
    "🌤": "Emojis/iphone/",
    "🌥": "Emojis/iphone/",
    "🌦": "Emojis/iphone/",
    "🌧": "Emojis/iphone/",
    "🌨": "Emojis/iphone/",
    "🌩": "Emojis/iphone/",
    "🌪": "Emojis/iphone/",
    "🌫": "Emojis/iphone/",
    "🌬": "Emojis/iphone/",
    "🌭": "Emojis/iphone/emoji 201.png",
    "🌮": "Emojis/iphone/",
    "🌯": "Emojis/iphone/",
    "🌰": "Emojis/iphone/",
    "🌱": "Emojis/iphone/emoji 2709.png",
    "🌲": "Emojis/iphone/",
    "🌳": "Emojis/iphone/",
    "🌴": "Emojis/iphone/",
    "🌵": "Emojis/iphone/",
    "🌶": "Emojis/iphone/emoji 3281.png",
    "🌷": "Emojis/iphone/",
    "🌸": "Emojis/iphone/",
    "🌹": "Emojis/iphone/",
    "🌺": "Emojis/iphone/",
    "🌻": "Emojis/iphone/",
    "🌼": "Emojis/iphone/",
    "🌽": "Emojis/iphone/",
    "🌾": "Emojis/iphone/",
    "🌿": "Emojis/iphone/",
    "🍀": "Emojis/iphone/",
    "🍁": "Emojis/iphone/",
    "🍂": "Emojis/iphone/",
    "🍃": "Emojis/iphone/",
    "🍄": "Emojis/iphone/",
    "🍅": "Emojis/iphone/emoji 2664.png",
    "🍆": "Emojis/iphone/emoji 203.png",
    "🍇": "Emojis/iphone/",
    "🍈": "Emojis/iphone/",
    "🍉": "Emojis/iphone/",
    "🍊": "Emojis/iphone/",
    "🍋": "Emojis/iphone/emoji 2005.png",
    "🍌": "Emojis/iphone/",
    "🍍": "Emojis/iphone/",
    "🍎": "Emojis/iphone/emoji 818.png",
    "🍏": "Emojis/iphone/emoji 98.png",
    "🍐": "Emojis/iphone/",
    "🍑": "Emojis/iphone/",
    "🍒": "Emojis/iphone/emoji 1382.png",
    "🍓": "Emojis/iphone/emoji 3724.png",
    "🍔": "Emojis/iphone/emoji 452.png",
    "🍕": "Emojis/iphone/emoji 193.png",
    "🍖": "Emojis/iphone/",
    "🍗": "Emojis/iphone/",
    "🍘": "Emojis/iphone/",
    "🍙": "Emojis/iphone/",
    "🍚": "Emojis/iphone/",
    "🍛": "Emojis/iphone/",
    "🍜": "Emojis/iphone/",
    "🍝": "Emojis/iphone/emoji 3148.png",
    "🍞": "Emojis/iphone/",
    "🍟": "Emojis/iphone/",
    "🍠": "Emojis/iphone/",
    "🍡": "Emojis/iphone/",
    "🍢": "Emojis/iphone/",
    "🍣": "Emojis/iphone/",
    "🍤": "Emojis/iphone/",
    "🍥": "Emojis/iphone/",
    "🍦": "Emojis/iphone/",
    "🍧": "Emojis/iphone/",
    "🍨": "Emojis/iphone/",
    "🍩": "Emojis/iphone/",
    "🍪": "Emojis/iphone/",
    "🍫": "Emojis/iphone/",
    "🍬": "Emojis/iphone/",
    "🍭": "Emojis/iphone/",
    "🍮": "Emojis/iphone/",
    "🍯": "Emojis/iphone/",
    "🍰": "Emojis/iphone/",
    "🍱": "Emojis/iphone/",
    "🍲": "Emojis/iphone/",
    "🍳": "Emojis/iphone/",
    "🍴": "Emojis/iphone/",
    "🍵": "Emojis/iphone/",
    "🍶": "Emojis/iphone/",
    "🍷": "Emojis/iphone/emoji 3946.png",
    "🍸": "Emojis/iphone/",
    "🍹": "Emojis/iphone/",
    "🍺": "Emojis/iphone/",
    "🍻": "Emojis/iphone/",
    "🍼": "Emojis/iphone/",
    "🍽": "Emojis/iphone/",
    "🍾": "Emojis/iphone/",
    "🍿": "Emojis/iphone/",
    "🎀": "Emojis/iphone/",
    "🎁": "Emojis/iphone/",
    "🎂": "Emojis/iphone/",
    "🎃": "Emojis/iphone/",
    "🎄": "Emojis/iphone/",
    "🎆": "Emojis/iphone/",
    "🎇": "Emojis/iphone/",
    "🎈": "Emojis/iphone/",
    "🎉": "Emojis/iphone/",
    "🎊": "Emojis/iphone/",
    "🎋": "Emojis/iphone/",
    "🎌": "Emojis/iphone/",
    "🎍": "Emojis/iphone/",
    "🎎": "Emojis/iphone/",
    "🎏": "Emojis/iphone/",
    "🎐": "Emojis/iphone/",
    "🎑": "Emojis/iphone/",
    "🎒": "Emojis/iphone/",
    "🎓": "Emojis/iphone/",
    "🎖": "Emojis/iphone/",
    "🎗": "Emojis/iphone/",
    "🎙": "Emojis/iphone/",
    "🎚": "Emojis/iphone/",
    "🎛": "Emojis/iphone/",
    "🎞": "Emojis/iphone/",
    "🎟": "Emojis/iphone/",
    "🎠": "Emojis/iphone/",
    "🎡": "Emojis/iphone/",
    "🎢": "Emojis/iphone/",
    "🎣": "Emojis/iphone/",
    "🎤": "Emojis/iphone/",
    "🎥": "Emojis/iphone/",
    "🎦": "Emojis/iphone/",
    "🎧": "Emojis/iphone/",
    "🎨": "Emojis/iphone/",
    "🎩": "Emojis/iphone/",
    "🎪": "Emojis/iphone/",
    "🎫": "Emojis/iphone/",
    "🎬": "Emojis/iphone/",
    "🎭": "Emojis/iphone/",
    "🎮": "Emojis/iphone/",
    "🎯": "Emojis/iphone/",
    "🎰": "Emojis/iphone/",
    "🎱": "Emojis/iphone/",
    "🎲": "Emojis/iphone/",
    "🎳": "Emojis/iphone/",
    "🎴": "Emojis/iphone/",
    "🎵": "Emojis/iphone/",
    "🎶": "Emojis/iphone/",
    "🎷": "Emojis/iphone/",
    "🎸": "Emojis/iphone/",
    "🎹": "Emojis/iphone/emoji 164.png",
    "🎺": "Emojis/iphone/",
    "🎻": "Emojis/iphone/",
    "🎼": "Emojis/iphone/emoji 3661.png",
    "🎽": "Emojis/iphone/",
    "🎾": "Emojis/iphone/",
    "🎿": "Emojis/iphone/",
    "🏀": "Emojis/iphone/",
    "🏁": "Emojis/iphone/",
    "🏂": "Emojis/iphone/",
    "🏃": "Emojis/iphone/",
    "🏄": "Emojis/iphone/",
    "🏅": "Emojis/iphone/",
    "🏆": "Emojis/iphone/",
    "🏇": "Emojis/iphone/",
    "🏈": "Emojis/iphone/",
    "🏉": "Emojis/iphone/",
    "🏊": "Emojis/iphone/",
    "🏋": "Emojis/iphone/",
    "🏌": "Emojis/iphone/",
    "🏍": "Emojis/iphone/",
    "🏎": "Emojis/iphone/",
    "🏏": "Emojis/iphone/",
    "🏐": "Emojis/iphone/",
    "🏑": "Emojis/iphone/",
    "🏒": "Emojis/iphone/",
    "🏓": "Emojis/iphone/",
    "🏔": "Emojis/iphone/",
    "🏕": "Emojis/iphone/",
    "🏖": "Emojis/iphone/",
    "🏗": "Emojis/iphone/",
    "🏘": "Emojis/iphone/",
    "🏙": "Emojis/iphone/",
    "🏚": "Emojis/iphone/",
    "🏛": "Emojis/iphone/",
    "🏜": "Emojis/iphone/",
    "🏝": "Emojis/iphone/",
    "🏞": "Emojis/iphone/",
    "🏟": "Emojis/iphone/",
    "🏠": "Emojis/iphone/",
    "🏡": "Emojis/iphone/",
    "🏢": "Emojis/iphone/",
    "🏣": "Emojis/iphone/",
    "🏤": "Emojis/iphone/",
    "🏥": "Emojis/iphone/",
    "🏦": "Emojis/iphone/",
    "🏧": "Emojis/iphone/",
    "🏨": "Emojis/iphone/",
    "🏩": "Emojis/iphone/",
    "🏪": "Emojis/iphone/",
    "🏫": "Emojis/iphone/",
    "🏬": "Emojis/iphone/",
    "🏭": "Emojis/iphone/",
    "🏮": "Emojis/iphone/",
    "🏯": "Emojis/iphone/",
    "🏰": "Emojis/iphone/",
    "🏳": "Emojis/iphone/",
    "🏴": "Emojis/iphone/",
    "🏵": "Emojis/iphone/",
    "🏷": "Emojis/iphone/",
    "🏸": "Emojis/iphone/",
    "🏹": "Emojis/iphone/",
    "🏺": "Emojis/iphone/",
    "🐀": "Emojis/iphone/",
    "🐁": "Emojis/iphone/emoji 3600.png",
    "🐂": "Emojis/iphone/",
    "🐃": "Emojis/iphone/",
    "🐄": "Emojis/iphone/",
    "🐅": "Emojis/iphone/",
    "🐆": "Emojis/iphone/emoji 3782.png",
    "🐇": "Emojis/iphone/",
    "🐈": "Emojis/iphone/",
    "🐉": "Emojis/iphone/",
    "🐊": "Emojis/iphone/emoji 525.png",
    "🐋": "Emojis/iphone/",
    "🐌": "Emojis/iphone/emoji 2757.png",
    "🐍": "Emojis/iphone/emoji 3166.png",
    "🐎": "Emojis/iphone/",
    "🐏": "Emojis/iphone/",
    "🐐": "Emojis/iphone/",
    "🐑": "Emojis/iphone/",
    "🐒": "Emojis/iphone/",
    "🐓": "Emojis/iphone/",
    "🐔": "Emojis/iphone/",
    "🐕": "Emojis/iphone/",
    "🐖": "Emojis/iphone/",
    "🐗": "Emojis/iphone/",
    "🐘": "Emojis/iphone/",
    "🐙": "Emojis/iphone/",
    "🐚": "Emojis/iphone/",
    "🐛": "Emojis/iphone/",
    "🐜": "Emojis/iphone/",
    "🐝": "Emojis/iphone/",
    "🐞": "Emojis/iphone/",
    "🐟": "Emojis/iphone/",
    "🐠": "Emojis/iphone/",
    "🐡": "Emojis/iphone/",
    "🐢": "Emojis/iphone/emoji 47.png",
    "🐣": "Emojis/iphone/",
    "🐤": "Emojis/iphone/",
    "🐥": "Emojis/iphone/",
    "🐦": "Emojis/iphone/",
    "🐧": "Emojis/iphone/",
    "🐨": "Emojis/iphone/",
    "🐩": "Emojis/iphone/",
    "🐪": "Emojis/iphone/",
    "🐫": "Emojis/iphone/",
    "🐬": "Emojis/iphone/",
    "🐭": "Emojis/iphone/",
    "🐮": "Emojis/iphone/",
    "🐯": "Emojis/iphone/",
    "🐰": "Emojis/iphone/",
    "🐱": "Emojis/iphone/",
    "🐲": "Emojis/iphone/",
    "🐳": "Emojis/iphone/",
    "🐴": "Emojis/iphone/",
    "🐵": "Emojis/iphone/",
    "🐶": "Emojis/iphone/emoji 413.png",
    "🐷": "Emojis/iphone/",
    "🐸": "Emojis/iphone/",
    "🐹": "Emojis/iphone/",
    "🐺": "Emojis/iphone/",
    "🐻": "Emojis/iphone/",
    "🐼": "Emojis/iphone/",
    "🐽": "Emojis/iphone/",
    "🐾": "Emojis/iphone/",
    "🐿": "Emojis/iphone/",
    "👀": "Emojis/iphone/",
    "👁": "Emojis/iphone/emoji 3366.png",
    "👂": "Emojis/iphone/",
    "👃": "Emojis/iphone/",
    "👄": "Emojis/iphone/",
    "👅": "Emojis/iphone/",
    "👆": "Emojis/iphone/",
    "👇": "Emojis/iphone/",
    "👈": "Emojis/iphone/",
    "👉": "Emojis/iphone/",
    "👊": "Emojis/iphone/",
    "👋": "Emojis/iphone/",
    "👌": "Emojis/iphone/",
    "👍": "Emojis/iphone/emoji 2732.png",
    "👎": "Emojis/iphone/",
    "👏": "Emojis/iphone/",
    "👐": "Emojis/iphone/",
    "👑": "Emojis/iphone/",
    "👒": "Emojis/iphone/",
    "👓": "Emojis/iphone/",
    "👔": "Emojis/iphone/",
    "👕": "Emojis/iphone/",
    "👖": "Emojis/iphone/",
    "👗": "Emojis/iphone/",
    "👘": "Emojis/iphone/",
    "👙": "Emojis/iphone/",
    "👚": "Emojis/iphone/",
    "👛": "Emojis/iphone/",
    "👜": "Emojis/iphone/",
    "👝": "Emojis/iphone/",
    "👞": "Emojis/iphone/",
    "👟": "Emojis/iphone/",
    "👠": "Emojis/iphone/",
    "👡": "Emojis/iphone/",
    "👢": "Emojis/iphone/",
    "👣": "Emojis/iphone/",
    "👤": "Emojis/iphone/",
    "👥": "Emojis/iphone/",
    "👧": "Emojis/iphone/",
    "👨": "Emojis/iphone/",
    "👩": "Emojis/iphone/",
    "👫": "Emojis/iphone/",
    "👬": "Emojis/iphone/",
    "👭": "Emojis/iphone/",
    "👮": "Emojis/iphone/",
    "👯": "Emojis/iphone/",
    "👰": "Emojis/iphone/",
    "👱": "Emojis/iphone/",
    "👲": "Emojis/iphone/",
    "👳": "Emojis/iphone/",
    "👵": "Emojis/iphone/",
    "👶": "Emojis/iphone/",
    "👷": "Emojis/iphone/",
    "👸": "Emojis/iphone/",
    "👹": "Emojis/iphone/",
    "👺": "Emojis/iphone/",
    "👻": "Emojis/iphone/emoji 2162.png",
    "👼": "Emojis/iphone/",
    "👽": "Emojis/iphone/emoji 1713.png",
    "👾": "Emojis/iphone/emoji 1864.png",
    "💁": "Emojis/iphone/",
    "💂": "Emojis/iphone/",
    "💃": "Emojis/iphone/",
    "💄": "Emojis/iphone/",
    "💅": "Emojis/iphone/",
    "💆": "Emojis/iphone/",
    "💇": "Emojis/iphone/",
    "💈": "Emojis/iphone/",
    "💉": "Emojis/iphone/",
    "💊": "Emojis/iphone/",
    "💋": "Emojis/iphone/",
    "💌": "Emojis/iphone/",
    "💍": "Emojis/iphone/",
    "💎": "Emojis/iphone/",
    "💏": "Emojis/iphone/",
    "💐": "Emojis/iphone/",
    "💑": "Emojis/iphone/",
    "💒": "Emojis/iphone/",
    "💓": "Emojis/iphone/",
    "💔": "Emojis/iphone/emoji 3275.png",
    "💕": "Emojis/iphone/emoji 3075.png",
    "💖": "Emojis/iphone/",
    "💗": "Emojis/iphone/",
    "💘": "Emojis/iphone/",
    "💙": "Emojis/iphone/emoji 1947.png",
    "💚": "Emojis/iphone/emoji 3793.png",
    "💛": "Emojis/iphone/emoji 3546.png",
    "💜": "Emojis/iphone/emoji 2999.png",
    "💝": "Emojis/iphone/",
    "💞": "Emojis/iphone/",
    "💟": "Emojis/iphone/",
    "💠": "Emojis/iphone/",
    "💡": "Emojis/iphone/emoji 3385.png",
    "💢": "Emojis/iphone/",
    "💣": "Emojis/iphone/emoji 1372.png",
    "💤": "Emojis/iphone/emoji 2024.png",
    "💥": "Emojis/iphone/",
    "💦": "Emojis/iphone/",
    "💧": "Emojis/iphone/",
    "💨": "Emojis/iphone/",
    "💩": "Emojis/iphone/emoji 3729.png",
    "💪": "Emojis/iphone/",
    "💫": "Emojis/iphone/",
    "💬": "Emojis/iphone/",
    "💭": "Emojis/iphone/",
    "💮": "Emojis/iphone/",
    "💯": "Emojis/iphone/emoji 3894.png",
    "💰": "Emojis/iphone/",
    "💱": "Emojis/iphone/",
    "💲": "Emojis/iphone/",
    "💳": "Emojis/iphone/",
    "💴": "Emojis/iphone/",
    "💵": "Emojis/iphone/",
    "💶": "Emojis/iphone/",
    "💷": "Emojis/iphone/",
    "💸": "Emojis/iphone/",
    "💹": "Emojis/iphone/",
    "💺": "Emojis/iphone/",
    "💻": "Emojis/iphone/",
    "💼": "Emojis/iphone/",
    "💽": "Emojis/iphone/",
    "💾": "Emojis/iphone/",
    "💿": "Emojis/iphone/",
    "📀": "Emojis/iphone/",
    "📁": "Emojis/iphone/",
    "📂": "Emojis/iphone/",
    "📃": "Emojis/iphone/",
    "📄": "Emojis/iphone/",
    "📅": "Emojis/iphone/",
    "📆": "Emojis/iphone/",
    "📇": "Emojis/iphone/",
    "📈": "Emojis/iphone/",
    "📉": "Emojis/iphone/",
    "📊": "Emojis/iphone/",
    "📋": "Emojis/iphone/",
    "📌": "Emojis/iphone/",
    "📍": "Emojis/iphone/",
    "📎": "Emojis/iphone/",
    "📏": "Emojis/iphone/",
    "📐": "Emojis/iphone/",
    "📑": "Emojis/iphone/",
    "📒": "Emojis/iphone/",
    "📓": "Emojis/iphone/",
    "📔": "Emojis/iphone/",
    "📕": "Emojis/iphone/",
    "📖": "Emojis/iphone/",
    "📗": "Emojis/iphone/",
    "📘": "Emojis/iphone/",
    "📙": "Emojis/iphone/",
    "📚": "Emojis/iphone/",
    "📛": "Emojis/iphone/",
    "📜": "Emojis/iphone/",
    "📝": "Emojis/iphone/",
    "📞": "Emojis/iphone/",
    "📟": "Emojis/iphone/",
    "📠": "Emojis/iphone/",
    "📡": "Emojis/iphone/",
    "📢": "Emojis/iphone/",
    "📣": "Emojis/iphone/",
    "📤": "Emojis/iphone/",
    "📥": "Emojis/iphone/",
    "📦": "Emojis/iphone/",
    "📧": "Emojis/iphone/",
    "📨": "Emojis/iphone/",
    "📩": "Emojis/iphone/",
    "📪": "Emojis/iphone/",
    "📫": "Emojis/iphone/",
    "📬": "Emojis/iphone/",
    "📭": "Emojis/iphone/",
    "📮": "Emojis/iphone/",
    "📯": "Emojis/iphone/",
    "📰": "Emojis/iphone/",
    "📱": "Emojis/iphone/",
    "📲": "Emojis/iphone/",
    "📳": "Emojis/iphone/",
    "📴": "Emojis/iphone/",
    "📵": "Emojis/iphone/",
    "📶": "Emojis/iphone/",
    "📷": "Emojis/iphone/",
    "📸": "Emojis/iphone/",
    "📹": "Emojis/iphone/",
    "📺": "Emojis/iphone/",
    "📻": "Emojis/iphone/",
    "📼": "Emojis/iphone/",
    "📽": "Emojis/iphone/",
    "📿": "Emojis/iphone/",
    "🔀": "Emojis/iphone/",
    "🔁": "Emojis/iphone/",
    "🔂": "Emojis/iphone/",
    "🔃": "Emojis/iphone/",
    "🔄": "Emojis/iphone/",
    "🔅": "Emojis/iphone/",
    "🔆": "Emojis/iphone/",
    "🔇": "Emojis/iphone/",
    "🔈": "Emojis/iphone/",
    "🔉": "Emojis/iphone/",
    "🔊": "Emojis/iphone/",
    "🔋": "Emojis/iphone/",
    "🔌": "Emojis/iphone/",
    "🔍": "Emojis/iphone/",
    "🔎": "Emojis/iphone/",
    "🔏": "Emojis/iphone/",
    "🔐": "Emojis/iphone/",
    "🔑": "Emojis/iphone/",
    "🔒": "Emojis/iphone/",
    "🔓": "Emojis/iphone/",
    "🔔": "Emojis/iphone/",
    "🔕": "Emojis/iphone/",
    "🔖": "Emojis/iphone/",
    "🔗": "Emojis/iphone/",
    "🔘": "Emojis/iphone/",
    "🔙": "Emojis/iphone/",
    "🔚": "Emojis/iphone/",
    "🔛": "Emojis/iphone/",
    "🔜": "Emojis/iphone/",
    "🔝": "Emojis/iphone/",
    "🔞": "Emojis/iphone/",
    "🔟": "Emojis/iphone/",
    "🔠": "Emojis/iphone/",
    "🔡": "Emojis/iphone/",
    "🔢": "Emojis/iphone/",
    "🔣": "Emojis/iphone/",
    "🔤": "Emojis/iphone/",
    "🔥": "Emojis/iphone/",
    "🔦": "Emojis/iphone/",
    "🔧": "Emojis/iphone/",
    "🔨": "Emojis/iphone/",
    "🔩": "Emojis/iphone/",
    "🔪": "Emojis/iphone/emoji 348.png",
    "🔫": "Emojis/iphone/emoji 153.png",
    "🔬": "Emojis/iphone/",
    "🔭": "Emojis/iphone/",
    "🔮": "Emojis/iphone/",
    "🔯": "Emojis/iphone/",
    "🔰": "Emojis/iphone/",
    "🔱": "Emojis/iphone/",
    "🔲": "Emojis/iphone/",
    "🔳": "Emojis/iphone/",
    "🔴": "Emojis/iphone/",
    "🔵": "Emojis/iphone/",
    "🔶": "Emojis/iphone/",
    "🔷": "Emojis/iphone/",
    "🔸": "Emojis/iphone/",
    "🔹": "Emojis/iphone/",
    "🔺": "Emojis/iphone/",
    "🔻": "Emojis/iphone/",
    "🔼": "Emojis/iphone/",
    "🔽": "Emojis/iphone/",
    "🕉": "Emojis/iphone/",
    "🕊": "Emojis/iphone/",
    "🕋": "Emojis/iphone/",
    "🕌": "Emojis/iphone/",
    "🕍": "Emojis/iphone/",
    "🕎": "Emojis/iphone/",
    "🕐": "Emojis/iphone/",
    "🕑": "Emojis/iphone/",
    "🕒": "Emojis/iphone/",
    "🕓": "Emojis/iphone/",
    "🕔": "Emojis/iphone/",
    "🕕": "Emojis/iphone/",
    "🕖": "Emojis/iphone/",
    "🕗": "Emojis/iphone/",
    "🕘": "Emojis/iphone/",
    "🕙": "Emojis/iphone/",
    "🕚": "Emojis/iphone/",
    "🕛": "Emojis/iphone/",
    "🕜": "Emojis/iphone/",
    "🕝": "Emojis/iphone/",
    "🕞": "Emojis/iphone/",
    "🕟": "Emojis/iphone/",
    "🕠": "Emojis/iphone/",
    "🕡": "Emojis/iphone/",
    "🕢": "Emojis/iphone/",
    "🕣": "Emojis/iphone/",
    "🕤": "Emojis/iphone/",
    "🕥": "Emojis/iphone/",
    "🕦": "Emojis/iphone/",
    "🕧": "Emojis/iphone/",
    "🕯": "Emojis/iphone/",
    "🕰": "Emojis/iphone/",
    "🕳": "Emojis/iphone/",
    "🕴": "Emojis/iphone/",
    "🕵": "Emojis/iphone/",
    "🕶": "Emojis/iphone/",
    "🕷": "Emojis/iphone/",
    "🕸": "Emojis/iphone/",
    "🕹": "Emojis/iphone/",
    "🕺": "Emojis/iphone/emoji 3259.png",
    "🖇": "Emojis/iphone/",
    "🖊": "Emojis/iphone/",
    "🖋": "Emojis/iphone/",
    "🖌": "Emojis/iphone/",
    "🖍": "Emojis/iphone/",
    "🖐": "Emojis/iphone/",
    "🖕": "Emojis/iphone/",
    "🖖": "Emojis/iphone/",
    "🖤": "Emojis/iphone/",
    "🖥": "Emojis/iphone/",
    "🖨": "Emojis/iphone/",
    "🖱": "Emojis/iphone/",
    "🖲": "Emojis/iphone/",
    "🖼": "Emojis/iphone/",
    "🗂": "Emojis/iphone/",
    "🗃": "Emojis/iphone/",
    "🗄": "Emojis/iphone/",
    "🗑": "Emojis/iphone/",
    "🗒": "Emojis/iphone/",
    "🗓": "Emojis/iphone/",
    "🗜": "Emojis/iphone/",
    "🗝": "Emojis/iphone/",
    "🗞": "Emojis/iphone/",
    "🗡": "Emojis/iphone/",
    "🗣": "Emojis/iphone/",
    "🗨": "Emojis/iphone/",
    "🗯": "Emojis/iphone/",
    "🗳": "Emojis/iphone/",
    "🗺": "Emojis/iphone/",
    "🗻": "Emojis/iphone/",
    "🗼": "Emojis/iphone/",
    "🗽": "Emojis/iphone/",
    "🗾": "Emojis/iphone/",
    "🗿": "Emojis/iphone/",
    "🙅": "Emojis/iphone/",
    "🙆": "Emojis/iphone/",
    "🙇": "Emojis/iphone/",
    "🙈": "Emojis/iphone/",
    "🙉": "Emojis/iphone/",
    "🙊": "Emojis/iphone/",
    "🙋": "Emojis/iphone/",
    "🙌": "Emojis/iphone/emoji 3411.png",
    "🙌🏻": "Emojis/iphone/emoji 3411.png",
    "🙍": "Emojis/iphone/",
    "🙎": "Emojis/iphone/",
    "🙏": "Emojis/iphone/emoji 2854.png",
    "🚀": "Emojis/iphone/",
    "🚁": "Emojis/iphone/",
    "🚂": "Emojis/iphone/",
    "🚃": "Emojis/iphone/",
    "🚄": "Emojis/iphone/",
    "🚅": "Emojis/iphone/",
    "🚆": "Emojis/iphone/",
    "🚇": "Emojis/iphone/",
    "🚈": "Emojis/iphone/",
    "🚉": "Emojis/iphone/",
    "🚊": "Emojis/iphone/",
    "🚋": "Emojis/iphone/",
    "🚌": "Emojis/iphone/",
    "🚍": "Emojis/iphone/",
    "🚎": "Emojis/iphone/",
    "🚏": "Emojis/iphone/",
    "🚐": "Emojis/iphone/",
    "🚑": "Emojis/iphone/",
    "🚒": "Emojis/iphone/",
    "🚓": "Emojis/iphone/",
    "🚔": "Emojis/iphone/",
    "🚕": "Emojis/iphone/",
    "🚖": "Emojis/iphone/",
    "🚗": "Emojis/iphone/",
    "🚘": "Emojis/iphone/",
    "🚙": "Emojis/iphone/",
    "🚚": "Emojis/iphone/",
    "🚛": "Emojis/iphone/",
    "🚜": "Emojis/iphone/",
    "🚝": "Emojis/iphone/",
    "🚞": "Emojis/iphone/",
    "🚟": "Emojis/iphone/",
    "🚠": "Emojis/iphone/",
    "🚡": "Emojis/iphone/",
    "🚢": "Emojis/iphone/",
    "🚣": "Emojis/iphone/",
    "🚤": "Emojis/iphone/",
    "🚥": "Emojis/iphone/",
    "🚦": "Emojis/iphone/",
    "🚧": "Emojis/iphone/",
    "🚨": "Emojis/iphone/",
    "🚩": "Emojis/iphone/",
    "🚪": "Emojis/iphone/",
    "🚫": "Emojis/iphone/",
    "🚬": "Emojis/iphone/",
    "🚭": "Emojis/iphone/",
    "🚮": "Emojis/iphone/",
    "🚯": "Emojis/iphone/",
    "🚰": "Emojis/iphone/",
    "🚱": "Emojis/iphone/",
    "🚲": "Emojis/iphone/",
    "🚳": "Emojis/iphone/",
    "🚴": "Emojis/iphone/",
    "🚵": "Emojis/iphone/",
    "🚶": "Emojis/iphone/",
    "🚷": "Emojis/iphone/",
    "🚸": "Emojis/iphone/",
    "🚹": "Emojis/iphone/",
    "🚺": "Emojis/iphone/",
    "🚻": "Emojis/iphone/",
    "🚼": "Emojis/iphone/",
    "🚽": "Emojis/iphone/",
    "🚾": "Emojis/iphone/",
    "🚿": "Emojis/iphone/",
    "🛀": "Emojis/iphone/",
    "🛁": "Emojis/iphone/",
    "🛂": "Emojis/iphone/",
    "🛄": "Emojis/iphone/",
    "🛅": "Emojis/iphone/",
    "🛋": "Emojis/iphone/",
    "🛌": "Emojis/iphone/",
    "🛍": "Emojis/iphone/",
    "🛎": "Emojis/iphone/",
    "🛏": "Emojis/iphone/",
    "🛐": "Emojis/iphone/",
    "🛑": "Emojis/iphone/",
    "🛒": "Emojis/iphone/",
    "🛕": "Emojis/iphone/",
    "🛠": "Emojis/iphone/",
    "🛡": "Emojis/iphone/",
    "🛢": "Emojis/iphone/",
    "🛣": "Emojis/iphone/",
    "🛤": "Emojis/iphone/",
    "🛥": "Emojis/iphone/",
    "🛩": "Emojis/iphone/",
    "🛫": "Emojis/iphone/",
    "🛬": "Emojis/iphone/",
    "🛰": "Emojis/iphone/",
    "🛳": "Emojis/iphone/",
    "🛴": "Emojis/iphone/",
    "🛵": "Emojis/iphone/",
    "🛶": "Emojis/iphone/",
    "🛷": "Emojis/iphone/",
    "🛸": "Emojis/iphone/",
    "🛹": "Emojis/iphone/",
    "🛺": "Emojis/iphone/",
    "🛻": "Emojis/iphone/",
    "🟠": "Emojis/iphone/",
    "🟡": "Emojis/iphone/",
    "🟢": "Emojis/iphone/",
    "🟣": "Emojis/iphone/",
    "🟤": "Emojis/iphone/",
    "🟥": "Emojis/iphone/",
    "🟦": "Emojis/iphone/",
    "🟧": "Emojis/iphone/",
    "🟨": "Emojis/iphone/",
    "🟩": "Emojis/iphone/",
    "🟪": "Emojis/iphone/",
    "🟫": "Emojis/iphone/",
    "🤍": "Emojis/iphone/emoji 457.png",
    "🤎": "Emojis/iphone/",
    "🤏": "Emojis/iphone/",
    "🤘": "Emojis/iphone/",
    "🤙": "Emojis/iphone/",
    "🤚": "Emojis/iphone/",
    "🤛": "Emojis/iphone/",
    "🤜": "Emojis/iphone/",
    "🤝": "Emojis/iphone/",
    "🤞": "Emojis/iphone/",
    "🤟": "Emojis/iphone/",
    "🤰": "Emojis/iphone/",
    "🤱": "Emojis/iphone/",
    "🤲": "Emojis/iphone/",
    "🤳": "Emojis/iphone/",
    "🤵": "Emojis/iphone/",
    "🤶": "Emojis/iphone/",
    "🤷": "Emojis/iphone/",
    "🤸": "Emojis/iphone/",
    "🤹": "Emojis/iphone/",
    "🤺": "Emojis/iphone/",
    "🤼": "Emojis/iphone/",
    "🤽": "Emojis/iphone/",
    "🤾": "Emojis/iphone/",
    "🤿": "Emojis/iphone/",
    "🥀": "Emojis/iphone/",
    "🥁": "Emojis/iphone/",
    "🥂": "Emojis/iphone/",
    "🥃": "Emojis/iphone/",
    "🥄": "Emojis/iphone/",
    "🥅": "Emojis/iphone/",
    "🥇": "Emojis/iphone/",
    "🥈": "Emojis/iphone/",
    "🥉": "Emojis/iphone/",
    "🥊": "Emojis/iphone/",
    "🥋": "Emojis/iphone/",
    "🥌": "Emojis/iphone/",
    "🥍": "Emojis/iphone/",
    "🥎": "Emojis/iphone/",
    "🥏": "Emojis/iphone/",
    "🥐": "Emojis/iphone/",
    "🥑": "Emojis/iphone/",
    "🥒": "Emojis/iphone/",
    "🥓": "Emojis/iphone/",
    "🥔": "Emojis/iphone/",
    "🥕": "Emojis/iphone/",
    "🥖": "Emojis/iphone/",
    "🥗": "Emojis/iphone/",
    "🥘": "Emojis/iphone/",
    "🥙": "Emojis/iphone/",
    "🥚": "Emojis/iphone/",
    "🥛": "Emojis/iphone/",
    "🥜": "Emojis/iphone/",
    "🥝": "Emojis/iphone/",
    "🥞": "Emojis/iphone/",
    "🥟": "Emojis/iphone/",
    "🥠": "Emojis/iphone/",
    "🥡": "Emojis/iphone/",
    "🥢": "Emojis/iphone/",
    "🥣": "Emojis/iphone/",
    "🥤": "Emojis/iphone/",
    "🥥": "Emojis/iphone/",
    "🥦": "Emojis/iphone/",
    "🥧": "Emojis/iphone/",
    "🥨": "Emojis/iphone/",
    "🥩": "Emojis/iphone/",
    "🥪": "Emojis/iphone/",
    "🥫": "Emojis/iphone/",
    "🥬": "Emojis/iphone/",
    "🥭": "Emojis/iphone/",
    "🥮": "Emojis/iphone/",
    "🥯": "Emojis/iphone/",
    "🥻": "Emojis/iphone/",
    "🥼": "Emojis/iphone/",
    "🥽": "Emojis/iphone/",
    "🥾": "Emojis/iphone/",
    "🥿": "Emojis/iphone/",
    "🦀": "Emojis/iphone/",
    "🦁": "Emojis/iphone/",
    "🦂": "Emojis/iphone/",
    "🦃": "Emojis/iphone/",
    "🦄": "Emojis/iphone/",
    "🦅": "Emojis/iphone/",
    "🦆": "Emojis/iphone/",
    "🦇": "Emojis/iphone/",
    "🦈": "Emojis/iphone/emoji 2730.png",
    "🦉": "Emojis/iphone/",
    "🦊": "Emojis/iphone/",
    "🦋": "Emojis/iphone/",
    "🦌": "Emojis/iphone/",
    "🦍": "Emojis/iphone/",
    "🦎": "Emojis/iphone/",
    "🦏": "Emojis/iphone/",
    "🦐": "Emojis/iphone/",
    "🦑": "Emojis/iphone/",
    "🦒": "Emojis/iphone/",
    "🦓": "Emojis/iphone/",
    "🦔": "Emojis/iphone/",
    "🦕": "Emojis/iphone/",
    "🦖": "Emojis/iphone/",
    "🦗": "Emojis/iphone/",
    "🦘": "Emojis/iphone/",
    "🦙": "Emojis/iphone/",
    "🦚": "Emojis/iphone/",
    "🦛": "Emojis/iphone/",
    "🦜": "Emojis/iphone/",
    "🦝": "Emojis/iphone/",
    "🦞": "Emojis/iphone/",
    "🦟": "Emojis/iphone/",
    "🦠": "Emojis/iphone/",
    "🦡": "Emojis/iphone/",
    "🦢": "Emojis/iphone/",
    "🦥": "Emojis/iphone/",
    "🦦": "Emojis/iphone/",
    "🦧": "Emojis/iphone/",
    "🦨": "Emojis/iphone/",
    "🦩": "Emojis/iphone/",
    "🦪": "Emojis/iphone/",
    "🦮": "Emojis/iphone/",
    "🦯": "Emojis/iphone/",
    "🦰": "Emojis/iphone/",
    "🦱": "Emojis/iphone/",
    "🦲": "Emojis/iphone/",
    "🦳": "Emojis/iphone/",
    "🦴": "Emojis/iphone/",
    "🦵": "Emojis/iphone/",
    "🦶": "Emojis/iphone/",
    "🦷": "Emojis/iphone/emoji 2826.png",
    "🦸": "Emojis/iphone/",
    "🦹": "Emojis/iphone/",
    "🦺": "Emojis/iphone/",
    "🦻": "Emojis/iphone/",
    "🦼": "Emojis/iphone/",
    "🦽": "Emojis/iphone/",
    "🦾": "Emojis/iphone/",
    "🦿": "Emojis/iphone/",
    "🧀": "Emojis/iphone/",
    "🧁": "Emojis/iphone/",
    "🧂": "Emojis/iphone/",
    "🧃": "Emojis/iphone/",
    "🧄": "Emojis/iphone/",
    "🧅": "Emojis/iphone/",
    "🧆": "Emojis/iphone/",
    "🧇": "Emojis/iphone/",
    "🧈": "Emojis/iphone/",
    "🧉": "Emojis/iphone/",
    "🧊": "Emojis/iphone/",
    "🧍": "Emojis/iphone/",
    "🧎": "Emojis/iphone/",
    "🧏": "Emojis/iphone/",
    "🧑": "Emojis/iphone/",
    "🧒": "Emojis/iphone/",
    "🧔": "Emojis/iphone/",
    "🧕": "Emojis/iphone/",
    "🧖": "Emojis/iphone/",
    "🧗": "Emojis/iphone/",
    "🧘": "Emojis/iphone/",
    "🧙": "Emojis/iphone/",
    "🧚": "Emojis/iphone/",
    "🧛": "Emojis/iphone/",
    "🧜": "Emojis/iphone/",
    "🧝": "Emojis/iphone/",
    "🧞": "Emojis/iphone/",
    "🧟": "Emojis/iphone/",
    "🧠": "Emojis/iphone/",
    "🧡": "Emojis/iphone/",
    "🧢": "Emojis/iphone/",
    "🧣": "Emojis/iphone/",
    "🧤": "Emojis/iphone/",
    "🧥": "Emojis/iphone/",
    "🧦": "Emojis/iphone/",
    "🧧": "Emojis/iphone/",
    "🧨": "Emojis/iphone/",
    "🧩": "Emojis/iphone/",
    "🧪": "Emojis/iphone/",
    "🧫": "Emojis/iphone/",
    "🧬": "Emojis/iphone/",
    "🧭": "Emojis/iphone/",
    "🧮": "Emojis/iphone/",
    "🧯": "Emojis/iphone/",
    "🧰": "Emojis/iphone/",
    "🧱": "Emojis/iphone/",
    "🧲": "Emojis/iphone/",
    "🧳": "Emojis/iphone/",
    "🧴": "Emojis/iphone/",
    "🧵": "Emojis/iphone/",
    "🧶": "Emojis/iphone/",
    "🧷": "Emojis/iphone/",
    "🧸": "Emojis/iphone/",
    "🧹": "Emojis/iphone/",
    "🧺": "Emojis/iphone/",
    "🧻": "Emojis/iphone/",
    "🧼": "Emojis/iphone/",
    "🧽": "Emojis/iphone/",
    "🧾": "Emojis/iphone/",
    "🧿": "Emojis/iphone/",
    "🩰": "Emojis/iphone/",
    "🩱": "Emojis/iphone/",
    "🩲": "Emojis/iphone/",
    "🩳": "Emojis/iphone/",
    "🩸": "Emojis/iphone/",
    "🩹": "Emojis/iphone/",
    "🩺": "Emojis/iphone/",
    "🪀": "Emojis/iphone/",
    "🪁": "Emojis/iphone/",
    "🪂": "Emojis/iphone/",
    "🪐": "Emojis/iphone/",
    "🪑": "Emojis/iphone/",
    "🪒": "Emojis/iphone/",
    "🪓": "Emojis/iphone/",
    "🪔": "Emojis/iphone/",
    "🪕": "Emojis/iphone/",
    "\U000e0062": "Emojis/iphone/",
    "\U000e0063": "Emojis/iphone/",
    "\U000e0065": "Emojis/iphone/",
    "\U000e0067": "Emojis/iphone/",
    "\U000e006c": "Emojis/iphone/",
    "\U000e006e": "Emojis/iphone/",
    "\U000e0073": "Emojis/iphone/",
    "\U000e0074": "Emojis/iphone/",
    "\U000e0077": "Emojis/iphone/",
    "\U000e007f": "Emojis/iphone/",
}
