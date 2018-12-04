import re
from Project import Poems


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

    def generate_poem_score(self, poems):
        pass

    def create_word_dict(self, poems):
        pass

    def check_string(self, string):
        pass

