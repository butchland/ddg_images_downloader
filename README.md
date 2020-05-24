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

```python
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

```python
bear_types = ['teddy','black']
path = Path('bears')
```

```python
# slow
!rm -rf bears
download_search_urls(path, bear_types,'{0} bear',scroll_count=4,sleep=5)
```

```python
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

```python
# slow
download_search_images_slowly(path,bear_types)
```
