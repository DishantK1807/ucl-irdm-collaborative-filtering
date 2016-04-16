# get vocabulary from the data. then concatenate all data as text for each track.
# finally, obtain the tf-idf of each track or document against the vocab..
# at the end we need to have a TxV matrix where T is the number of tracks and
# the V is the vocabulary size.

import pandas as pd
import numpy as np
from collections import defaultdict
from collections import Counter

import csv

np.set_printoptions(threshold=np.nan)


########################################################################################################################



if __name__ == '__main__':

    print ("starting to load the data...\n")

    df1 = pd.read_csv("data/musicbrainz/track_artist_tags.csv", sep=';')

    df2 = pd.read_csv("data/musicbrainz/track_data.csv", sep=';')

    print ("...loading complete, now writing to file \n")

    merged = df1.merge(df2, on="gid", how="outer").fillna("")

    print ("...merged \n")

    merged.to_csv("data/musicbrainz/merged.csv", index=False)

    print ("...exported to csv \n")




    #CLEAN
    # sed 's/[^a-zA-Z0-9,-]/ /g' pre/output.csv > pre/clean_output.csv
