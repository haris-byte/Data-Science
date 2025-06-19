import numpy as hn
import pandas as hp
import matplotlib.pyplot as hmat
import seaborn as hc

#  PROJECT : GAME RATING ANALYSIS
data = {
    "Game": ["Genshin", "Homkai", "Wuthering Waves", "PUBG", "COD", "Apex"],
    "Genre":["RPG","RPG","RPG","Battle Royale","FPS","FPS"],
    "Rating":[9.1,8.7,None,7.8, 8.2,7.9],
    "Downloads":[7000000,5000000,2000000,None,6000000,4000000],
    "In-App Purchases":["Yes","Yes","Yes","No","Yes","No"]
}
Game_DF = hp.DataFrame(data)
print(f"\nOriginal Data{Game_DF}\n")

# ✅ 1. Clean the Data 

null = Game_DF.isnull().sum()
for col in Game_DF.columns:
    if Game_DF[col].isnull().sum() > 0:
        if Game_DF[col].dtype in ["int64","float64"]:
            Game_DF[col]=Game_DF[col].fillna(Game_DF[col].mean())
        else:
            Game_DF[col] = Game_DF[col].fillna("Unknown")

Game_DF.replace("RPG","Adventure",inplace=True)

Game_DF["Game"] = Game_DF["Game"].dropna()

# ✅ 2. Add Calculated Columns

Game_DF["Popularity"] = hn.where(Game_DF["Downloads"]>=5000000, "High","Low")

Game_DF["Revenue"] = Game_DF["In-App Purchases"].apply(lambda x: "Monitized" if x =="Yes" else "Free"  )

# ✅ 3. Visualizations
hmat.figure(figsize=(12,7)) 

hmat.subplot(2, 2, 1)
hc.barplot(data=Game_DF, x=Game_DF["Game"],y=Game_DF["Rating"],hue="Rating")
hmat.title("Game VS Rating")
hmat.xlabel("Games")
hmat.ylabel("Ratings")

hmat.subplot(2, 2, 2)
hc.scatterplot(data=Game_DF,x=Game_DF["Downloads"],y=Game_DF["Rating"],hue="Downloads")
hmat.title("Downloads VS Rating")
hmat.xlabel("Downloads")
hmat.ylabel("Ratings")

hmat.subplot(2,2,3)
hc.countplot(data=Game_DF,x=Game_DF["Genre"],color="Green")
hmat.title("Counts of Genre")
hmat.xlabel("Genre")

hmat.subplot(2,2,4)
hc.heatmap(Game_DF.corr(numeric_only=True))


hmat.show()

print(f"\n    --Modified Data--{Game_DF.to_string()}\n")
print("\n     --Report--    \n")
print(Game_DF.describe())
print(Game_DF.corr(numeric_only=True))
print(Game_DF.head())
print(
    "\n      --Conclusion--\n" \
    "Genshin is top Rated And Highly Download\n " \
    "Wuthering Waves has Missing Value \n" \
    "RPG games Dominate The Market As They Are Besto\n" \
    "In-App Purchases games tend to have Higher Rating"
)