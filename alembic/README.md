## Database Migration Tool
Generic single-database configuration.
This is a Database Migration tool for SQLAlchemy.

I configured env.py so that Database URL is obtained from config object, consistent with config.py

## Updating DB
When creating/deleting/modifying DB tables, type:
```
alembic revision --autogenerate
alembic upgrade head
```
Alembic automatically detects revisions and updates them in DB.