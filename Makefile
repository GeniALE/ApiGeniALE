.PHONY: help dev

PYTHON ?= python
HOST ?= 127.0.0.1
PORT ?= 8000

help: ## Affiche la liste des commandes disponibles
	@echo "Commandes disponibles :"
	@awk 'BEGIN {FS = ":.*## "} /^[a-zA-Z_-]+:.*## / {printf "  %-12s %s\n", $$1, $$2}' MAKEFILE

dev: ## Lance le serveur API en mode developpement (reload)
	$(PYTHON) -m uvicorn app.app:app --reload --host $(HOST) --port $(PORT)
