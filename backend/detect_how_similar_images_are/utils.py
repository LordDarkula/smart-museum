import urllib.request

def download_image_with_url(url: str, output_name: str):
	urllib.request.urlretrieve(url, output_name + ".jpg")





# Testing 
my_url = "http://www.gunnerkrigg.com//comics/00000001.jpg"
my_filename = "image1"
download_image_with_url(my_url, my_filename)