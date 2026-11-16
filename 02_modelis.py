from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

data = pd.read_csv("tirs.csv")

# izevedojam mainigos un iedodam parametrus

X = data[["tempo", "loudness", "energy", "danceability", "speechiness"]]
y = data["playlist_genre"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# sagrupejam datus

most_popular_genre = y_train.value_counts().idxmax()
base_accuracy = (y_test == most_popular_genre).mean()

print("train count:", len(X_train))
print("Test count:", len(X_test), "\n")



print("Most popular genre in training set:", most_popular_genre)

# Izveidojam un trenējam modeli

model = DecisionTreeClassifier(max_depth=9, random_state=42)
model.fit(X_train, y_train)

# izveidojam prognozes un aprēķinam precizitāti

predictions = pd.Series(model.predict(X_test), index=X_test.index)
model_accuracy = model.score(X_test, y_test)

print("Baseline accuracy:", f"{base_accuracy:.2%}")
print("Model accuracy:", f"{model_accuracy:.2%}", "\n")

# analizējam modela svarus

importance = pd.Series(model.feature_importances_, index=X.columns)
print("most popular feature importance:")
for feature, value in importance.nlargest(2).items():
    print(" ", feature, f"{value:.2%}")

print("\n")

# Uz ka modleis pirmo reizi kļūdas

mistakes = predictions[predictions != y_test]
if not mistakes.empty:
    track_index = mistakes.index[0]
    track = data.loc[track_index]
    print("mistake:", track["track_artist"], "—", track["track_name"])
    print("Playlist genre:", track["playlist_genre"], "| Predicted:", mistakes.loc[track_index])