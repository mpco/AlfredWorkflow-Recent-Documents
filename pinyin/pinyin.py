# -*- coding: utf-8 -*-

import os
import itertools
import unicodedata

from ._compat import u

__all__ = ['get', 'get_pinyin', 'get_initial']


# init pinyin dict
pinyin_dict = {}
pinyin_tone = {}
dat = os.path.join(os.path.dirname(__file__), "Mandarin.dat")
with open(dat) as f:
    for line in f:
        k, v = line.strip().split('\t')
        pinyin_dict[k] = u(v.lower().split(" ")[0][:-1])
        pinyin_tone[k] = int(v.lower().split(" ")[0][-1])


def _pinyin_generator(chars, format):
    """Generate pinyin for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    for char in chars:
        key = "%X" % ord(char)
        pinyin = pinyin_dict.get(key, char)
        tone = pinyin_tone.get(key, 0)

        if tone == 0 or format == "strip":
            pass
        elif format == "numerical":
            pinyin += str(tone)
        elif format == "diacritical":
            # Find first vowel -- where we should put the diacritical mark
            vowels = itertools.chain((c for c in pinyin if c in "aeo"),
                                     (c for c in pinyin if c in "iuv"))
            vowel = pinyin.index(next(vowels)) + 1
            pinyin = pinyin[:vowel] + tonemarks[tone] + pinyin[vowel:]
        else:
            error = "Format must be one of: numerical/diacritical/strip"
            raise ValueError(error)

        yield unicodedata.normalize('NFC', pinyin)


def get(s, delimiter='', format="diacritical"):
    """Return pinyin of string, the string must be unicode
    """
    return delimiter.join(_pinyin_generator(u(s), format=format))


def get_pinyin(s):
    """This function is only for backward compatibility, use `get` instead.
    """
    import warnings
    warnings.warn('Deprecated, use `get` instead.')
    return get(s)


def get_initial(s, delimiter=' '):
    """Return the 1st char of pinyin of string, the string must be unicode
    """
    initials = (p[0] for p in _pinyin_generator(u(s), format="strip"))
    return delimiter.join(initials)

tonemarks = ["", u("̄"), u("́"), u("̌"), u("̀"), ""]
