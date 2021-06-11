all: build open

open:
	open ~/Desktop/RecentDocuments.alfredworkflow

build:
	zip -r ~/Desktop/RecentDocuments.alfredworkflow . -x '*.git*'
