
# Each .txt or .html file can be represent as a Document class.

import PorterStemmer as ps


class Document:
    def __init__(self, url, doc_id, file_name, file_type, stop_words):
        self.url = url
        self.doc_id = doc_id
        self.name = file_name
        self.type = file_type
        self.title = ''
        self.f_name = ''
        self.s_name = ''
        self.term = dict()          # key: term, value: frequency
        self.stop_words = stop_words

    def filter(self):
        # Filter abnormal terms.
        # All words already don't contain space.
        punctuation = [':', '.', '!', '?', ',', '\'', '\"']
        self.f_name = self.name.split('.')[0] + '_filtered.txt'
        with open(self.name, encoding='utf-8') as f:
            done = 0
            while not done:
                word = f.readline().lower()
                word = word[:len(word)-1]
                if word == '':  # Reach the end of the file.
                    break
                if word[0] in punctuation:
                    word = word[1:]
                    if len(word) == 0:
                        continue
                if word[len(word) - 1] in punctuation:
                    word = word[:len(word)-1]
                if word[0].isalpha():
                    if word[len(word)-1].isalpha() or word[len(word)-1].isdigit():
                        with open(self.f_name, 'a', encoding='utf-8') as o:
                            o.write(word + '\n')

    def stem(self):
        stemmer = ps.PorterStemmer()
        # Stem the words and write in a new file.
        self.s_name = self.name.split('.')[0] + '_stemmed.txt'
        with open(self.f_name, encoding='utf-8') as f:
            done = 0
            while not done:
                word = f.readline()
                word = word[:len(word)-1]
                if word == '':
                    break
                word = stemmer.stem(word, 0, len(word)-1)
                with open(self.s_name, 'a', encoding='utf-8') as o:
                    o.write(word + '\n')

    def collection(self):
        # get every term in the stemmed .txt file and store them in a dictionary with frequency as value.
        with open(self.s_name, encoding='utf-8') as f:
            for word in f.readlines():
                word = word[:len(word)-1]
                if word not in self.stop_words:
                    if word in self.term:
                        self.term[word] += 1
                    else:
                        self.term[word] = 1

    def set_title(self, title):
        self.title = title

    def get_term(self):
        return self.term

    def get_id(self):
        return self.doc_id

    def get_url(self):
        return self.url

    def get_title(self):
        return self.title