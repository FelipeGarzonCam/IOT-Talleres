.PHONY: install local build up down

install: ## Prepara entorno local
	bash install.sh

local:
	bash -c "source venv/bin/activate && python src/spacemax_defender.py"


build: ## Construye la imagen Docker
	docker build -t spacemax-defender:latest .

up: build ## Arranca contenedor
	docker-compose up --build

down: ## Para y elimina contenedor
	docker-compose down
