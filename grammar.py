from random import choice
""" 
I was remembering grammer class and as i thought back then, 
why can't just match any 2 or 3 and have my peace.. Well this was why

This is just some basic grammar program
This is to just combine phrase or words to form a sentence
Sentence = sunj + verb + obj or adv or adj
"""

# a list of subjs, pronouns
subj  = ['I', "We", 'He', 'She', 'It', 'They', 'You']

# list of verbs
aux_verbs = ['am', 'are', 'was', 'were', 'is']
action_verbs = ['sitting', 'standing', 'sleeping', 'jumping', 'coding', 
'laughing', 'jogging', 'crying', 'eating', 'rolling', 
 'driving', 'dancing', 'writing', 'reading', 'cooking']
past_action_verbs = ['sat', 'stood', 'slept', 'jumped', 'coded', 'laughed', 
'jogged', 'cried', 'ate', 'rolled', 'drove', 'wrote', 'read', 'cooked']

# list of objs
objs = ['down', 'tall', 'early', 'up and down', 'in python', 'loudly', 
'across the park', 'alone in the dark', 'tuna and bread', 'on the ground', 'a bus',
 'azonto', 'a poem', 'Modern X86 Assembly Language Programming: 32-bit, 64-bit, SSE, and AVX by Daniel Kasswurm']

sentence1  = choice(subj) + " " + choice(past_action_verbs)
print(sentence1)

sentence2  = choice(subj) + " " + choice(aux_verbs) + " " + choice(action_verbs)
print(sentence2)

sentence3  = choice(subj) + " " + choice(aux_verbs) + " " + choice(action_verbs) + " " + choice(objs)
print(sentence3)

sentence4  = choice(subj) + " " + choice(past_action_verbs) + " " + choice(objs)
print(sentence4)