makemigrations:
	docker-compose exec -T backend /bin/bash -c "alembic -c alembic/alembic.ini revision --autogenerate -m '$(name)'"

psql:
	docker-compose exec db /bin/bash -c "psql -U feedback -d feedback"
