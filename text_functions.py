
"""This class contains functions to preprocess the text
@author: Diem BUI
@Creation Date : 03/08/2020 : Add the following functions:
1) remove non alpha numeric letters
2) remove the punctuation
3) remove english stop words in the text
4) Create CleanText class
"""

import re
import string
import nltk
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
from nltk import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

from nltk.stem import wordnet

from nltk import pos_tag


class CleanText:

    def __init__(self, text):
        self.text = text
    
    def remove_non_alphameric_character(self, text):
        """remove alpha numerical words and make lowercase

        Args:
            text ([string]): [a text without being processed]

        Returns:
            [string]: [a text without non alphabet]
        """
        non_alpha_char_re = re.compile('[^a-zA-Z0-9{$}]')
        return non_alpha_char_re.sub(' ', text.strip().lower())


    def remove_punctuation(self, text):
        """remove punctuations in the text such as : (. , : ; ‘ “ ? !)

        Args:
            text ([type]): [description]

        Returns:
            [type]: [description]
        """
        punc_re = re.compile('[%s]' % re.escape(string.punctuation))
        return punc_re.sub('', text)

    def remove_stop_words(self, text):
        nltk.download('stopwords', quiet=True)

        en_stopwords = set(stopwords.words('english'))
        tokenized_words = word_tokenize(text)
        return (" ".join([word for word in tokenized_words if word not in en_stopwords]))

    def get_wordnet_pos(self, tagged_word):
        """
        Translate part of speech into wordnet tag of speech
        """

        nltk.download('wordnet', quiet=True)

        if tagged_word.startswith('J'):
            return wn.ADJ
        elif tagged_word.startswith('V'):
            return wn.VERB
        elif tagged_word.startswith('N'):
            return wn.NOUN
        elif tagged_word.startswith('R'):
            return wn.ADV
        else:
            return wn.NOUN

    def lemmatizer(self, text):
        """
        Do the lematization for the text
        """
        nltk.download('wordnet', quiet=True)

        wn_lemmatizer = WordNetLemmatizer()
        tokenized_words = word_tokenize(text)
        # tag part of speech on each token
        tagged_pos = pos_tag(tokenized_words)
        wordnet_pos = [self.get_wordnet_pos(word[1]) for word in tagged_pos]
        return " ".join([wn_lemmatizer.lemmatize(pair[0], pair[1]) for pair in zip(tokenized_words, wordnet_pos)])

    def remove_forwarded_and_response(self, text):
        my_text = self._remove_forwarded(text)
        return self._remove_response(my_text)

    def _remove_forwarded(self, text):
        forwarded = "---------------------- Forwarded by"
        subject = 'Subject:'

        while forwarded in text:
            previous_text = text[:text.find(forwarded)]

            subject_index = text.find(forwarded) + text[text.find(forwarded):].find(subject)
            next_text = text[subject_index + text[subject_index:].find('\n') + 2:]

            text = previous_text + next_text
        return text

    def _remove_response(self, text):
        subject = 'Subject:'

        while 'To:' in text and 'cc:' in text and 'Subject:' in text:
            previous_text = text[:text.find('To:') - 2]
            # remove 2 trailling text between '\n'
            previous_text = previous_text[:previous_text.rfind('\n')]
            previous_text = previous_text[:previous_text.rfind('\n')]

            next_text = text[text.find(subject):]
            next_text = next_text[next_text.find('\n') + 2:]
            text = previous_text + next_text
        return text

    def remove_blank(self, text):
        return "".join([s for s in text.strip().splitlines(True) if s.strip()])

    def preprocessing(self):
        text = self.remove_stop_words(self.text)
        text = self.remove_punctuation(text)
        text = self.remove_non_alphameric_character(text)
        return self.lemmatizer(text)

if __name__ == "__main__":

    '''
    # test remove_non_alphameric_character()
    text = "this text contains # the non * alpha $ numeric letters"
    print(remove_non_alphameric_character(text))
    '''
    
    '''
    # test remove_punctuation()
    text = "this text contains , some punctuation."
    print(remove_punctuation(text))
    '''

    '''
    # test find_email_address()
    text ="this text contains email address from phillip.allen@enron.com to david.delainey@enron.com"
    print(find_email_address(text))
    '''

    '''
    # test remove_stop_words()
    text = "this text contains some stop words such as the, and, he, she, we"
    print(remove_stop_words(text))
    '''

    '''
    # test get_wordnet_pos()
    text = "Hidden Markov Models largely used to assign the correct label sequence to sequential data or assess the probability of a given label and data sequence"
    print(word_tokenize(text))
    tagged_pos_words = pos_tag(word_tokenize(text))
    print(",".join([get_wordnet_pos(word[1]) for word in tagged_pos_words]))
    #print(get_wordnet_pos( pos_tag(word_tokenize(text))))
    '''

    '''
    text = "NLTK is a leading platform for building Python programs to work with human language data"
    print(lemmatizer(remove_stop_words(text)))
    # Hidden Markov Models largely use to assign the correct label sequence to sequential data or assess the probability of a give label and data sequence
    '''

    text = "NLTK is a leading platform for building Python programs to work with human language data"
    cleantext = CleanText(text)
    print(cleantext.preprocessing())
