import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords',quiet=True)
nltk.download('wordnet',quiet=True)
nltk.download('omw-1.4',quiet=True)
def clean_text(text):
    text=text.lower()
    text=text.translate(str.maketrans('','',string.punctuation))
    words=text.split()
    stop_words=set(stopwords.words("english"))
    filtered_words=[word for word in words if word not in stop_words]
    lemmatizer=WordNetLemmatizer()
    lemmatized=[lemmatizer.lemmatize(word) for word in filtered_words]
    return lemmatized
 
