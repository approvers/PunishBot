.PHONY: sync
sync:
	uv sync

.PHONY: sleep-infinity
sleep-infinity:
	sleep infinity

.PHONY: run
run: sleep-infinity

.PHONY: up
up:
	docker compose up -d

.PHONY: dev
dev: up
	docker compose watch

.PHONY: rebuild
rebuild:
	docker compose up -d --build
