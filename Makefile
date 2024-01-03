build:
	@echo "Building Docker containers..."
	docker compose build

up:
	@echo "Starting Docker containers..."
	docker compose up -d

up-build:
	@echo "Starting Docker containers..."
	docker compose up -d --build

down:
	@echo "Stopping Docker containers..."
	docker compose down

restart:
	@echo "Restarting Docker containers..."
	docker compose restart

logs:
	@echo "Showing Docker logs..."
	docker compose logs -f

exec-api:
	@echo "Executing API container..."
	docker exec -it udacity-todo-udado-api-1 bash