import pandas as pd
import matplotlib.pyplot as plt

#Create a bar chart of Messi's goals per season

messi_stats = pd.read_csv('path\messi_stats.csv')


#seasons messi played in
messi_seasons = messi_stats['Season'].unique()


#Each row in Messi_stats represents a goal
messi_goals_per_season = []
for i in range (len(messi_seasons)):
    count = 0
    for j in range(len(messi_stats)):
        if messi_stats['Season'][j] == messi_seasons[i]:
            count += 1
    messi_goals_per_season.append(count)
    
#fix label
messi_seasons[7] = "11/12"
messi_seasons[8] = "12/13"


#Bar chart of Messi's goals per season
plt.bar(messi_seasons, messi_goals_per_season, color="blue")
plt.xlabel('Season')
plt.ylabel('Goals')
plt.xticks(rotation=30)
plt.title("Messi's Goals per Season")
plt.show()


#Create a bar chart of Ronaldo's goals per season

# Ronaldo's stats
ronaldo_stats = pd.read_csv('C:\\Users\\nyeko\\Downloads\\coding\\Data_Visualisation\\bar_graphs\\data\\ronaldo_stats.csv')

ronaldo_seasons = ronaldo_stats['Season'].unique()

ronaldo_goals_per_season = []

for i in range(len(ronaldo_seasons)):
    count = 0
    for j in range(len(ronaldo_stats)):
        if ronaldo_stats["Season"][j] == ronaldo_seasons[i]:
            count += 1
    ronaldo_goals_per_season.append(count)

#fix label
ronaldo_seasons[10] = "12/13"

plt.bar(ronaldo_seasons, ronaldo_goals_per_season, color="red")
plt.title("Ronaldo's goals per season")
plt.xticks(rotation=30)
plt.xlabel("Seasons")
plt.ylabel("Goals")
plt.show()


# Compare stats
plt.bar(ronaldo_seasons, ronaldo_goals_per_season, color="red")
plt.bar(messi_seasons, messi_goals_per_season, color="blue")
plt.title("Messi vs Ronaldo goals per season")
plt.legend(["Ronaldo", "Messi"])
plt.xticks(rotation=30)
plt.xlabel("Seasons")
plt.ylabel("Goals")
plt.show()
