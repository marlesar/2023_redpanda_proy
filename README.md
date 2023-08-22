# redpanda_proy
Este repositorio contiene la tarea módulo data streaming del diplomado de UNA Big Data 2023.

## Prerequisitos
- Python 3 con pip
- Docker
- Visual Studio Code (opcional)

Instalar paquete `kafka-python`:
```
pip install kafka-python
```

## Iniciar un cluster single-node Redpanda & KsqlDB

```
docker compose up -d
```

## Generar y consumir JSON

Ejecutar `producer.py` para generar consultas a la Api Finnhub en el topic `stock-updates`. Posteriormente ejecutar `consumer.py` para consumirlas.

## KsqlDB Queries

Ejecutar `docker exec -it ksqldb-cli ksql http://ksqldb-server:8088` para iniciar KsqlDB.
Ejecutar los queries de `ksqldb.sql` para la creacion de stream y tablas.

## Clean

Limpiar el contenedor ejecutando:

```
docker compose down
```

