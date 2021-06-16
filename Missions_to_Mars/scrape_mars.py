from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():

    # scrape news item and text from 'https://redplanetscience.com'
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Navigate to location in html       
    news_title = soup.find('div', class_="content_title").text
    news_p = soup.find('div', class_="article_teaser_body").text
    browser.quit()
    print(f"{url} scrape complete")

    # scrape image-url from 'https://spaceimages-mars.com'
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Navigate to location in html 
    results = soup.find_all('div',class_='header')
    # grab url extension
    url_extension = results[0].find_all('a')[2]['href']
    # create full url
    featured_image_url = f"{url}/{url_extension}"
    browser.quit()
    print(f"{url} scrape complete")

    # scrape table from https://galaxyfacts-mars.com
    import pandas as pd
    url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url)
    mars_1_df = tables[0]
    mars_1_df.drop([0], inplace=True)
    mars_1_df.rename(columns={0:"Parameter",1:"Mars",2:"Earth"}, inplace=True)
    html_table = mars_1_df.to_html()
    html_table.split()
    print(f"{url} table scrape complete")
    
    # scrape urls to high-resolution images of Mars' hemispheres
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere_image_urls = []
    a = len(' Enhanced')

    results = soup.find_all('div',class_='item')

    for result in results:
    
        hemi_dict = {}
        
        # Scrape image title
        title = result.h3.text[:-a]
        hemi_dict["title"] = title
        
        # Click into detail using the variable <title> to find link
        browser.links.find_by_partial_text(title).click()
        
    
        # Update html based on the new page
        html = browser.html
        # Update Soup
        soup = BeautifulSoup(html, 'html.parser')
        # New search query for image_url
        result_2 = soup.find_all("div", class_="container")
        url_extension = result_2[0].find_all('img')[2]['src']
        # add full image url to dictionairy
        hemi_dict["img_url"] = f"{url}{url_extension}"
        # Append dictionary to list
        hemisphere_image_urls.append(hemi_dict)
        # Return to landing page (no need to update soup)
        browser.links.find_by_partial_text('Back').click()
    
    browser.quit()
    print(f"{url} scrape complete")

    # Create Python dictionary with all scraped results

    listings = {"news_title": news_title, "news_p": news_p, "featured_image_url": featured_image_url,
    "data_table": html_table, "hemispheres_image_urls": hemisphere_image_urls }


    return listings
























    return