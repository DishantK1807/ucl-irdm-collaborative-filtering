
# import packages
import graphlab as gl

########################################################################################################################


# load data
data = gl.SFrame.read_csv('data/nowplaying/nowplaying_2016_04_06.csv', delimiter=',', verbose=False)


########################################################################################################################


# get total number of users
def users_total():

    # get total number of users
    users = data.__getitem__('user_id')
    users = users.unique()
    print 'Total number of users: {}'.format(len(users))


########################################################################################################################

# get total number of artists
def artists_total():

    artists = data.__getitem__('artist')
    artists = artists.unique()
    print 'Total number of artists: {}'.format(len(artists))


########################################################################################################################


# get total number of tracks
def tracks_total():

    tracks = data.__getitem__('track')
    tracks = tracks.unique()
    print 'Total number of tracks: {}'.format(len(tracks))


########################################################################################################################

def source_stats():

    print(data.groupby('source', {'freq': gl.aggregate.COUNT('source')}).sort('freq', False))


########################################################################################################################


def artist_stats():

    print(data.groupby('artist', {'freq': gl.aggregate.COUNT('artist')}).sort('freq', False))


########################################################################################################################


def track_stats():

    print(data.groupby('track', {'freq': gl.aggregate.COUNT('track')}).sort('freq', False))


########################################################################################################################


def artist_track_stats():

    print(data.groupby('artist',
                       {'track': gl.aggregate.SELECT_ONE('track')},
                       {'artist freq': gl.aggregate.COUNT('artist')},
                       {'track freq': gl.aggregate.COUNT('track')}
                       ).sort('artist freq', False))


########################################################################################################################


# main function
def main():

    # get total number of tweets
    print 'Total number of tweets: {}'.format(len(data.__getitem__('timestamp')))
    # get total number of users
    # users_total()
    # get total number of artists
    # artists_total()
    # get total number of tracks
    tracks_total()

    # get source stats
    # source_stats()
    # get artist stats
    # artist_stats()
    # get track stats
    # track_stats()
    # get artist track stats
    # artist_track_stats()

########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
