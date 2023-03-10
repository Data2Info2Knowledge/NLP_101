# Natural Language Processing (NLP) - Semantic Similarity with `spacy`

In this repository, I used the `spacy` library to perform some basic Natural Language Processing (NLP) on a variety of text samples.  

These practice tests are based on a task from a [HyperionDev](https://www.hyperiondev.com) coding bootcamp.

Unless specified otherwise, I used the medium-sized English language model.

## Similarity of individual words  
Initially, I used the `similarity` method on pairs of words taken from the triplet {'cat', 'monkey', 'banana'}.  

The main obervations made after running `semantic.py` are as follows:
* The similarity between 'cat' and 'monkey' is only slightly higher than that between 'banana' and 'monkey', at 0.395 vs. 0.374 - a surprising result, since *Cat* and *Monkey* can be thought of as sub-classes of the *Animal* class (and incidentally its *Mammal* sub-class), whereas the relationship between a banana and a monkey is of the type "food <--> consumer".  
* Similarly(!), one would have expected a much weaker association between 'banana' and 'cat'.

## Similarity between sentences
The program also compares short sentences to a given one, and displays each sentence with its similarity to the comparison 'benchmark.'  

In another program (not incuded here), starting from one list containing complaints submitted to a company and another list made up of recipes found online, I again used the `similarity` method, this time on longer, more complex sentences taken from each list, with the following results:
* Similarities among complaints ranged from 87.9% to 100.0%
* Similarities among recipes ranged from 87.6% to 100.0%
* Similarities between complaints and recipes ranged from 66.5% to 89.5%

## Medium- *vs.* small-sized language models
I then loaded the smaller model by using the statement `nlp = spacy.load('en_core_web_sm')` instead of `nlp = spacy.load('en_core_web_md')` and ran the same script, with the following results:
* Average similarity among complaints decreased from 95.7% to 70.6%
* Average similarity among recipes decreased from 94.4% to 76.0%
* Average similarity between complaints and recipes decreased from 79.3% to 47.5%

## Movie recommendation
In another application, `watch_next.py` finds the film, in a given dataset read in from `movies.txt`, that is most similar to a movie recently watched. This is done by sequentially calculating the similarity between the description of the given movie and the ones in the dataset.  
The user can opt to remove 'stop words' and punctuation from the film summaries.
