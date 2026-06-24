import nltk

# nltk.download('all') 

import nltk
import re
import string
from nltk.stem import WordNetLemmatizer
 
# nltk.download('wordnet')
# nltk.download('omw-1.4') 


with open('final.txt','r',encoding='utf8') as f:
    text_data=f.read().lower()
    words=re.findall(r'\w+',text_data)

vocad_words=set(words)

def count_frequency(words):
    words_count={}
    for word in words:
        words_count[word]=words_count.get(word,0)+1 
    return words_count 
word_count=count_frequency(words)

def calculate_prob(word_count):
    total_words=sum(word_count.values())
    return {word:count/total_words for word,count in word_count.items() }

probabilities=calculate_prob(word_count)

lemmatizer=WordNetLemmatizer()

def lemmatizer_words(word):
    return lemmatizer.lemmatize(word)

def delete_letter(word):
    return [word[:i]+word[i+1:] for i in range(len(word))]

def swap_letters(word):
    return [word[:i]+word[i+1]+word[i]+word[i+2:] for i in range(len(word)-1)]

def replace_letter(word):
    letters=string.ascii_lowercase
    return [word[:i]+l+word[i+1:] for i in range(len(word)) for l in letters]

def insert_letter(word):
    letters = string.ascii_lowercase
    return [word[:i] + l + word[i:] for i in range(len(word)+1) for l in letters] 

def genrate_candiates(word):
    candidates=set()
    candidates.update(delete_letter(word))
    candidates.update(swap_letters(word))
    candidates.update(replace_letter(word))
    candidates.update(insert_letter(word))

    return candidates

def candidate_l2(word):
    level1=genrate_candiates(word)
    level2=set()
    for w in level1:
        level2.update(genrate_candiates(w))

    return level2 

def get_best_correction(word, probs, vocab, max_suggestions=3):
    candidates = (
        [word] if word in vocab else list(candidate_l2(word).intersection(vocab)) or 
        list(candidate_l2(word).intersection(vocab))

    )
    return sorted([(w, probs.get(w, 0)) for w in candidates],key=lambda x:x[1],reverse=True)[:max_suggestions]


user_input=input('\n Enter a word for autocorrections:')

suggestions=get_best_correction(user_input,probabilities,vocad_words,max_suggestions=3)

print('\n suggestions')
for s in suggestions:
    print(suggestions[0])



    
