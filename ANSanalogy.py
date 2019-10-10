import numpy as np


print("Loading..........")
file = open("Glove/glove.6B.300d.txt")
file = file.readlines()

#to create word to vector dictionary
word2vector = dict()
for lines in file:
    line = lines.split()
    word = line[0]
    word_vector =line[1:]
    if word not in word2vector:
        word2vector[word]=np.asarray(word_vector, dtype='float32')

#function to compute cosine similarity
def cosine_similarity(u,v):
    #using cosine formule to calculate cosine of angle between two vectors
    similarity = (u@v)/(np.linalg.norm(u)*np.linalg.norm(v))
    #returning similarity
    return similarity

def check_analogy(e_a,e_b,e_c,word_choice):
    
    #u = word2vector[e_b.lower()]-word2vector[e_a.lower()]
    try:
        u = word2vector[e_b.lower()]-word2vector[e_a.lower()]
    except:
        return None,-1
    option = None
    max_sim = -100
    best_word = None
    
    for i in range(len(word_choice)):
        try:
            v=word2vector[word_choice[i].lower()]-word2vector[e_c.lower()]
            cosine_sim = cosine_similarity(u,v)
        except:
            print(word)
            #print('I dont wanna answer!!!Do whatever you want')
            return None,-1
        if cosine_sim > max_sim:
            max_sim = cosine_sim
            best_word = word_choice[i]
            option = chr(65+i)
    return best_word,option



