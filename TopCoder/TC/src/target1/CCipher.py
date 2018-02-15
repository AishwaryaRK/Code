import string


class CCipher:
    def decode(self, cipherText, shift):
        alphabets = string.ascii_uppercase
        decoded_text = ""
        for c in cipherText:
            decoded_text += alphabets[((ord(c) - ord('A')) + 26 - shift) % 26]
        return decoded_text


print(CCipher().decode("VQREQFGT", 2))
