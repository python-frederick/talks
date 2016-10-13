all: slides


slides: README.md
	pandoc -s -i -t revealjs -V theme=moon -V history=true -o $@.html $<
