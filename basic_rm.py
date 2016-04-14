
# import packages
import argparse
import graphlab as gl

########################################################################################################################

# load data
data = gl.SFrame.read_csv('data/nowplaying_subset.csv', delimiter=',', verbose=False)

########################################################################################################################


def item_sim():

    # create item similarity recommender
    rm = gl.item_similarity_recommender.create(data)

    # make recommendations
    recs = rm.recommend()

    # save recommendations to file
    recs.save('recs/basic_rm/item_sim_recs.csv', format='csv')

    # get similar items
    sim_items = rm.get_similar_items()

    # save similar items to file
    sim_items.save('recs/basic_rm/item_sim_sim_items.csv', format='csv')


########################################################################################################################


def rank_fact():

    # create ranking factorization recommender
    rm = gl.ranking_factorization_recommender.create(data)

    # make recommendations
    recs = rm.recommend()

    # save recommendations to file
    recs.save('recs/basic_rm/rank_fact_recs.csv', format='csv')

    # get similar items
    sim_items = rm.get_similar_items()

    # save similar items to file
    sim_items.save('recs/basic_rm/rank_fact_sim_items.csv', format='csv')


########################################################################################################################


def pop():

    # create popularity recommender
    rm = gl.popularity_recommender.create(data)

    # make recommendations
    recs = rm.recommend()

    # save recommendations to file
    recs.save('recs/basic_rm/pop_recs.csv', format='csv')

    # get similar items
    sim_items = rm.get_similar_items()

    # save similar items to file
    sim_items.save('recs/basic_rm/pop_sim_items.csv', format='csv')


########################################################################################################################


# main function
def main(basic_rm):

    # if basic recommender equals to 'item_sim'
    if basic_rm == 'item_sim':
        # run item sim function
        item_sim()
    # if basic recommender equals to 'rank_fact'
    elif basic_rm == 'rank_fact':
        # run rank function
        rank_fact()
    # if basic recommender equals to 'pop'
    elif basic_rm == 'pop':
        # run pop function
        pop()


########################################################################################################################


# runs main function
if __name__ == '__main__':

    # parse script argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-b_rm', '--basic_rm', type=str, dest='basic_rm', metavar='basic recommender name',
                        help='basic recommender name', required=True)
    args = parser.parse_args()

    # call main function with the script argument as parameter
    main(args.basic_rm)


########################################################################################################################
