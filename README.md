# CMS-SYSTEM
First of all we need to up docker containers:

---
docker-compose -f docker-compose-local.yaml up -d
---

To make migrations if you don't have alembic.ini yet, write the following command:

---
alembic init migrations
---

After this action migration's folder and conf. file will be created 
Go to env.py in migrations, and change the following:

---
from ... import Base
target_metadata = Base.metadata
---


The following step is to make migrations:

---
alembic revision --autogenerate -m "comment"
alembic upgrade heads
---

To run testing change directory to tests: 

---
cd src/backend/tests
---

And then write: 

---
pytest
---