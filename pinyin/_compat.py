import sys
py2 = sys.version_info < (3, 0)


if py2:
    str_type = unicode

    def u(s):
        if not isinstance(s, unicode):
            s = unicode(s, "utf-8")
        return s

else:
    str_type = str

    def u(s):
        return s
