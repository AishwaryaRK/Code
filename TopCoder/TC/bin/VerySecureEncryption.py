class VerySecureEncryption:
    def encrypt(self, message, key, K):
        message = list(message)
        for n in range(0, K):
            tempMsg = "".join(message)
            for i, a in enumerate(tempMsg):
                message[key[i]] = a
        return "".join(message)


print VerySecureEncryption().encrypt("uogcodlk", (4, 3, 6, 2, 5, 1, 0, 7), 44)
