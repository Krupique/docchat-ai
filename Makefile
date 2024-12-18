build:
	docker build -f images/Dockerfile -t docchat-ai .

run:
	docker run --rm docchat-ai "$(PROMPT)"
