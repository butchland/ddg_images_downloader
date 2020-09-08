# Duckduckgo Images Downloader
> This package provides functions to download images using duckduckgo images search.


## Installation

`pip install git+https://github.com/butchland/ddg_images_downloader.git`

#### Install chromium and chromedriver
> In order to run the package, you need to install chromium and chromedriver
> If you are running on linux, you can install chromium and chrome driver using the `apt` tool.
>
```
!apt-get update
!apt install chromium-chromedriver
```
> If on other OS (Mac or Windows), please see instructions on setting up chrome driver with Selenium on 
> your platform.
> See [Chrome Driver Getting Started](https://chromedriver.chromium.org/getting-started) for details.

## How to use

**Import library**

```
from pathlib import Path
from fastcore.utils import *
from ddg_images_downloader.images import *
```

### Download image urls and save to text files
> This function will download the image urls and save them into textfiles
```
download_search_urls(path, search_terms, search_pattern, **kwargs)
```
> Each textfile contains the list of urls for each search term and are named after the search term 

#### An example

```
bear_types = ['teddy','black']
path = Path('bears')
```

```
# slow
!rm -rf bears
download_search_urls(path, bear_types,'{0} bear',scroll_count=4,sleep=5)
```

```
!ls -ald {path.as_posix()}/*
```

    drwxr-xr-x  473 butch  staff  15136 May 21 22:07 [34mbears/black[m[m
    -rw-r--r--    1 butch  staff  34854 May 21 21:56 bears/black.txt
    drwxr-xr-x  471 butch  staff  15072 May 21 22:02 [34mbears/teddy[m[m
    -rw-r--r--    1 butch  staff  34706 May 21 21:55 bears/teddy.txt


### Download list of urls from a text file named after the search term
```download_search_images_slowly(path,search_terms)
```
> Each text file named after the search term containing the list of urls will
> be downloaded into a separate folder

```
# slow
download_search_images_slowly(path,bear_types)
```

### Search and Download  single search terms

Aside from retrieving urls from multiple search terms, you can also search for
a single search term and save the retrieved urls to a file.

#### An example

Retrieve image urls into a file

```
!mkdir fruits
download_search_url('passion fruit',Path('fruits')/'passion.txt',scroll_count=3)
```

    passion fruit 357


Download the images into a folder

```
download_images_slowly(Path('fruits')/'passion',Path('fruits')/'passion.txt')
```

    downloaded:  0  dest:  fruits/passion
    downloaded:  10  dest:  fruits/passion
    downloaded:  20  dest:  fruits/passion
    downloaded:  30  dest:  fruits/passion
    downloaded:  40  dest:  fruits/passion
    downloaded:  50  dest:  fruits/passion
    downloaded:  60  dest:  fruits/passion
    downloaded:  70  dest:  fruits/passion
    downloaded:  80  dest:  fruits/passion
    downloaded:  90  dest:  fruits/passion
    downloaded:  100  dest:  fruits/passion
    downloaded:  110  dest:  fruits/passion
    downloaded:  120  dest:  fruits/passion
    downloaded:  130  dest:  fruits/passion
    downloaded:  140  dest:  fruits/passion
    downloaded:  150  dest:  fruits/passion
    downloaded:  160  dest:  fruits/passion
    downloaded:  170  dest:  fruits/passion
    downloaded:  180  dest:  fruits/passion
    downloaded:  190  dest:  fruits/passion
    downloaded:  200  dest:  fruits/passion
    downloaded:  210  dest:  fruits/passion
    downloaded:  220  dest:  fruits/passion
    downloaded:  230  dest:  fruits/passion
    downloaded:  240  dest:  fruits/passion
    downloaded:  250  dest:  fruits/passion
    downloaded:  260  dest:  fruits/passion
    downloaded:  270  dest:  fruits/passion
    downloaded:  280  dest:  fruits/passion
    downloaded:  290  dest:  fruits/passion
    downloaded:  300  dest:  fruits/passion
    downloaded:  310  dest:  fruits/passion
    downloaded:  320  dest:  fruits/passion
    downloaded:  330  dest:  fruits/passion
    downloaded:  340  dest:  fruits/passion
    downloaded:  350  dest:  fruits/passion


### Samples

A sample notebook for downloading simple terms is [provided here](https://github.com/butchland/ddg_images_downloader/blob/master/samples/ddg_images_downloader_example.ipynb) that is runnable on Colab : 

[![](https://camo.githubusercontent.com/52feade06f2fecbf006889a904d221e6a730c194/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/butchland/ddg_images_downloader/blob/master/samples/ddg_images_downloader_example.ipynb)
