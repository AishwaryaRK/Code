class Hexspeak:
    def decode(self, ciphertext):
        hexadecimalMap={0:'O',1:'I',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        code = ""
        quotient = ciphertext
        hexadecimal = 16
        while quotient > 0:
            digit = quotient % hexadecimal
            if 2 <= digit <= 9:
                return "Error!"
            code = hexadecimalMap[digit]+code
            quotient = int(quotient / hexadecimal)
        return code

        # hexadecimal= hex(ciphertext)[2:].upper()
        # hexadecimal.replace('1', 'I')
        # hexadecimal.replace('0', 'O')
        # return hexadecimal


print Hexspeak().decode(999994830345994239)
