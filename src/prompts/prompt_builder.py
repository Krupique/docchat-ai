# Defines the similarity search function
def similarity_search(index, query, k = 2):

    # Uses the 'similarity_search' method of the 'index' object to search for the 'k' results
    # most similar to the 'query'
    matching_results = index.similarity_search(query, k)

    # Returns the matching results of the similarity search
    return matching_results

# Defines the function to get the answer
def get_answer(index, chain, query):

    # Calls the 'similarity_search' function with the given 'query' and stores the result in 'doc_search'
    doc_search = similarity_search(index, query)

    # Uses the 'chain' object to execute the run function and process the 'query' and the documents found,
    # storing the answer in 'response'
    response = chain.invoke(input= {"input_documents": doc_search, "question": query})

    # Returns the answer obtained from the previous processing
    return response