

class Word:
    def __init__(self, source_text: str, word_searched: str):
        self.source_text = source_text.split()
        self.word_searched = word_searched
        self.source_text_reshaped = self.reformat()
        self.report = self.report()

    def reformat(self):
        box = []
        for word in self.source_text:
            # Textos comuns
            if word.isalnum():
                box.append(word)
            # 's (posse no inglês) é ignorado e não excluído pela função isalnum
            if not word.isalnum() and "'s" in word:
                box.append(word)
            # Outros símbolos além de 's são tratados, removendo (ex: Kahn. se torna Kahn)
            if not word.isalnum() and "'s" not in word:
                # print(f'-> {word}', "'s" in word)
                box.append(word[0:len(word) - 1])
        return box

    def report(self):
        box = []
        for pos, each_word in enumerate(self.source_text_reshaped):
            if each_word == self.word_searched:
                box.append((each_word, pos))
        return box


if __name__ == '__main__':
    text = """
    Rain fights valiantly for the emperor Shao Kahn. But it would be Kahn's own step daughter, the Princess Kitana, who
    turns Rain against him. Like Kitana, Rain's origins also come from their former realm of Edenia. He learns that his
    father was once a general in Edenia's army and died at the hands of Shao Kahn himself. Enraged at the truth of his
    history, he joins Kitana in aligning with the Earthrealm warriors. But his allegiance comes under question when he
    mysteriously disappears during an extermination squad attack. To prove his loyalty, he embarked on a suicide mission
    to destroy Shao Kahn and end the menace once and for all."""

    word = Word(source_text=text, word_searched='the')
    print(word.source_text_reshaped)
    print(word.report)
