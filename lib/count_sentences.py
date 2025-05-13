
import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Use the setter for initial assignment

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")


    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        split_sentences = re.split(r'[.!?]+', self.value)
        sentences = [s for s in split_sentences if s.strip()]
        return len(sentences)
