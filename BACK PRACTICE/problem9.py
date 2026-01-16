import string

def word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    
    return freq

print(word_frequency("Hello world, hello chatGPT world!"))
