# Project 4 - Scraping & Dealing with data - Zuyi Cai

In this project, I use BeautifulSoup to scrape data from the National Parks website: https://www.nps.gov/index.htm

For each state, I scrape data representing all National Sites (which come in many "types" -- National Parks, National Monuments, National Forests, National Military Parks… etc). And I got the results end up with data about a long list of parks that includes these attributes for name of site, type of site, description of site, location value of site and state(s).

Here type of site is "National Park" or "National Forest", etc; Description of site is the sentence/short paragraph describing the site; Location value of site is something like "AL" or could be a city like "Daviston, AL" or could be a list of states like "LA, MS, FL", etc; State(s) is the name or abbreviation of the state(s) that the site is in. In this program, I replaced all missing data and weird values with "No Information".

In this repo, parks.csv is the file saved all data and each row represents 1 national site, and SI507_project4.py is the main file that I created a cache and made all of my requests in the program, saved it all to a JSON file. And every time the program is run, my program checks if there is a cache file already, if there is it opens it and gets the data out, and it checks if the data from the specific URL I need is in there. If it isn't, it makes the request.

Here I showed part of my parks.csv file:

* ![Alt text](https://github.com/zuyicai/image/blob/master/project4/parks.png)


Readers need to follow the steps to install everything needed to run this application.

## Getting Started

* Anaconda installed
* Open your terminal window! `cd` to the place where you want this project to go.
* This repository cloned to somewhere in your computer (the place).
```
git clone <git url>
```
* `cd` into where the project lives
* Create a virtual environment for it
```
virtualenv env
```
* Activate the virtual environment
```
$ source <projectname>-env/bin/activate    # For Mac/Linux...
$ source <projectname>-env/Scripts/activate    # For Windows
(project4-env) $     # you've succeeded if you see this after!
```
* install all requirement
```
pip install -r requirements.txt
```
```
Deactivate
```
* Just run the program!
```
python SI507_project4.py
```
* Check out what’s happening in your terminal window!
* Check the json files and csv file, you may see something like the following picture:
* ![Alt text](https://github.com/zuyicai/image/blob/master/project4/files.png)
