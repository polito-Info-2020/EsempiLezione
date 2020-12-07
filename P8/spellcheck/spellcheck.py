##
#  This program checks which words in a file are not present in a list of
#  correctly spelled words.
#

def main():
    # Read the word list and the document.
    correctlySpelledWords = readWords("words", "")
    documentWords = readWords("alice30.txt", "*END*")  # Skip the prefix

    # Print all words that are in the document but not the word list.
    misspellings = documentWords.difference(correctlySpelledWords)
    for word in sorted(misspellings):
        print(word)


## Reads all words from a file.
#  @param filename the name of the file
#  @param skipUntil skip all lines until a line starts with this string
#  @return a set with all lowercased words in the file. Here, a word is a 
#  sequence of upper- and lowercase letters
#   
def readWords(filename, skipUntil):
    wordSet = set()
    inputFile = open(filename, "r")
    skip = True

    for line in inputFile:
        line = line.strip()
        if not skip:
            # Use any character other than a-z or A-Z as word delimiters.
            # parts = split("[^a-zA-Z]+", line)
            parts = extractWords(line)
            for word in parts:
                if len(word) > 0:
                    wordSet.add(word.lower())
        elif line.find(skipUntil) >= 0:
            skip = False

    inputFile.close()
    return wordSet


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
