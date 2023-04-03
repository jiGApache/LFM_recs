import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def group_input(artist_names):
    group_name = input("Введите название группы(q - для выхода): ")
    
    if group_name == 'q': exit()

    while group_name not in artist_names:
        print("Нет такой группы")
        group_name = input("Повторите ввод (q - для выхода): ")
        if group_name == 'q': exit()

    return group_name


if __name__ == "__main__":
    # Reading data
    scrobbles = pd.read_csv('Data/lastfm_user_scrobbles.csv')
    artists = pd.read_csv('Data/lastfm_artist_list.csv', index_col=0)
    artist_names = artists['artist_name'].to_list()

    # Convert the dataset into a user-item matrix
    user_item_matrix = scrobbles.pivot_table(index='user_id', columns='artist_id', values='scrobbles', fill_value=0)

    # Calculate the pairwise cosine similarity between the columns
    item_similarity_matrix = cosine_similarity(user_item_matrix.T)
    item_similarity_matrix = pd.DataFrame(item_similarity_matrix, index=artist_names, columns=artist_names)

    group_name = group_input(artist_names)
    while True:
        similarities = list(enumerate(item_similarity_matrix[group_name]))
        similarities = list(filter(lambda x: x[1] > 0.8, similarities))
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

        if len(similarities) == 1: 
            print('Ничего не найдено')
        else:
            print('Возможные результаты:')
            for similarity in similarities: 
                if item_similarity_matrix.columns[similarity[0]] != group_name:
                    print(f'- {item_similarity_matrix.columns[similarity[0]]} | ({similarity[1]})')

        group_name = group_input(artist_names)


