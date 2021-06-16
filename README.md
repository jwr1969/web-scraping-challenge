# web-scraping-challenge

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

# Step 1 - Scraping 

* Scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text.

** Used splinter to navigate the site and found the image url for the current Featured Mars Image ensuring it’s full size `.jpg` image and saving a complete url string for this image.

*** Visited the Mars Facts webpage (https://galaxyfacts-mars.com) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Converted the data to a HTML table string.


**** Visited the astrogeology site (https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres. Clicked each of the links to the hemispheres in order to find the image url to the full resolution image.

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Converted Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data. Tested the scrape_mars.py in Jupyter Notebook.

* In a separate script (app.py) created a route called `/scrape` that imports `scrape_mars.py` script and called `scrape` function. Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that queries Mongo database and passes the mars data into an HTML template (index.html) to display the data.


