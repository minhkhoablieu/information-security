class ReverseCipher:
    def __init__(self, text):
        self.text = text
        
    def encrypt(self):
        return self.text[::-1]

    def decrypt(self):
        return self.text[::-1]

message = ReverseCipher("olleH").decrypt()
print(message)