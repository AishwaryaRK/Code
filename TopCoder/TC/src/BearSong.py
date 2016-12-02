class BearSong:
    def countRareNotes(self, notes):
        return len([e for e in notes if notes.count(e)==1])



print BearSong().countRareNotes((9,10,7,8,9))
