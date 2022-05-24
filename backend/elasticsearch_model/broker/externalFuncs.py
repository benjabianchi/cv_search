from nltk.corpus import stopwords
from scipy import spatial
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tika import parser
import unidecode
from tqdm import tqdm
import glob
import docx
import json
import pickle
import nltk
import os
import pandas as pd

def remove_punc(string):
    punc = '''!()-[]{};:'"\, <>./?@$%^&*--\_~'''
    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")
    return string


def getText_pdf(cv):
    nltk.download('wordnet')
    nltk.download('stopwords')
    clean_text = []
    parsed_pdf = parser.from_file(cv)
    data = parsed_pdf['content']
    data_split = data.split()
    lis = [remove_punc(i) for i in data_split]
    tokens_without_sw = [word.lower() for word in lis if not word in stopwords.words("spanish")+stopwords.words("english")]
    lemmatizer = WordNetLemmatizer()
    for token in tokens_without_sw:
        clean_text.append(lemmatizer.lemmatize(token))
    full_tokens = []
    error = ['\uf0b7','','\uf07d']
    for i in tokens_without_sw:
        if i not in error:
            full_tokens.append(i)
    return full_tokens

def getText_docx(cv):
    nltk.download('wordnet')
    nltk.download('stopwords')
    clean_text = []
    parsed_pdf = parser.from_file(cv)
    data = parsed_pdf['content']
    data_split = data.split()
    lis = [remove_punc(i) for i in data_split]
    tokens_without_sw = [word.lower() for word in lis if not word in stopwords.words("spanish")+stopwords.words("english")]
    lemmatizer = WordNetLemmatizer()
    for token in tokens_without_sw:
        clean_text.append(lemmatizer.lemmatize(token))
    full_tokens = []
    error = ['\uf0b7','']
    for i in tokens_without_sw:
        if i not in error:
            full_tokens.append(i)
    return full_tokens




'''
    For the given path, get the List of all files in the directory tree
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles
def main():

    dirName = 'C:\\Users\\Benjamin\\Desktop\\elasticsearch_cv\\cvs_ejemplo';

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)

    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]


    # Print the files
    for elem in listOfFiles:
        print(elem)

    return listOfFiles


def get_extension(list_files):
    extensions = []
    for i in range(list_files):
        file_extension = pathlib.Path(list_files[i]).suffix
        extension.append(file_extension)
    return extensions


def open_files(path):
    cvs_tokens = []
    formats_pdf = [".pdf"]
    formats_docx = [".docx",".doc"]
    ## QUITAR GLOB Y USAR DIRECTAMENTE LA FUNCION CREADA PARA TOMAR TODOS LOS FOLDERS Y SUBFOLDERS
    files = glob.glob(path+"*.pdf")+glob.glob(path+"*.docx")+glob.glob(path+"*.doc")
    files_names = []
    for i in range(len(files)):
        print(files[i])
        files_names.append(os.path.split(files[i])[1])
    #print(files_names)
    #data = getText_docx(files[100])
    for i in tqdm(range(len(files_names))):
        if formats_pdf[0] in files_names[i]:
            cvs_tokens.append(getText_pdf(files[i]))
        elif formats_docx[0] in files_names[i]:
            cvs_tokens.append(getText_docx(files[i]))
    return cvs_tokens

def get_local(files):
    local = []
    for i in range(len(files)):

        path_split = files[i].split("\\")[0].split("/")
        if len(path_split)>1:
            local.append(path_split[1])
        else:
            local.append("Desconocido")
    return local


def create_csv(path):
    words = open_files(path)
    files = glob.glob("cvs_ejemplo/"+"*.pdf")+glob.glob("cvs_ejemplo/"+"*.docx")+glob.glob("cvs_ejemplo/"+"*.doc")
    print(len(words))
    print(len(files))

    d = {"path":files,"words":[" ".join(w) for w in words]}
    df = pd.DataFrame(d)
    df.to_csv("csv/CVs.csv",index=False)
