from selenium import webdriver
import time
import urllib.request

class GettyImage(object):
	"""docstring for GettyImage"""
	def __init__(self, query, img_url, alt_text):
		super(GettyImage, self).__init__()
		self.query = query
		self.url = img_url
		self.alt_text = alt_text

	def save_image(self, path):
		try:
			urllib.request.urlretrieve(self.url, '{0}/{1}'.format(path, self.url.split("/")[-1]))
			return True
		except:
			return False

class GettyScraper(object):
	"""docstring for GettyScraper"""
	def __init__(self):
		super(GettyScraper, self).__init__()
		self.base_search_url = "https://www.gettyimages.com/photos/"
		self.driver = webdriver
		self.profile = self.driver.FirefoxProfile()
		self.browser = self.driver.Firefox(firefox_profile=self.profile)
		self.query = ""
		self.ScrapedImageObjects = []

	def generate_image_objects(self):
		img_elems = self.browser.find_elements_by_xpath("//img[contains(@class, 'gallery-asset__thumb gallery-mosaic-asset__thumb')]")
		for e in img_elems:
			try:
				img_url = e.get_attribute("src").split("?")[0]
				alt_text = e.get_attribute("alt")
				getty_image = GettyImage(self.query, img_url, alt_text)
				self.ScrapedImageObjects.append(getty_image)
			except:
				print("Failed to scrape element: {0}".format(e))
				continue

	def process_pages_from_query(self, query, page_count=0):
		self.query = query
		self.browser.get(self.base_search_url + query)
		time.sleep(0.5)
		self.generate_image_objects()
		if page_count == 0:
			self.total_pages = self.browser.find_element_by_class_name("search-pagination__last-page").text
		else:
			self.total_pages = page_count
		for p in range(1, int(self.total_pages)):
			next_page = "https://www.gettyimages.com/photos/{0}?page={1}".format(query, p)
			self.browser.get(next_page)						
			time.sleep(0.5)
			self.generate_image_objects()