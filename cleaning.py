# %% [markdown]
# Data Preprocessing

# %% [markdown]
# Import the neccessary libraries

# %%
import pandas as pd

# %% [markdown]
# Load the dataset

# %%
df = pd.read_csv("nba.csv")

# %% [markdown]
# Data Inspection

# %%
print(df.head().to_string())
print(df.info())

# %% [markdown]
# Check for missing values

# %%
df_missing = df.isnull().sum()
print(df_missing)

# %% [markdown]
# Drop any rows with any missing values

# %%
df = df.dropna()

# %% [markdown]
# Rename the column for Clarity and Consistency

# %%
df.rename(columns={
    "PName":"player",
    "POS":"position",
    "Team":"team",
    "Age":"age",
    "GP":"gp",
    "W":"won",
    "L":"lost",
    "Min":"minutes",
    "PTS":"points",
    "FGM":"fgm",
    "FGA":"fga",
    "FG%":"fg%",
    "3PM":"3pm",
    "3PA":"3pa",
    "3P%":"3p%",
    "FTM":"ftm",
    "FTA":"fta",
    "FT%":"ft%",
    "OREB":"oreb",
    "DREB":"dreb",
    "REB":"reb",
    "AST":"ast",
    "TOV":"tov",
    "STL":"stl",
    "BLK":"blk",
    "PF":"pf",
    "FP":"fp",
    "DD2":"dd2",
    "TD3":"td3",
    "+/-":"+/-"
},inplace=True)

# %% [markdown]
# Preview the data

# %%
print(df.head().to_string())
print(df.info())

# %% [markdown]
# Save the cleaned data

# %%
df.to_csv("nba_cleaned.csv",index=False)
print("Saved Successfully")


