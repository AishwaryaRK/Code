class IdentifyingWood:
    def check(self, s, t):
        s=sorted(s)
        t=sorted(t)
        for c in t:
            if c in s:
                s.remove(c)
            else:
                return "Nope."
        return "Yep, it's wood."

IdentifyingWood().check("xoxoxoxo","ooxxoo")