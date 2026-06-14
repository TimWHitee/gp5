import pandas as pd

genre_names = ["Electronic", "Experimental", "Folk",
               "Hip-Hop", "Instrumental", "International", "Pop", "Rock"]

group_map = {
    "Electronic": "Electronic_Experimental",
    "Experimental": "Electronic_Experimental",
    "Instrumental": "Electronic_Experimental",
    "Pop": "Pop_Rock_HipHop",
    "Rock": "Pop_Rock_HipHop",
    "Hip-Hop": "Pop_Rock_HipHop",
    "Folk": "Folk_International",
    "International": "Folk_International",
}

group_names = sorted(set(group_map.values()))
genre_to_group_idx = {
    i: group_names.index(group_map[name])
    for i, name in enumerate(genre_names)
}


for name in ["train_meta.csv", "val_meta.csv"]:
    df = pd.read_csv(name)

    df["group"] = df["genre"].map(genre_to_group_idx)

    print(group_names)
    print(df.head())

    df.to_csv(f"{name}_grouped.csv", index=False)
