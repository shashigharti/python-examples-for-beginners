Python Practice For Beginners

------------------------------------------------------------------------------------------------
Project Overview:
-----------------

This repo contains python coding examples for beginners. I will be adding practice projects
with varying difficulty levels. These examples will be a mix of problem solving, datastructure
and machine learning problems. I started this to practice machine learning and refine my python 
skills. I hope this will be helpful to others who are at the beginners level and want to improve
their coding skills.

------------------------------------------------------------------------------------------------

Libraries Used:
---------------
1. Pytest for unit testing
2. Python 3 (I have version 3.7.6)
3. Code Formatter(Black: https://pypi.org/project/black/)

File Structure:
---------------
1. all modules => /packages folder
2. notebooks => /notebooks folder
3. tests => /tests folders

Examples:
---------------
1. [Exploring linear, exponential and quadratic functions](https://github.com/shashigharti/python-examples-for-beginners/blob/master/notebooks/functions.ipynb)
2. [Binomial Distribution](https://github.com/shashigharti/python-examples-for-beginners/blob/master/notebooks/binomial_distribution.ipynb)
3. [Twitter Scrapper](https://github.com/shashigharti/python-examples-for-beginners/blob/master/notebooks/twitter_scrapper.ipynb)
4. Prepare own dataset for 'Nutrient Deficiency in Tomato'
    4.1 [Scrapping](https://github.com/shashigharti/python-examples-for-beginners/blob/master/notebooks/scrapping-plant-images-with-nutrient-deficiency.ipynb)
    4.2 [Image Processing](https://github.com/shashigharti/python-examples-for-beginners/blob/master/notebooks/plant-nutrient-deficiency/process-images.ipynb)

Getting Started:
---------------

- Clone the repo

```
git clone git@github.com:shashigharti/python-examples-for-beginners.git
```

- Create a virtual environment using anaconda tool (https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
    - python version 3 or above

- Once virtual environment is setup install 
    - pytest
    - numpy

- To run tests run:

```
pytest
```
   OR

```
python -m pytest
```

- To check code usage in notebook run:

``` 
jupyter notebook
```