
## Collaborative filtering project using Deep Learning

Coursework project developed as part of the [COMPGI15 - Information Retrieval and Data Mining](http://www.cs.ucl.ac.uk/teaching_learning/syllabus/mscml/gi15_information_retrieval_data_mining/) module at University College London

#### Group Members - MSc. Web Science and Big Data Analytics

* [Santiago Gonzalez](https://github.com/santteegt)
* [Archie Norman](https://github.com/archienorman11)
* [Sergiu Tripon](https://github.com/SergiuTripon)

#### Dataset

#### System Requirements

#### Installation

Fork repo then clone using:

```bash
git clone https://github.com/YOUR-USERNAME/ucl-irdm-collaborative-filtering
```

##### Setting up GraphLab Create

GraphLab Create is a machine learning framework provided by Dato. In order to use GraphLab Create a license is required. Dato's Academic Programme offers a 1-year free license of GraphLab Create. In order to obtain a license, visit https://dato.com/download/academic.html and register using a @ucl.ac.uk or @cs.ucl.ac.uk account.

Once you have obtained a GraphLab Create license, forked the repo and then cloned, follow the steps below:

```bash
# navigate to ucl-irdm-collaborative-filtering folder
$ cd ucl-irdm-collaborative-filtering

# navigate to dato folder
$ cd dato
```

```bash
# Create a new virtual environment with Python 2.7.x
$ virtualenv -p /usr/bin/python2.7 dato-env
```

```bash
$ source dato-env/bin/activate
```

```bash
# Ensure pip is updated to the latest version
$ pip install --upgrade pip
```

```bash
# Install your licensed copy of GraphLab Create
$ pip install --upgrade --no-cache-dir pip install --upgrade --no-cache-dir https://get.dato.com/GraphLab-Create/1.8.5/your registered email address here/your product key here/GraphLab-Create-License.tar.gz
```

##### Running Analysis

##### Running Basic Recommenders
