import pandas as pd

data = pd.read_csv("dati/spotify_songs.csv")
print("full tracks count: ", len(data))


# atrodam visus unique tracks

unique_data = data["track_id"].nunique()
print("unique tracks: ", unique_data)


# šeit mēs atrodam tracks kuriem ir vairāk par vienu žanru

genre_nr = data.groupby("track_id")["playlist_genre"].nunique()
more_than_one_genre = genre_nr[genre_nr > 1]
print("tracks with more than one genre: ", len(more_than_one_genre))


# Izslēdzam dziesmas ar vairākiem žanriem, lai katrai dziesmai būtu viena mērķa vērtība.

data_first = len(data)
data = data[~data["track_id"].isin(more_than_one_genre.index)]
print("Rows removed due to conflicting genres: ", data_first - len(data))


# Katru dziesmu atstājam vienreiz, lai tā nevarētu būt gan treniņa, gan testa datos.

data_first = len(data)
data = data.drop_duplicates(subset=["track_id"], keep="first")
print("Duplicate rows removed: ", data_first - len(data))
print("new data tracks: ", len(data))

data.to_csv("tirs.csv", index=False)