dist:
	python setup.py sdist bdist_wheel

clean:
	-rm -rf build/ dist/ *.egg-info

upload: clean dist
	python -m twine upload --repository pypi dist/*

test: clean dist
	python -m twine upload --repository testpypi dist/*

.PHONY: dist clean upload test
