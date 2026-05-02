.PHONY: build clean

build:
	@mkdir -p build release
	@python3 .github/scripts/convert_to_latex.py
	@cp latex/*.tex build/
	@cd build && xelatex -interaction=nonstopmode book.tex && xelatex -interaction=nonstopmode book.tex
	@cp build/book.pdf release/重塑组织逻辑.pdf

clean:
	@rm -rf build release
	@echo "Cleaned build/ and release/"