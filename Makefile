SRC = $(wildcard ./*.ipynb)

all: ddg_images_downloader docs

ddg_images_downloader: $(SRC)
	nbdev_build_lib
	touch ddg_images_downloader

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist