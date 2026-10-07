import pandas as pd

from graph import histogram

workbook = pd.read_excel(
    "Music.xlsx",
    sheet_name=None
)

data = pd.concat(workbook.values(), ignore_index=True)

data.columns = data.columns.str.strip()

keep = [
        column for column in [
            "Album",
            "Artist",
            "Release Year",
            "Listen date",
            "Rating",
            "Thoughts"
        ]
        if column in data.columns
    ]

data = data[keep]

data["Rating"] = (
        data["Rating"]
        .astype(str)
        .str.replace("/10", "", regex=False)
        .str.strip()
    )

data["Rating"] = pd.to_numeric(data["Rating"], errors="coerce")

data = data.dropna(subset=["Rating"])


print(f"\nAlbums Rated: {len(data)}")
print(f"Average Rating: {data['Rating'].mean():.2f}")
print(f"Median Rating: {data['Rating'].median()}")
print(f"Most Common Rating: {data['Rating'].mode()[0]}")

histogram(data)
