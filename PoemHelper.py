import re
from Project import Poems
from ScoreHelper import ScoreHelper


class PoemHelper:

    @staticmethod
    def read_text(path, mode):
        file = open(path, mode)
        return file

    @staticmethod
    def create_poems(file):
        lines = file.readlines()
        poem_collection = []

        for l in lines:
            l.rstrip()
            result = re.search('^POEM:\s(.+)AUTHOR:\s(.+)$', l)
            if result is not None:
                poem_collection.append(Poems())
                poem_collection[-1].title = result.group(1).rstrip()
                poem_collection[-1].author = result.group(2).rstrip()
            else:
                if l.strip():
                    poem_collection[-1].text += l
                    poem_collection[-1].numberLines += 1

        return poem_collection

    @staticmethod
    def get_smallest_poem(poem_collection):
        smallest_poem_name = ''
        smallest_poem_line = -1

        if len(poem_collection) == 0:
            print('There is no poems read from text file')
        else:
            smallest_poem_name = poem_collection[0].title
            smallest_poem_line = poem_collection[0].numberLines

            for poem in poem_collection:
                if poem.numberLines < smallest_poem_line:
                    smallest_poem_name = poem.title
                    smallest_poem_line = poem.numberLines

        return "smallest_poem_name: {}, its line number is: {}".format(smallest_poem_name, smallest_poem_line)

    @staticmethod
    def generate_poem_score(poem_collection):
        for poem in poem_collection:
            decision, score = ScoreHelper.estimate_sentiment(poem.text, False)
            poem.score = score
        return poem_collection

    @staticmethod
    def sort_poem_lowToHigh(poem_collection):
        sorted_poems = sorted(poem_collection, key=lambda x: x.score, reverse=False)
        return sorted_poems

    def create_word_dict(self, poems):
        pass

    @staticmethod
    def check_string(string, word_dict):
        error_message = ''
        punctuation_check = '[!"\',.:?]+'
        capitalletter_check = '[A-Z]+'

        if len(string) < 7 or len(string) > 9:
            error_message += 'input string length should be in range [7,10), but is {}. '.format(len(string))

        if re.search(punctuation_check, string) is None:
            error_message += 'input string has no punctuation. '

        if re.search(capitalletter_check, string) is None:
            error_message += 'input string has no capital letter. '

        if word_dict.get(string) is None:
            error_message += 'input string does not exist in any poem.'

        if error_message is '':
            return [True, 'input string correct']
        else:
            return [False, error_message]

    @staticmethod
    def wordtrain(word, limit):
        if len(word) >= limit:
            return word

        last_letter = word[-1]
        next_letter = findNext(last_letter)
        word += ' ' + next_letter

        wordtrain(word, limit)

    def findNext(self, letter):
        pass







