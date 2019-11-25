makemigrations:
	docker-compose exec -T backend /bin/bash -c "alembic -c alembic/alembic.ini revision --autogenerate -m '$(name)'"
