from sklearn.metrics.pairwise import cosine_similarity

def recommended_shows(title, shows_df, tfidf_vect):

    '''
    Recommends the top 5 similar shows to provided show title.
            Arguments:
                    title (str): Show title extracted from JSON API request
                    shows_df (pandas.DataFrame): Dataframe of Netflix shows dataset
                    tfidf_vect (scipy.sparse.matrix): sklearn TF-IDF vectorizer sparse matrix
            Returns:
                    response (dict): Recommended shows and similarity confidence in JSON format
    '''

    try:

        title_iloc = shows_df.index[shows_df['title'] == title][0]

    except:
        
        return 'Movie/TV Show title not found. Please make sure it is one of the titles in this dataset: https://www.kaggle.com/shivamb/netflix-shows'

    show_cos_sim = cosine_similarity(tfidf_vect[title_iloc], tfidf_vect).flatten()

    sim_titles_vects = sorted(list(enumerate(show_cos_sim)), key=lambda x: x[1], reverse=True)[1:6]

    response = {'result': [{'title':shows_df.iloc[t_vect[0]][0], 'confidence': round(t_vect[1],1)} for t_vect in sim_titles_vects]}
    
    return response

# def recommended_shows(title):
    
#     #Get show index
#     title_iloc = netflix_titles_df.index[netflix_titles_df['title'] == title][0]
    
#     #Get cosine similarity
#     show_cos_sim = cosine_similarity(tfidf_vectorizer[title_iloc], tfidf_vectorizer).flatten()
    
#     #Get the top 5 most similar shows
#     sim_titles_vects = sorted(list(enumerate(show_cos_sim)), key=lambda x: x[1], reverse=True)[1:6]
    
#     #Return result
#     response = '\n'.join([f'{netflix_titles_df.iloc[t_vect[0]][0]} --> confidence: {round(t_vect[1],1)}' for t_vect in sim_titles_vects])
    
#     return response
# print(recommended_shows('The Matrix'))
