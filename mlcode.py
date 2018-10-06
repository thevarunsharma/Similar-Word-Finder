import numpy as np
from pickle import load

with open('words.dat', 'rb') as f:
    words = load(f)

vecs = np.load('vecs.npy')

def similarity(u, v):
    num = np.dot(u, v.T).reshape((u.shape[0], 1))
    den = (np.linalg.norm(u, axis=1)*np.linalg.norm(v, axis=1)).reshape((u.shape[0], 1))
    sim = num/den
    return sim.ravel()

def search(wrd, arr):       #binary search
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid]==wrd:
            return mid
        if arr[mid] < wrd:
            low = mid+1
        if arr[mid] > wrd:
            high = mid-1
    return -1

def find_similar(word, words=words, vecs=vecs):
    idx = search(word, words)
    if idx==-1:
        return "Word not in vocabulary!"
    vec1 = vecs[idx].reshape((1,50))
    sims = similarity(vecs, vec1)
    simidx = np.where(sims > 0.6)[0]
    simwords = []
    for i in simidx:
        if i!=idx:
            simwords.append((words[i], sims[i]))
    return simwords

def filter_results(simwords):
    if simwords=="Word not in vocabulary!" or len(simwords)==0:
        return simwords
    simwords = sorted(simwords, key = lambda x:x[1], reverse=True)
    return list(np.array(simwords)[:5,0])

def get_similar_words(word):    #wrapper function
    return filter_results(find_similar(word))
