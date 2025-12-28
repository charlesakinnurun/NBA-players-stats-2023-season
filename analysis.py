# %% [markdown]
# Data Analysis

# %% [markdown]
# import the necessary libraries

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# Load the cleaned dataset

# %%
df = pd.read_csv("nba_cleaned.csv")

# %% [markdown]
# Set the plot style

# %%
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10,6)

# %% [markdown]
# Question 1: Does player age correlate with performance

# %%
# Calculate correlation
corr_age_pts = df["age"].corr(df["points"])
corr_age_ast = df["age"].corr(df["ast"])
corr_age_reb = df["age"].corr(df["reb"])
print(f"Correlation between Age and Points: {corr_age_pts:.2f}")
print(f"Correlation between Age and Assists: {corr_age_ast:.2f}")
print(f"Correlation between Age and Rebounds: {corr_age_reb}")

# Plotting
# Create a scatter plot of Age vs Points
plt.figure(figsize=(10,6))
sns.regplot(x="age",y="points",data=df,scatter_kws={"alpha":0.5})
plt.title("Age vs Points Scored")
plt.xlabel("Age")
plt.ylabel("Points (PTS)")
plt.show()

# Create a box plot of Points by Age group
df["age_group"] = pd.cut(df["age"],bins=[18, 23, 27, 31, 35, 40],labels=['19-22', '23-26', '27-30', '31-34', '35+'])
plt.figure(figsize=(10,6))
sns.boxplot(x="age_group",y="points",data=df)
plt.title("Distribution of Points by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Points (PTS)")
plt.show()

# %% [markdown]
# Question 2: How do different player positions compare in terms of key statistics

# %%
# Group by Position and Calculate mean stats
pos_stats = df.groupby("position")[["points","ast","reb","blk","stl"]].mean().sort_values(by="points",ascending=False)
print("Average Stats by Position")
print(pos_stats.round(2))

# Plotting
# Create a grouped bar chart
pos_stats_melted = pos_stats.reset_index().melt("position",var_name="Statistic",value_name="Average Value")
plt.figure(figsize=(10,6))
sns.barplot(x="position",y="Average Value",hue="Statistic",data=pos_stats_melted)
plt.title("Average Key Statistics by Player Position")
plt.xlabel("Position")
plt.ylabel("Average Value")
plt.legend(title="Statistic")
plt.show()

# %% [markdown]
# Question 3: Which teams have most successful win/loss records, and how does this relate to their players average stats

# %%
# Calculate win percentage per team
team_success = df.groupby("team").agg(
    total_wins = ("won","sum"),
    total_loss = ("lost","sum"),
    avg_points = ("points","mean")
).reset_index()
team_success["win_percentage"] = team_success["total_wins"] / (team_success["total_wins"] + team_success["total_loss"])
print("Team Win Percentage and Average Player Points")
print(team_success[["team","win_percentage","avg_points"]].sort_values(by="win_percentage",ascending=False).round(2))

# Plotting
# Create a scatter plot of Win Percentage vs Average Points
plt.figure(figsize=(10,6))
sns.scatterplot(x="avg_points",y="win_percentage",data=team_success,hue="team",s=100)
plt.title("Team Win Percentage vs Average Player Points")
plt.xlabel("Average Player Points (PTS)")
plt.ylabel("Win Percentage")
plt.show()

# %% [markdown]
# Question 4: Are there notable difference in performace between players with high vs low minutes played

# %%
# Categorize players based on minutes played
median_min = df["minutes"].median()
df['minutes_category'] = df['minutes'].apply(lambda x: 'High Minutes' if x > median_min else 'Low Minutes')
print(f"Median minutes played used for categorization: {median_min:.2f}")
print(f"Average Points for each Minutes Category")
print(df.groupby("minutes_category")["points"].mean().round(2))

# Plotting 
# Create a box plot for Points (PTS) by Minute Category
plt.figure(figsize=(8,6))
sns.boxplot(x="minutes_category",y="points",data=df)
plt.title("Points (PTS) Distribution by Minutes Played Category")
plt.xlabel("Minutes Category")
plt.ylabel("Points (PTS)")
plt.show()

# %% [markdown]
# Question 5: What is the relationship between shooting percentages and the number of shot attempted

# %%
# Create scatter for FG% vs FGA
plt.figure(figsize=(10,6))
sns.regplot(x="fga",y="fg%",data=df,scatter_kws={"alpha":0.5})
plt.title("Field Goal Attempts (FGA) vs Field Goal Percentage (FG%)")
plt.xlabel("Field Goal Attempts (FGA)")
plt.ylabel("Field Goal Percentage (FG%)")
plt.show()

# Create a scatter plot for 3P% vs 3PA
plt.figure(figsize=(10,6))
sns.regplot(x="3pa",y="3p%",data=df,scatter_kws={"alpha":0.5})
plt.title("3-Point Attempts (3PA) vs 3-Point Percentage (3P%)")
plt.xlabel("3-Point Attempts (3PA)")
plt.ylabel("3-Point Percentage (3P%)")
plt.show()


