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

```python
from nltk.corpus import stopwords
sw = stopwords.words("english")
```
`sw` is the list of stopwords in English language.

`Stemming` to consolidate vocabulary. Not all words are unique. For example: response, responsivity, respond all `stem` from single word `respon`. So this helps reduce total number of words in vocab.


```python
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("responsiveness")
### Output is: 'respon'
```

## Tf-Idf Representation
Tf: Term Frequency. It is similar to Bag of Words.

Idf: Inverse Document Frequency. Weighting by how often word occur in a corpus. Rare words are weighted higher as compared to commonly occurring words.
