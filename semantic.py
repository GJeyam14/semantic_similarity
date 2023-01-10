import spacy

nlp = spacy.load('en_core_web_md')

"""
Cat and Monkey have the highest similarity (0.59) likely due to both words being animals.
They are more likely to arise in similar contexts. 

Monkey and Banana have the second highest similarity (0.40).
This is likely due to the monkey's diet and these words being used frequently in that context.

Cat and Banana have the least similarity (0.22) of the possible pairs.
The small amount of similarity may be due to their use in some household contexts.
"""

word1 = nlp("love")
word2 = nlp("like")
word3 = nlp("hate")

print(f"{word1} <-> {word2}:\t{word1.similarity(word2)}")
print(f"{word1} <-> {word3}:\t{word1.similarity(word3)}")
print(f"{word2} <-> {word3}:\t{word2.similarity(word3)}")

"""
It may be expected that love and hate would have the least similarity, as they describe opposite emotions. 
However, love and hate return the highest similarity (0.571). 
This is likely due their use in situations of higher emotion. 
'Like' does not demonstrate a similar strength of opinion about something as love and hate.

Spacy seems to prioritise the use of words in similar circumstances 
over whether the words are synonyms or antonyms, in determining similarity. 

There is not a huge degree of difference in the similarity results. 
They are all used to describe an emotion or feeling and therefore used in similar contexts.  
Love and like (0.521) has a slightly higher similarity than like and hate (0.507).
This is likely due to like and love being used in generally positive contexts.
"""

"""
Example File with Small vs. Medium Language Model - Differences:

When utilising the the medium language model, there is a high degree of similarity between all of the complaints
and between all of the recipes. The similarity between the complaints and recipes is not as high.

When the the file is run with the small language model, the similarity for complaints, recipes and
recipes to complaints falls significantly. Therefore, it is apparent that the medium language model
is better at recognising more abstract similarities between short texts.

The small model does not have any word vectors loaded, and therefore similarity judgements are not as accurate
or useful. The small model can be improved by adding word vectors.
"""
