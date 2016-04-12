
# import packages
import graphlab as gl

########################################################################################################################


# load data
data = gl.SFrame.read_csv('data/nowplaying/nowplaying_subset.csv', delimiter=',', verbose=False)


########################################################################################################################


# print source stats
print(data.groupby('source', {'freq': gl.aggregate.COUNT('source')}).sort('freq', False))

# print artist stats
print(data.groupby('artist', {'freq': gl.aggregate.COUNT('artist')}).sort('freq', False))

# print track stats
print(data.groupby('track', {'freq': gl.aggregate.COUNT('track')}).sort('freq', False))


########################################################################################################################
