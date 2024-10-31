class PigLatin:

    def __init__(self, phrase: str):
        self.phase = phrase

    def get_phrase(self) -> str:
        return self.phase

    def isVowel(self, ch ):
        return (0x208222 >> (ord(ch) & 0x1f)) & 1

    def translate(self) -> str:
        if self.get_phrase() == '':
            return "nil"
        else:
            if self.get_phrase()[-1] == 'y':
                return self.get_phrase() + 'nay'

            else:
                if self.isVowel(self.get_phrase()[-1]):
                    return self.get_phrase() + "yay"
                else:
                    return self.get_phrase() + "ay"

