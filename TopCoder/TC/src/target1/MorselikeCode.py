class MorselikeCode:
    def decrypt(self, library, message):
        decoded_msg = []
        ms = message.split(' ')
        for m in ms:
            dm = '?'
            for l in library:
                if l.split(' ')[1] == m:
                    dm = l.split(' ')[0]
                    break
            decoded_msg.append(dm)
        return "".join(decoded_msg)


print(MorselikeCode().decrypt(["H -", "E .", "L --", "L ..", "O -."], "- . -- .. -."))
