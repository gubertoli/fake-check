from nltk import download as nltk_download
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import unidecode
import re
from pickle import load

nltk_download("stopwords", quiet=True)
nltk_download("rslp", quiet=True)

stop_words = stopwords.words("portuguese")
stemmer = RSLPStemmer()

tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
min_length = 3

def valid(word):
    return len(word) >= min_length and re.match(r"^[a-z]*$", word) and word not in stop_words and word not in string.punctuation

def clean(text):
    #text = re.sub(r"#", "", text) # Remover #
    text = unidecode.unidecode(text)
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)
    
    words = tokenizer.tokenize(text)
 
    return " ".join([word for word in words if valid(word)])

def main():
    text = """Kátia Abreu diz que vai colocar sua expulsão em uma moldura, mas não para de reclamar.	

A senadora Kátia Abreu (sem partido-TO) disse que sua expulsão do PMDB foi resultado de uma ação da cúpula atual da legenda que, segundo ela, é oportunista.

“Amanhã eu vou botar numa moldura dourada a minha expulsão, porque das mãos de onde veio, é um atestado de boa conduta para o meu currículo. Essas pessoas que me expulsaram não servem ao país. Eles se servem do país em seus benefícios próprios”, disse Kátia Abreu.

Ué, mas se a expulsão é algo tão bom para seu currículo, por que tanta choradeira, Kátia?

Sabemos o motivo. Provavelmente Kátia não tem valor para o PT, partido que já deveria tê-la absorvido. Ao que parece o PT gostava de Kátia somente se ela ficasse entrincheirada dentro do PMDB.

Ou seja, isso é se rebaixar demais. Resta a Kátia ficar chorando as pitangas por todos os cantos.

Em tempo: até o momento o PT não cadastrou Kátia Abreu em suas fileiras. Que situação patética para a ex-ministra da Agricultura de Dilma."""

    text_clean = clean(text)
    text_stemmed = " ".join([ stemmer.stem(word) for word in text_clean.split(" ") ])
    
    tfidf = load(open('tfidf.pkl', 'rb')) # load trained TfidfVectorizer
    clf = load(open('clf.pkl', 'rb')) # load trained model
    
    X = tfidf.transform([text_stemmed])
    inference = clf.predict_proba(X.toarray())
    print(inference)


if __name__ == "__main__":
    main()
    