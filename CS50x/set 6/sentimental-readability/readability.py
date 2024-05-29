from cs50 import get_string
import re

input_sentence = get_string("Text: ")

# Split sentence by spaces
input_sentence = input_sentence.split()

number_of_letters = 0
number_of_words = 0
number_of_sentences = 0


# choose each word in the input senteces
for word in input_sentence:
    # calculate the count of words
    number_of_words += 1

    # calculate the count of letters
    filtered_word = re.sub("[^A-Za-z0-9]+", "", word)
    number_of_letters += len(filtered_word)

    # calculate the count of sentences
    sentence_delims = ["!", "?", "."]
    if any(delim in word for delim in sentence_delims):
        number_of_sentences += 1

# calculate the average
AVERAGE = 100 / number_of_words
# based of Coleman-Liau equation we have:
index = (
    (0.0588 * number_of_letters * AVERAGE)
    - (0.296 * number_of_sentences * AVERAGE)
    - 15.8
)

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {round(index)}")
