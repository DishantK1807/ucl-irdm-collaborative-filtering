# get vocabulary from the data. then concatenate all data as text for each track.
# finally, obtain the tf-idf of each track or document against the vocab..
# at the end we need to have a TxV matrix where T is the number of tracks and
# the V is the vocabulary size.


# import packages
import argparse
import graphlab as gl

########################################################################################################################


# loads data
def load_data():

    # load data
    print ("starting to load the data...")

    track_data = gl.SFrame.read_csv('data/musicbrainz/track_data.csv', delimiter=';', verbose=False)

    track_record_tags = gl.SFrame.read_csv('data/musicbrainz/track_record_tags.csv', delimiter=';', verbose=False)

    track_artist_tags = gl.SFrame.read_csv('data/musicbrainz/track_artist_tags.csv', delimiter=';', verbose=False)

    # return data
    print("data loaded...")

    return track_data, track_record_tags, track_artist_tags

if __name__ == '__main__':

    track_data, track_record_tags, track_artist_tags = load_data()

    print ("merging...")

    merged = track_data.join(track_record_tags, on='gid', how='left')

    print ("printing...")

    print(merged)


    # print ("starting to load the data...\n")
    #
    # df1 = pd.read_csv("data/musicbrainz/track_artist_tags.csv", sep=';')
    #
    # df2 = pd.read_csv("data/musicbrainz/track_data.csv", sep=';')
    #
    # print ("...loading complete, now merging \n")
    #
    # merged = df1.merge(df2, on="gid", how="outer").fillna("")
    #
    # print ("...merged \n")
    #
    # merged.to_csv("data/musicbrainz/merged.csv", index=False)
    #
    # print ("...exported to csv \n")


    # sed 's/[^a-zA-Z0-9,-]/ /g' pre/output.csv > pre/clean_output.csv
