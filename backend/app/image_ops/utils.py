import ssl
import requests
ssl._create_default_https_context = ssl._create_unverified_context

def download_image_with_url(url: str, output_name: str):
    r = requests.get(url, allow_redirects=True)
    open(output_name + '.jpg', 'wb').write(r.content)

if __name__ == '__main__':

    # Testing
    my_url = "http://www.gunnerkrigg.com//comics/00000001.jpg"
    my_filename = "image1"
    download_image_with_url(my_url, my_filename)
