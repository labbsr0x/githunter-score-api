import re

import unidecode
import random
import string


def clean(word: str): return unidecode.unidecode(re.sub(r'\W+', '', word))


def random_string(size=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(size))
