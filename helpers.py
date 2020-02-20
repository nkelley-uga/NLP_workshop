def make_cloud(freq_dict):
    '''make a wordcloud from a word frequency dictionary'''
    
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    
    wordcloud = WordCloud()
    wordcloud.generate_from_frequencies(frequencies=freq_dict)

    plt.figure(figsize=(12, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    
    
def clean(text):
    '''given some text, clean it'''
    import string
    import re
    from nltk.corpus import stopwords
    from nltk import WordNetLemmatizer

    # remove stuff
    non_char = string.punctuation + string.digits + '\n' + '’' + '“' + '”'
    cleaner_text = re.sub('[%s]' % re.escape(non_char), ' ', text.lower())
    # import lemma
    lemma = WordNetLemmatizer()
    # combine lemma and stopword removal
    clean_text = ' '.join([lemma.lemmatize(i) for i in cleaner_text.split() 
                           if i not in stopwords.words('english')])
    
    return clean_text


def moving_avg(numlist, lag):
    '''moving average across list of numbers'''
    window = [] 
    moving_avg = []
    
    for idx, i in enumerate(numlist):
        window.append(i)
        if idx >= lag:
            del window[0]
        moving_avg.append(sum(window)/len(window))
        
    return moving_avg