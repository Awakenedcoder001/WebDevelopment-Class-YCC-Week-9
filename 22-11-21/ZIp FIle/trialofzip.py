from zipfile import *
def zipping():
    documents=ZipFile('Documents.zip', 'w',ZIP_DEFLATED)
    documents.write('writting.txt')
    documents.write('writting1.txt')

if __name__ == '__main__':
    zipping()
