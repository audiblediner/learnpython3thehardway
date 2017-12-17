import sys
import re
from collections import defaultdict

def read_file(filename):
    input_file = open(filename, 'rU')
    text = input_file.read()
    input_file.close()
    return text

def split_into_sentences(text):
    sentences = re.findall("[A-Z].*?[\.!?]", text, re.MULTILINE | re.DOTALL )
    return sentences

def count_words(text):
    word_count = defaultdict(int)
    for word in text.split():
        word = word.lower()
        word_count[word] = word_count[word] + 1
    return word_count

def calculate_average_sentence_length(text):
    sentences = split_into_sentences(text)
    total = 0
    for sentence in sentences:
        total += len(sentence)
    average = total / float(len(sentences))
    return average

def print_words_in_descending_frequency(text):
    word_count = count_words(text)
    items = sorted (word_count.items(), key=lambda a:a[-1], reverse=True)
    for item in items:
        print "List of words in descending frequency: %s, %s" % (item[0], item[1])


def main():

    if len(sys.argv) != 3:
        print 'usage: ./.py {--count | --brownies} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    text = read_file(filename)

    if option == '--count':
        word_count = count_words(text)
        sentences = split_into_sentences(text)
        print "Total word count: %s" % str(sum(word_count.values()))
        print "Unique words: %s" % str(len(word_count))
        print "Sentences: %s" % str(len(sentences))

    elif option == '--brownies':
        average = calculate_average_sentence_length(text)
        print "Average sentence length: %s" % str(average)
        print "Words in descending order:"
        print_words_in_descending_frequency(text)

    else:
        print 'unknown option: ' + option
        sys.exit(1)

if __name__ == '__main__':
    main()
