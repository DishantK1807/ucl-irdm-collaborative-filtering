
# import packages
import graphlab as gl

########################################################################################################################


# loads data
def load_data():

    # load data
    data = gl.SFrame.read_csv('../data/nowplaying_subset.csv', delimiter=',', verbose=False)

    # return data
    return data


########################################################################################################################


# get total number of users
def users_total(data):

    # get total number of users
    users = data.__getitem__('user_id')
    users = users.unique()
    print 'Total number of users: {}'.format(len(users))


########################################################################################################################


# get total number of artists
def artists_total(data):

    artists = data.__getitem__('artist')
    artists = artists.unique()
    print 'Total number of artists: {}'.format(len(artists))


########################################################################################################################


# get total number of tracks
def tracks_total(data):

    tracks = data.__getitem__('track')
    tracks = tracks.unique()
    print 'Total number of tracks: {}'.format(len(tracks))


########################################################################################################################


# gets filtered users
def filtered_users():

    # get filtered users
    user_id_item_id = gl.SFrame.read_csv('output/user_id_item_id_2016_04_06.csv', delimiter=',', verbose=False)
    user_count_3 = gl.SArray('output/user_count_3_2016_04_06.csv')

    sample_count_3 = user_id_item_id.filter_by(user_count_3, 'user_id').sort('user_id', ascending=False)
    sample_count_3.save('output/sample_count_3_2016_04_06.csv')


########################################################################################################################


# gets user stats
def user_stats(data):

    # get user stats
    users = (data.groupby('user_id', {'count': gl.aggregate.COUNT('user_id')}).sort('count', ascending=False))
    users.save('output/user_count_2016_04_06.csv')


########################################################################################################################


# gets source stats
def source_stats(data):

    # get source stats
    source = (data.groupby('source', {'count': gl.aggregate.COUNT('source')}).sort('count', ascending=False))
    source.save('output/source_2016_04_06.txt')


########################################################################################################################


# gets artist stats
def artist_stats(data):

    # get artist stats
    artist = (data.groupby('artist', {'count': gl.aggregate.COUNT('artist')}).sort('count', ascending=False))
    artist.save('output/artist_2016_04_06.txt')


########################################################################################################################


# gets track stats
def track_stats(data):

    # get track stats
    track = (data.groupby('track', {'count': gl.aggregate.COUNT('track')}).sort('count', ascending=False))
    track.save('output/track_2016_04_06.txt')


########################################################################################################################


# gets artist track stats
def artist_track_stats(data):

    # get artist track stats
    artist_track = (data.groupby('artist',
                       {'track': gl.aggregate.SELECT_ONE('track')},
                       {'artist count': gl.aggregate.COUNT('artist')},
                       {'track count': gl.aggregate.COUNT('track')}
                       ).sort('artist count', ascending=False))
    artist_track.save('output/artist_track_2016_06_04.txt')


########################################################################################################################


# main function
def main():

    # load data
    data = load_data()

    # get total number of tweets
    # print 'Total number of tweets: {}'.format(len(data.__getitem__('timestamp')))
    # get total number of users
    # users_total(data)
    # get total number of artists
    # artists_total(data)
    # get total number of tracks
    # tracks_total(data)

    # get user_stats()
    user_stats(data)
    # get source stats
    # source_stats(data)
    # get artist stats
    # artist_stats(data)
    # get track stats
    # track_stats(data)
    # get artist track stats
    # artist_track_stats(data)


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
