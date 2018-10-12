# SimilarWordFinder
A web application with Python backend which finds words similar to a given word, using pre-trained GloVe word embeddings.

Used pre-trained GloVe (Global Vectors for Word Representation) Word Embeddings to find out top 5 words similar/related to a given word (using similarity function). Optimized the search algorithm for similar words by vectorisation of similarity function (using NumPy) and binary search for word indices.

Created a frontend interface for the same with HTML, CSS and implemented its backend with Flask. It takes a word as input and returns top 5 words related to it.
