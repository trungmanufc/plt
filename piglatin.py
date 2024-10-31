class PigLatin:

    def __init__(self, phrase: str):
        self.phase = phrase

    def get_phrase(self) -> str:
        return self.phase

    def translate(self) -> str:
        if self.get_phrase() == '':
            return "nil"
