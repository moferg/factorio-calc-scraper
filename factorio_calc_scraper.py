# Factorio Calc Scraper - Marshall Ferguson - 8/2020

# TODO: Figure out template for url to get different results from calc

# base url =    https://kirkmcdonald.github.io/calc.html

# data set =    #data="inset data set"
# data set determines which version of Factorio the recipe is for
# data set should be kept up to date in case of recipe changes

# item =        &items="inset item name"
# item determines which item the recipe is for
# item names will name to exactly match a specific syntax

# factories =   :f:"inset number of factories"
# factories determines the number of factories (assembly machines) working on the recipe
# factories syntax defaults to assembly machine 1, another change to url is needed for assembly machines 2 and 3

# rate =        :r:"inset rate"
# rate determines the rate at which the recipe is worked on
# rate defaults to items/minute, another change to url is needed for items/seond and items/hour

# example url = https://kirkmcdonald.github.io/calc.html#data=1-0-0&items=electronic-circuit:f:1
# example url syntax = base url + data set + items + factories OR rate

# In the future, this script will be able to handle different levels of assembly machines and rates, but for now it will focus on the defaults

# TODO: Request web page

# TODO: Parse through HTML to get link to .csv

# TODO: Pull data from .csv

# TODO: Manipulate data from .csv to show total number of assemblers needed