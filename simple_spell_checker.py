from newspaper import Article
from pyaspeller import Word

file_word_list = []
article_word_list = []

# add exception for non-text files
# filename is the location of the file
def open_file(filename):
    with open(filename, 'r') as file:
        sentences = file.readlines()
        for sentence in sentences:
            file_word_list.extend(sentence.split())

    return file_word_list


def download_article(input_url):

    # input URL
    my_article = Article(input_url, language='en')

    # Extracting the Article Content
    my_article.download()
    my_article.parse()

    # text of the article
    full_text = my_article.text

    # split the article into a list of words
    article_word_list = full_text.split()

    return article_word_list


def check_text(word_list):

    misspelt_words = []

    for word in word_list:
        check = Word(word)
        val = check.correct
        if not val:
            print('Unrecognized word: ' + word)
            if check.spellsafe == None:
                print('Suggested edits: ' + str(check.spellsafe))
            else:
                print('Did you mean: ' + str(check.variants))
            # misspelt_words.append(word)

    # return misspelt_words


def check_word(one_word):

    check = Word(one_word)
    if not check.correct:
        print('Incorrect word: ' + one_word)
        print('Did you mean: ' + check.variants)


def give_article_suggestions():
    pass


# test for online articles
# url = 'https://hackernoon.com/dilemmas-of-a-digital-lifestyle-27c044940157'

# words = download_article(url)
# print(check_text(words))

# test for text files
file_words = open_file('consider_reading.txt')
check_text(file_words)

# test for words
# check_word('peeple')
