class CapitalizedWord:
    def __init__(self, word: str):
        self.word = word
        self.capitalize = False


class Sentence:
    def __init__(self, plain_text):
        self.words = [CapitalizedWord(word) for word in plain_text.split(" ")]

    def __getitem__(self, idx):
        return self.words[idx]

    def __str__(self):
        return " ".join(
            [word.word.upper() if word.capitalize else word.word for word in self.words]
        )


if __name__ == "__main__":
    sentence = Sentence("hello world")
    sentence[1].capitalize = True
    print(sentence)