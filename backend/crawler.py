import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_social_media_posts(social_media, username):
    options = webdriver.ChromeOptions()
    options.headless = True

    # Automatically download and configure the appropriate ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Set URL based on social media type
    if social_media == 'twitter':
        url = f'https://twitter.com/{username}'
    elif social_media == 'instagram':
        url = f'https://www.instagram.com/{username}/'
    elif social_media == 'facebook':
        url = f'https://www.facebook.com/{username}'
    else:
        driver.quit()
        return [], 0

    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    posts = []
    if social_media == 'twitter':
        elements = driver.find_elements(By.CSS_SELECTOR, 'article a[href]')
        for elem in elements[:5]:  # Limit to 5 posts
            post_url = elem.get_attribute('href')
            posts.append({'url': post_url})

    elif social_media == 'instagram':
        elements = driver.find_elements(By.CSS_SELECTOR, 'article a')
        for elem in elements[:5]:
            post_url = elem.get_attribute('href')
            posts.append({'url': post_url})

    elif social_media == 'facebook':
        elements = driver.find_elements(By.CSS_SELECTOR, f'a[href^="https://www.facebook.com/{username}/posts/"]')
        for elem in elements[:5]:
            post_url = elem.get_attribute('href')
            posts.append({'url': post_url})

    driver.quit()
    return posts, len(posts)
