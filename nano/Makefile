all: build/presentation.pdf

build/presentation.pdf: presentation_long.tex header.tex| build
		lualatex --output-directory=build presentation_long.tex

full: presentation_long.tex header.tex | build
		lualatex --output-directory=build presentation_long.tex
		biber build/presentation_long.bcf
		lualatex --output-directory=build presentation_long.tex

build:
		mkdir -p build

clean:
		rm -rf build
.PHONY: clean all
