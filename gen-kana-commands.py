from itertools import chain


def orange(ostart, oend, step=1):
    """
    Iterate in octal over range <ostart>, <oend> with stride <ostep>
    """
    dstart = int(ostart, 8)
    dend = int(oend, 8)

    return [oct(i) for i in range(dstart, dend, step)]


def orange_inclusive(ostart, oend, step=1):
    """
    Iterate in octal over range <ostart>, <oend> with stride <ostep>
    """
    return orange(ostart, oct(int(oend, 8) + 1), step=step)


def def_tex(char, num):
    """
    Define the latex command that adds <char> as a unicode character
    referencing point <num> in the udmj30 font table.

    <num> should be an octal string of the form `0o<x>`



    """
    # Remove the leading `0o` and pad with zeros
    print(num)
    num = num[2:].zfill(3)

    out_str = (
        r"\newunicodechar{"
        + char
        + r"}{\text{\usefont{U}{min}{m}{n}\symbol{'"
        + num
        + "}}}\n"
    )
    return out_str


with open("out.txt", "w") as f:
    nums1 = orange_inclusive("0o001", "0o007")
    ps1 = "、。〃　々乄〇"

    nums2 = orange_inclusive("0o010", "0o017")
    ps2 = "〈〉《》「」『』"

    nums3 = orange_inclusive("0o020", "0o025")
    ps3 = "【】〒〓〔〕"

    nums4 = ["0o034"]
    ps4 = "〜"

    nums5 = orange_inclusive("0o101", "0o223")
    ps5 = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎゐゑをん"

    nums6 = orange_inclusive("0o223", "0o236")
    ps6 = "゛゜ゝゞ"

    nums7 = orange_inclusive("0o241", "0o366")
    ps7 = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮヰヱヲンヴヵヶ"

    nums8 = orange_inclusive("0o373", "0o376")
    ps8 = "・ーヽヾ"

    pairs = chain.from_iterable(
        [
            zip(ps1, nums1),
            zip(ps2, nums2),
            zip(ps3, nums3),
            zip(ps4, nums4),
            zip(ps5, nums5),
            zip(ps6, nums6),
            zip(ps7, nums7),
        ]
    )

    out_str = ""
    for (char, num) in pairs:
        out_str += def_tex(char, num)

    print(out_str)

    f.write(out_str)
