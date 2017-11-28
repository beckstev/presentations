all: build/presentation.pdf

build/presentation.pdf: presentation_short.tex header.tex| build
		lualatex --output-directory=build presentation_short.tex

full: presentation_short.tex header.tex | build
		lualatex --output-directory=build presentation_short.tex
		biber build/presentation_short.bcf
		lualatex --output-directory=build presentation_short.tex

build:
		mkdir -p build

clean:
		rm -rf build
.PHONY: clean all
