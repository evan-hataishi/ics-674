TEX_SOURCES = $(shell find . -name "*.tex")
BIB_SOURCES = $(shell find . -name "*.bib")
MAIN = main

default: $(MAIN).pdf

$(MAIN).pdf: $(TEX_SOURCES) $(BIB_SOURCES)
	pdflatex $(MAIN)
	# bibtex $(MAIN)
	pdflatex $(MAIN)
	pdflatex $(MAIN)


clean:
	/bin/rm -rf *.aux *log *.blg *.bbl *.out
	touch *.tex *.bib
