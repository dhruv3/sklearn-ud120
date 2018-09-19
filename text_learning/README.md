# Lesson 11: Text Learning

## Bag of Words

Count the frequency of words in a sentence. Implement a dictionary with features as key and count their occurrences.

Properties of Bag of Word:
1. Word order does not matter.
2. Long phrases will result in different vectors. For eg if you enlongate a sentence by repeating it then the final 
vector generated will be different compared to initial one.
3. Complex phrases cannot be handled. Eg: "Chicago Bulls".

`Note: Not all words are equal. Some contain more info than others.`

Low info words are called `Stopwords`.

Code:
* Create a list of sentences you need to process.
* Perform `fit` operation. It just identifies what are total number of keys.
* Perform `transform`. It counts the occurrences for each identified key.

