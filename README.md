
## Collaborative filtering project using Deep Learning

Coursework project developed as part of the [COMPGI15 - Information Retrieval and Data Mining](http://www.cs.ucl.ac.uk/teaching_learning/syllabus/mscml/gi15_information_retrieval_data_mining/) module at University College London

#### Group Members - MSc. Web Science and Big Data Analytics

* [Santiago Gonzalez](https://github.com/santteegt)
* [Archie Norman](https://github.com/archienorman11)
* [Sergiu Tripon](https://github.com/SergiuTripon)

#### Dataset

#### System Requirements

#### Installation

Fork this repository and then clone it by running the following command and entering your GitHub username and password:

```bash
git clone https://github.com/YOUR-USERNAME/ucl-irdm-collaborative-filtering
```

##### Setting up GraphLab Create

GraphLab Create is a machine learning framework provided by Dato. In order to use GraphLab Create a license is required. Dato's Academic Programme offers a 1-year free license of GraphLab Create. In order to obtain a license, visit https://dato.com/download/academic.html and register using a @ucl.ac.uk or @cs.ucl.ac.uk account.

Once you have obtained a GraphLab Create license, forked and cloned the repo, follow the steps below to continue setting up GraphLab Create:

```bash
# navigate to ucl-irdm-collaborative-filtering folder
$ cd ucl-irdm-collaborative-filtering

# navigate to dato folder
$ cd dato

# create a new virtual environment with Python 2.7.x
$ virtualenv -p /usr/bin/python2.7 dato-env

# activate the virtual environment
$ source dato-env/bin/activate

# ensure pip is updated to the latest version
$ pip install --upgrade pip

# install your licensed copy of GraphLab Create
$ pip install --upgrade --no-cache-dir pip install --upgrade --no-cache-dir https://get.dato.com/GraphLab-Create/1.8.5/your registered email address here/your product key here/GraphLab-Create-License.tar.gz

# when finished, deactivate the virtual environment
$ deactivate

```

##### Running Analysis

To run the Analysis, you need to run the analysis.py file by following the steps below:

```bash
# navigate to dato folder
$ cd dato

# activate the virtual environment
$ source dato-env/bin/activate

# navigate to analysis folder
$ cd analysis

# navigate to src folder
$ cd src

# run the analysis.py file with the preferred parameter
$ python2.7 analysis.py -s tweet_total
$ python2.7 analysis.py -s user_total
$ python2.7 analysis.py -s artist_total
$ python2.7 analysis.py -s track_total

$ python2.7 analysis.py -s user_stat
$ python2.7 analysis.py -s source_stat
$ python2.7 analysis.py -s artist_stat
$ python2.7 analysis.py -s track_stat
$ python2.7 analysis.py -s artist_track_stat
$ python2.7 analysis.py -s user_filtered

# when done, deactivate the virtual environment
$ deactivate
```

The `analysis.py` script saves the following files at the following paths:

```
# user stats
dato/analysis/output/user_2016_04_06.csv

# source stats
dato/analysis/output/source_2016_04_06.csv

# artist stats
dato/analysis/output/artist_2016_04_06.csv

# track stats
dato/analysis/output/track_2016_04_06.csv

# artist and track stats
dato/analysis/output/artist_track_2016_04_06.csv

# user id and item id from the full dataset
dato/analysis/output/user_id_item_id_2016_04_06.csv

# user ids of users with 3 or more tweets
dato/analysis/output/user_count_3_2016_04_06.csv

# filtered user id and item id of users with 3 or more tweets
dato/analysis/output/filtered_user_count_3_2016_04_06.csv
```

The `analysis.py` also prints to terminal the following:

1. Total number of tweets in the full dataset
2. Total number of tweets in the subset
3. Total number of users in the full dataset
4. Total number of users in the subset
5. Total number of artists in the full dataset
6. Total number of tracks in the full dataset

##### Running Basic Recommenders

Basic Recommenders available:

* Item Similarity Model
* Popularity-based Recommender Model
* Factorization Recommender for Ranking Model

```bash
# navigate to dato folder
$ cd dato

# activate the virtual environment
$ source dato-env/bin/activate

# navigate to basic_rm folder
$ cd basic_rm

# navigate to src folder
$ cd src

# run the basic_rm.py file with the preferred parameter
# @param item_sim for item_similarity
# @param rank_fact for factorization recommender for ranking
# @param pop for popularity-based recommender
$ python2.7 basic_rm.py -b_rm item_sim
$ python2.7 basic_rm.py -b_rm rank_fact
$ python2.7 basic_rm.py -b_rm pop

# when done, deactivate the virtual environment
$ deactivate
```

The `basic_rm.py` script saves the following files at the following paths:

```
# item similarity model recommendations
dato/basic_rm/output/item_sim_recs.csv

# item similarity model similar items
dato/basic_rm/output/item_sim_sim_items.csv

# factorization recommender for ranking model recommendations
dato/basic_rm/output/rank_fact_recs.csv

# factorization recommender for ranking model similar items
dato/basic_rm/output/rank_fact_sim_items.csv

# popularity-based model recommendations
dato/basic_rm/output/pop_recs.csv

# popularity-based model similar items
dato/basic_rm/output/pop_sim_items.csv
```

