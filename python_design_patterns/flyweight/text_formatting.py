class Formatted_Text:
    def __init__(self, plain_text) -> None:
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)

    def capitalize(self, start, end):
        for idx in range(start, end):
            self.caps[idx] = True

    def __str__(self):
        result = []
        for idx, character in enumerate(self.plain_text):
            if self.caps[idx]:
                result.append(character.upper())
            else:
                result.append(character)
        return "".join(result)


class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        this_range = self.TextRange(start, end)
        self.formatting.append(this_range)
        return this_range

    def __str__(self):
        result = []
        for idx, character in enumerate(self.plain_text):
            for this_range in self.formatting:
                if this_range.covers(idx):
                    result.append(character.upper())
                else:
                    result.append(character)
        return "".join(result)


if __name__ == "__main__":
    text = "This is a brave new world."
    formatted_text = Formatted_Text(text)
    formatted_text.capitalize(start=10, end=15)
    print(formatted_text)

    bft = BetterFormattedText(text)
    bft.get_range(16, 19).capitalize = True
    print(bft)