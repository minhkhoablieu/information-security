class CaesarCipher:
    def __init__(self, text, key):
        self.text = text
        self.key = key
        self._lenght_text = len(text)

    def encrypt(self):
        result = ''
        for i in range(self._lenght_text):
            char = self.text[i]
            if (char.isupper()):
                result += chr((ord(char) + self.key - 65) % 26 + 65)

            else:
                result += chr((ord(char) + self.key - 97) % 26 + 97)
        return result

    def decrypt(self):
        result = ''
        for i in range(self._lenght_text):
            char = self.text[i]
            if (char.isupper()):
                result += chr((ord(char) - self.key - 65) % 26 + 65)

            else:
                result += chr((ord(char) - self.key - 97) % 26 + 97)
        return result


message = "I am so tired"
key = 10
encrypt_message = CaesarCipher(text=message, key=key).encrypt()
print(encrypt_message)