.PHONY: html clean

html: Makefile
	sphinx-build -M html . _build

clean:
	-rm -rf _build
