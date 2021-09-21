wordList = []
with open("3000word.txt") as file:
    wordList = [line.strip() for line in file]

class CrackCaesarCipher:
    def __init__(self, text):
        self.text = text
        self._lenght_text = len(text)
        self.result = []
    def crack(self):
        
        for i in range(1, 27):
            b_text_encrypt = self.decrypt(i).lower()
            wordIn = self.wordBreak(b_text_encrypt)
            self.result.append({
                'index': i,
                'scores': len(wordIn),
                'text': b_text_encrypt,
                'wordIn': wordIn
            })

    def wordBreak(self, s):
        wordIn = []
        for word in wordList:
            if(s.find(word) >= 0):
                wordIn.append(word)
        return wordIn

    def presult(self):
        newList = sorted(self.result , key=lambda k: k['scores'], reverse=True) 
        for i in newList:
            print("key - {}, scores - {}, word list - {}, text - {}".format(i['index'], i['scores'], i['wordIn'], i['text']))

    def decrypt(self, key):
        result = ''
        for i in range(self._lenght_text):
            char = self.text[i]
            if (char.isupper()):
                result += chr((ord(char) - key - 65) % 26 + 65)
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
        return result


message = "Sxkwxcyxdsbon"
crack = CrackCaesarCipher(text=message)
crack.crack()
crack.presult()
