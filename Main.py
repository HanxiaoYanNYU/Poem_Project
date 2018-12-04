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

decision, score = ScoreHelper.estimate_sentiment(poem_collection[8].text, False)
print("the decision is : " + decision)
print(score)

