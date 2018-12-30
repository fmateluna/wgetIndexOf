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
ext = ""
text = ""
thread = 0


#obtener todos los valores href o src desde el html
def get_Href_From_Url(url):
    print("wget {}".format(url))
    download = []
    ht= urllib.urlopen(url)
    html_page = ht.read()
    b_object = BeautifulSoup(html_page, "html5lib")
    to_download = False
    for link in b_object.find_all('a'):
        url_href = "{}/{}".format(url,link.get('href'))
        print("get info from : {}".format(url_href))
        try:
            to_download = False
            if (ext == "") or (text == ""):
                to_download = True
            else:
                if url_href.endswith(ext):
                    to_download = True
                print("get {}".format(url_href.split("/")[-1]))
                if text in url_href.split("/")[-1]:
                    to_download = True
            if to_download:
                ret = urllib2.urlopen(url_href)
                if ret.code == 200:
                    print("{} {}".format(ret.code, url_href))
                    os.system("wget {}".format(url_href))
                    download.append(url_href)
                else:
                    print("Error :{}".format(ret.code))
            if url_href.endswith("/"):
                if not 'Parent Directory' in link.text:
                    get_Href_From_Url(url_href)
        except :
            pass
    return download


# obtener url "index of" desde parametros
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="WGET Index of.")
    parser.add_argument('-url', help="Url ""index of"" site", default=None)
    parser.add_argument('-ext', help="Extension to Download", default="")
    parser.add_argument('-contains', help="contains any string in the text of href", default="")
    args = parser.parse_args()
    url = args.url
    ext = args.ext
    text = args.contains
    download_url = get_Href_From_Url(url)
    if download_url:
        print("{} file download!".format(len(download_url)))
    else:
        print("This URL {} not is a 'index of' page".format(url))
