# Duckduckgo Images Downloader
> This library provides utilities to download images using duckduckgo images search.


## Install

`pip install ddg_images_downloader`

#### Install chromium and chromedriver

> If on linux, you can install chromium and chrome driver using the `apt` tool.
>
```
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
```

## How to use

**Import library**

```python
from pathlib import Path
from fastcore.utils import *
from ddg_images_downloader.images import *
```

### Create text files 
```
download_search_urls(path, search_term, search_pattern, **kwargs)
```
> Each textfile containing the list of urls for each search term  

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
path.ls()
```

### Download list of urls from a text file named after the search term
```download_search_images_slowly(path,search_terms)
```
> Each text file named after the search term containing the list of urls will
> be downloaded into a separate folder

```python
# slow
download_search_images_slowly(path,bear_types)
```
