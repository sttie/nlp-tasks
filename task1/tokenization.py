def get_words(text):
    words = []
    word = ""

    for line in text.split("\n"):
        if len(word) > 0:
            words.append(word)
            word = ""

        for i in range(len(line)):
            if line[i] in [",", ".", "!", "?"]:
                assert len(word) > 0, word
                words.append(word)
                word = ""
            elif line[i] in [" "]:
                if len(word) > 0:
                    words.append(word)
                    word = ""
            else:
                word += line[i]

    return words

class Token:
    def __init__(self, form, primary_form, part_of_speech):
        self.form = form
        self.primary_form = primary_form
        self.part_of_speech = part_of_speech

    def __repr__(self):
        return f"{self.form}{{{self.primary_form}={self.part_of_speech}}}"

def get_token(forms, form):
    word = forms[form.upper()]
    return Token(form, word.primary_form, word.tags[0])

def tokenizate(forms, text):
    words = get_words(text)
    tokens = []

    for form in words:
        token = get_token(forms, form)
        tokens.append(token)

    return tokens
