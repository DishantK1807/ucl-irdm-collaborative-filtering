
# import packages
import graphlab as gl

########################################################################################################################


# loads data
def load_data():

    # load data
    data = gl.SFrame.read_csv('analysis/santi_count.csv', delimiter=',', verbose=False)

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
    user_id_item_id = gl.SFrame.read_csv('analysis/user_id_item_id_2016_04_06.csv', delimiter=',', verbose=False)
    user_count_3 = gl.SArray('analysis/user_count_3_2016_04_06.csv')

    sample_count_3 = user_id_item_id.filter_by(user_count_3, 'user_id').sort('user_id', ascending=False)
    sample_count_3.save('analysis/sample_count_3_2016_04_06.csv')


########################################################################################################################


# gets user stats
def user_stats(data):

    # get user stats
    # users = (data.groupby('user_id', {'count': gl.aggregate.COUNT('user_id')}).sort('count', ascending=False))
    # users.save('analysis/santi_count.csv')

    '''
    mean_std = (data.groupby("user_id",
                             {'argmax': gl.aggregate.ARGMAX('count', 'count')},
                             {'argmin': gl.aggregate.ARGMIN('count', 'count')},
                             {'mean': gl.aggregate.MEAN('count')},
                             {'std': gl.aggregate.STD('count')}))
    mean_std.save('analysis/santi_argmax_argmin_mean_std.csv')
    '''

    count = data.select_columns('count')
    mean = count.

########################################################################################################################

# gets source stats
def source_stats(data):

    # get source stats
    source = (data.groupby('source', {'count': gl.aggregate.COUNT('source')}).sort('count', ascending=False))
    source.save('analysis/source_2016_04_06.txt')


########################################################################################################################


# gets artist stats
def artist_stats(data):

    # get artist stats
    artist = (data.groupby('artist', {'count': gl.aggregate.COUNT('artist')}).sort('count', ascending=False))
    artist.save('analysis/artist_2016_04_06.txt')


########################################################################################################################


# gets track stats
def track_stats(data):

    # get track stats
    track = (data.groupby('track', {'count': gl.aggregate.COUNT('track')}).sort('count', ascending=False))
    track.save('analysis/track_2016_04_06.txt')


########################################################################################################################


# gets artist track stats
def artist_track_stats(data):

    # get artist track stats
    artist_track = (data.groupby('artist',
                       {'track': gl.aggregate.SELECT_ONE('track')},
                       {'artist count': gl.aggregate.COUNT('artist')},
                       {'track count': gl.aggregate.COUNT('track')}
                       ).sort('artist count', ascending=False))
    artist_track.save('analysis/artist_track_2016_06_04.txt')


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
