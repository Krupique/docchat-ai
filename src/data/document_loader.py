from langchain_community.document_loaders import PyPDFDirectoryLoader

# Function to read pdf files
def read_pdf(directory_path):

    # Accessing the directory which contains the pdf file
    file_loader = PyPDFDirectoryLoader(directory_path)

    # Reading the document
    documents = file_loader.load()

    return documents