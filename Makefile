clean:
	rm -rf apps/**/migrations
	rm -rf apps/**/tests.py

migrations:
	python manage.py makemigrations access account

migrate:
    python manage.py migrate
