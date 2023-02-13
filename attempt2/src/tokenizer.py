import re
from io import TextIOWrapper


class Tokenizer:

    def __init__(self, file: TextIOWrapper):
        '''
        Text tokenizer and cleaner
        '''
        self.__file = file

    def clean_text(self) -> str:
        text = str(self.__file.read()).lower()

        text = self.__remove_links(text)
        text = self.__replace_chars(text)
        text = self.__remove_stop_words(text)

        text = re.sub(r' +', ' ', text)
        text = re.sub(r' .{1,2} ', '', text)

        return text.strip()

    def __remove_stop_words(self, text):
        with open('data/stop_words.txt', 'r', encoding='utf-8') as fp:
            words = [word[:-1] for word in fp.readlines()]
            pattern = r"\b({})\b".format('|'.join(words))
            return re.sub(pattern, '', text)

    def __remove_links(self, text: str) -> str:
        pattern = r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)'
        return re.sub(pattern, ' ', text)

    def __replace_chars(self, text: str) -> str:
        pattern = r'[^A-Za-z ]'
        return re.sub(pattern, ' ', text)