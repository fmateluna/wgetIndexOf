import argparse
import urllib
from bs4 import BeautifulSoup
import urllib2
import os

__author__ = 'Sanukode'
__copyright__ = 'WGET INDEX OF'
__credits__ = ['LVS']

__license__ = 'GPL'
__version__ = '0.1'
__email__ = 'fernando.mateluna@gmail.com'
__maintainer__ = 'Fernando Mateluna'
__status__ = 'CTO'

url = ""
thread = 0


#obtener todos los valores href o src desde el html
def get_Href_From_Url(url):
    download = []
    ht= urllib.urlopen(url)
    html_page = ht.read()
    b_object = BeautifulSoup(html_page, "lxml")
    for link in b_object.find_all('a'):
        url_href = "{}/{}".format(url,link.get('href'))
        try:
            ret = urllib2.urlopen(url_href)
            if ret.code == 200:
                print("{} {}".format(ret.code, url_href))
                os.system("wget {}".format(url_href))
                download.append(url_href)
        except :
            pass
    return download


# obtener url "index of" desde parametros
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="WGET Index of.")
    parser.add_argument('-url', help="Url ""index of"" site", default=None)
    args = parser.parse_args()
    url = args.url
    download_url = get_Href_From_Url(url)
    if download_url:
        print("{} file download!".format(len(download_url)))
    else:
        print("This URL {} not is a 'index of' page".format(url))


