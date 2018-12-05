import re
from PoemHelper import PoemHelper
from Project import Poems
from ScoreHelper import ScoreHelper


class Main:

    path = '/Users/YHX/Documents/CodeHome/venv/Poem_Project/resource/Poems_new_2018.txt'
    mode = 'r'
    file = PoemHelper.read_text(path, mode)


m = Main()
poem_collection = PoemHelper.create_poems(m.file)

