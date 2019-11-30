import sys
sys.path.insert(1, '../')

from GettyScraper import GettyScraper

q = "danny devito"
gs = GettyScraper()

gs.process_pages_from_query(q, page_count=3)
for img in gs.ScrapedImageObjects:
	img.save_image("/tmp/dump/")
	print(img.query)
	print(img.url)
	print(img.alt_text)