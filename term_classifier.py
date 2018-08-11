from nltk import pos_tag

class TermClassifier():

    def is_verb(self, word):
        if not word:
            return False
        pos_info = pos_tag([word])

        return pos_info[0][1] == 'VB'

    def is_noun(self, word):
        if not word:
            return False
        pos_info = pos_tag([word])

        return pos_info[0][1] == 'NN'

    def is_number(self, string):
        return str(string).isdigit()