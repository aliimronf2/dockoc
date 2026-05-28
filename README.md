# dockoc
Docker Octopus

1. To run container for postgres

```bash
docker run -it --rm \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v ny_taxi_postgres_data:/var/lib/postgresql \
-p 5432:5432 \
postgres:18
```

2. To connect to it using pgcli:
```bash
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```

3. To run the script
```bash
uv run python ingest_data.py
```

4. To run in docker network
```bash
docker run -it --rm \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v ny_taxi_postgres_data:/var/lib/postgresql \
-p 5432:5432 \
--network=pg-network \
--name pgdatabase \
postgres:18
```

5. 