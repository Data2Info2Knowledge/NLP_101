import spacy
from tabulate import tabulate

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f"Similarity between '{word1}' and '{word2}' : \t\t{word1.similarity(word2) :.5f}")
print(f"Similarity between '{word3}' and '{word2}' : \t\t{word3.similarity(word2) :.5f}")
print(f"Similarity between '{word3}' and '{word1}' : \t\t{word3.similarity(word1) :.5f}")
print("—"*55)

tokens = nlp('cat apple monkey banana ')
tokn_list = [token.text for token in tokens]
similar = []
for token1 in tokens:
    thisrow = [token1.text]
    for token2 in tokens:
        thisrow.append(f"{token1.similarity(token2) :.5f}")
    similar.append(thisrow)
print(tabulate(similar, headers=tokn_list))
print("")

sentence_to_compare = "Why is my cat on the car"
print(sentence_to_compare)
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my cat in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
maxlength = max([len(sentence) for sentence in sentences])
print("—"*maxlength)
similar = []
for sentence in sentences:
    thisrow = [sentence]
    similarity = nlp(sentence).similarity(model_sentence)
    thisrow.append(similarity)
    similar.append(thisrow)

similar.sort(key=lambda x:x[1], reverse=True)
for line in similar:
    print(f"{line[0]: <{maxlength}}   \t {line[1] :.6f}")