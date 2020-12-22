##
#  This program counts the number of unique words contained in a text document.
#

DEFAULT_FILENAME = 'nurseryrhyme.txt'

def main():
    uniqueWords = set()

    filename = input(f"Enter filename (default: {DEFAULT_FILENAME}): ")
    if len(filename) == 0:
        filename = DEFAULT_FILENAME
    inputFile = open(filename, "r")

    for line in inputFile:
        theWords = extractWords(line)
        for word in theWords:
            if len(word) > 0:
                uniqueWords.add(word.lower())

    print("The document contains", len(uniqueWords), "unique words.")

## Split a line into its words
# Returns a list of strings, each string is an individual word
# Words may be separated by ANY character (spaces, numbers, punctuation, ...)
# All non-alpha characters act as delimiters. Multiple delimiters are merged (they count as one).
def extractWords(line):
    words = []
    i = 0
    while i < len(line):
        # get a consecutive sequence of alphabetic characters
        word = ''
        while i < len(line) and line[i].isalpha():
            word = word + line[i]
            i += 1
        if len(word) > 1:
            words.append(word)

        # now skip all non-alpha characters
        while i < len(line) and not line[i].isalpha():
            i += 1
    return words


# Start the program.
main()
