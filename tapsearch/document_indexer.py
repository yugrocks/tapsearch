# this module contains the class that indexes and searches for documents
class Indexer:
    
    def __init__(self):
        self.index = dict() # index is a mapping from words to a list of paragraph ids
        self.paragraphs = list() # 'paragraphs' is a list form which paragraph can be retrieved instantly, given its index
    
    def index_doc(self, document):
        """
        Inputs:
            document: is a text  (string) that is to be indexed.
        Returns: None
        
        Each piece of text can have multiple paragraphs and those paragraphs delimited by double nextlines will be preceived
        as two different paragraphs(documents) as per the requirement.
        """
        documents = document.split("\r\n\r\n") # this function is very fast. Each paragraph becomes a document.
        for document in documents:
            if document.strip() != "":
                paragraph_id = len(self.paragraphs)
                self.paragraphs.append(document)
                words = document.strip().split() # split by spaces
                seen_words = set()
                for word in words:
                    # check if word exists in the index
                    if not (word.lower() in seen_words):
                        seen_words.add(word.lower())
                        if word.lower() in self.index:
                            self.index[word.lower()].append(paragraph_id)
                        else:
                            self.index[word.lower()] = [paragraph_id, ]
                print("indexed paragraph. Number of words: ",len(words))
    
    def clear_index(self):
        # clear the index and everything
        self.index = dict()
        self.paragraphs = list()
        print("The index has been cleared.")
        
    def search(self, word):
        word = word.lower()
        if word in self.index:
            results = [self.paragraphs[index] for index in self.index[word]]
            return True, results
        else:
            return False, "" # word not found in index





