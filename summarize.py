import sys
import re

text  	  = sys.stdin.read()
sentences = re.split(r'\.', text)
wordsets  = []
for sentence in sentences:
    words = re.sub(r'\W+', ' ', sentence).strip().split()
    wordsets.append(set(words)) 

max_score = -1
max_index = -1
for i in range(len(wordsets)):
    current_score = 0
    for j in range(len(wordsets)):
        if i != j:
            current_score = current_score + len(wordsets[i] & wordsets[j])
    if current_score > max_score:
        max_score = current_score
        max_index = i

print sentences[max_index]
