
"""This class contains functions to preprocess the text
@author: Diem BUI
@Date  : 03/08/2020 : Add the following functions:
1) remove non alpha numeric letters
2) remove the punctuation
3) find the email address in the text

Returns:
    [type]: [description]
"""

import re
import string

def remove_non_alphameric_character(text):
    """remove alpha numerical words and make lowercase

    Args:
        text ([string]): [a text without being processed]

    Returns:
        [string]: [a text without non]
    """
    non_alpha_char_re = re.compile('[^a-zA-Z0-9 ]')
    return non_alpha_char_re.sub('', text.strip().lower())


def remove_punctuation(text):
    """remove punctuations in the text such as : (. , : ; ‘ “ ? !)

    Args:
        text ([type]): [description]

    Returns:
        [type]: [description]
    """
    punc_re = re.compile('[%s]' % re.escape(string.punctuation))
    return punc_re.sub('', text)

def find_email_address(text):
    """Find the email addresses hidden the text

    Args:
        text ([type]): [description]
    """

    email_re =re.compile('^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$')
    return email_re.findall(text)


if __name__ == "__main__":
    # test remove_non_alphameric_character()
    text = "this text contains # the non * alpha $ numeric letters"
    print(remove_non_alphameric_character(text))

    # test remove_punctuation()
    text = "this text contains , some punctuation."
    print(remove_punctuation(text))

    text ="this text contains email address from phillip.allen@enron.com to david.delainey@enron.com"
    print(find_email_address(text))