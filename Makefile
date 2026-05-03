.PHONY: build clean

TEX_PATH := /usr/local/texlive/2026/bin/universal-darwin
PATH := $(TEX_PATH):$(PATH)

build:
	@mkdir -p latex build release
	@python3 .github/scripts/convert_to_latex.py
	@cp latex/*.tex build/
	@cd build && xelatex -interaction=nonstopmode book.tex && xelatex -interaction=nonstopmode book.tex
	@cp build/book.pdf release/重塑组织逻辑.pdf

clean:
	@rm -rf latex build release
	@echo "Cleaned latex/, build/ and release/"