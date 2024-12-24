build:
	docker build -f images/local/Dockerfile -t docchat-ai .

run:
	docker run --rm docchat-ai "$(PROMPT)"
