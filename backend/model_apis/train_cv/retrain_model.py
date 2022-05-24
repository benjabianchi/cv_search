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


def remove_punc(string):
    punc = '''!()-[]{};:'"\, <>./?@$%^&*--\_~'''
    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")
    return string
## DESCARGAR EL STOPWORDS Y USARLO DIRECTAMETNE DESDE UN PICKLE NO DESDE LA LIBRERIA NLTK!!!!!
## ESTA FUNCION SE ENCARGA DE PREPROCESAR LOS CV EN FORMATO PDF
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
    error = ['\uf0b7','']
    for i in tokens_without_sw:
        if i not in error:
            full_tokens.append(i)
    return full_tokens

## ESTA FUNCION SE ENCARGA DE PREPROCESAR LOS CV EN FORMATO DOCX(WORD)
## FUNCION DEPRECATED
# def getText_docx(filename):
#     clean_text = []
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(unidecode.unidecode(para.text))
#     full_string = '\n'.join(fullText)
#     full_string = full_string.replace('\n'," ")
#     full_string = full_string.replace('\t'," ")
#     no_punct = ""
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     for char in full_string:
#        if char not in punctuations:
#            no_punct = no_punct + char
#     tokens = no_punct.split()
#     tokens_without_sw = [word.lower() for word in tokens if not word in stopwords.words("spanish")+stopwords.words("english")]
#     lemmatizer = WordNetLemmatizer()
#     for token in tokens_without_sw:
#         clean_text.append(lemmatizer.lemmatize(token))
#     return clean_text
## ESTA USA TIKA Y LEE TANTO DOC COMO DOCX
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


## ESTA FUNCION SE ENCARGA DE PREPROCESAR TANTO LOS CV EN PDF COMO LOS DE DOCS TODO JUNTO
def open_files(path):
    cvs_tokens = []
    formats_pdf = [".pdf"]
    formats_docx = [".docx",".doc"]
    files = glob.glob(path+"*.pdf")+glob.glob(path+"*.docx")+glob.glob(path+"*.doc")
    files_names = []
    for i in range(len(files)):
        print(files[i])
        files_names.append(files[i].split("/")[1])
    #print(files_names)
    #data = getText_docx(files[100])
    for i in tqdm(range(len(files_names))):
        if formats_pdf[0] in files_names[i]:
            cvs_tokens.append(getText_pdf(files[i]))
        elif formats_docx[0] in files_names[i]:
            cvs_tokens.append(getText_docx(files[i]))
    return cvs_tokens

##ESTA FUNCION SE ENCARGA DE ARMAR EL BOW(bag of words) CON EL CORPUS GENERAL DE LOS CV
def calculate_bow(tokens):
    corpus = []
    for sublist in tokens:
        for item in sublist:
            corpus.append(item)
    global vectorizer
    vectorizer = CountVectorizer()

    X = vectorizer.fit_transform(corpus)
    bag_of_words = []
    for i in tokens:
        bag_of_words.append(vectorizer.transform([" ".join(i)]).A[0])
    with open('model/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    bow_ind = []
    for i in range(len(bag_of_words)):
        bow_ind.append((i,bag_of_words[i]))
    with open('model/bow.pkl', 'wb') as f:
        pickle.dump(bow_ind,f)
    return bow_ind


##ESTA FUNCION SE ENCARGA DE CALCULAR LA SIMILARIDAD ENTRE CVS
def calculateSimilarity(cv,description):
    return 1 - spatial.distance.cosine(cv, description)

## Aca filtro los vectores de bow con los indeces que tiene la busqueda ejemplo : [1999, 2550, 4642, 6630, 8051]
def get_cv_ohe(data,indeces):
    ohe = []
    for i in range(len(data)):
        ohe.append(np.take(data[i], indeces))
    return ohe


def retrain(path="cvs_ejemplo/"):
    tokens = open_files(path)
    bag_of_words = calculate_bow(tokens)
    print("Re-entrenamiento Realizado")


##ESTA FUNCION SE ENCARGA DE BUSCAR LOS CVS MAS SIMILARES , RECIBE COMO INPUT UNA DESCRIPCION(eg: "Python Java y Go") Y TOP_N(CUANTOS QUIERES RECIBIR DE LOS TOP N MEJORES CV CON MAYOR SIMILITUD A LO QUE BUSCAS,
## EL ULTIMO PARAMETRO ME PIDE SI QUERES HACER RETRAIN O NO
def model_prediction(description,top_n,train=None):
    if train == "retrain":
        retrain()

    with open('bow.pkl', 'rb') as f:
        bag_of_words = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    bag_of_words=[i[1] for i in bag_of_words]

    busqueda = vectorizer.transform([description])

    result = np.where(busqueda.A[0] >= 1)
    #Tomo los valores de esos indices con np.take
    busqueda = np.take(busqueda.A[0], result)
    X = get_cv_ohe(bag_of_words,result)
    bow_ind_1 = []
    ## Saco los que tienen un valor igual a cero dentro del vector
    for i in range(len(X)):
        if np.all(X[i][0]) == True:
            bow_ind_1.append((i,X[i][0]))
    ## Calcular similaridad
    cos_sim = []


    for i in range(len(bow_ind_1)):
        #print(bow_ind_1[i][1])
        #print(busqueda[0])
        cos_sim.append((round(calculateSimilarity(bow_ind_1[i][1],busqueda[0]),4),bow_ind_1[i][0]))
    #print(len(bag_of_words))
    cos_sim.sort(key=lambda x:x[0])
    cos_sim = cos_sim[:top_n]
    indeces_of_best_cv = [(x[1]) for x in cos_sim]
    files = glob.glob("cvs_ejemplo/"+"*.pdf")+glob.glob("cvs_ejemplo/"+"*.docx")+glob.glob("cvs_ejemplo/"+"*.doc")
    print(files)
    #print(files)
    files =[(files[i],i) for i in range(len(files))]
    #print(len(files))
    filter_cvs =list(filter(lambda x: x[1] in indeces_of_best_cv, files))
    filter_predictions =[(filter_cvs[i][0],cos_sim[i][0]) for i in range(len(cos_sim))]
    #filter_predictions = filter_predictions.sort(key=lambda x:x[1])
    return(sorted(filter_predictions, key = lambda x: x[1]))


#retrain("cvs_ejemplo/")
#predictions = model_prediction("Java y Oracle",7)
#predictions = model_prediction("Java y Python",5,"retrain")

#print(predictions)
