SET 'auto.offset.reset' = 'earliest';	

CREATE STREAM trades (symbol VARCHAR, price DOUBLE, volume DOUBLE) 
  WITH (kafka_topic='stock-updates', value_format='json', partitions=1);

CREATE TABLE precioavgxsimbolo AS
    SELECT symbol,
           sum(price * volume)/sum(volume) AS avg_price
    FROM trades
    GROUP BY symbol
    EMIT CHANGES;
	
CREATE TABLE transacxsimbolo AS
    SELECT symbol,
           count(symbol) AS count_symbol
    FROM trades
    GROUP BY symbol
    EMIT CHANGES;

CREATE TABLE maxprecioxsimbolo AS
    SELECT symbol,
           max(price) AS max_price
    FROM trades
    GROUP BY symbol
    EMIT CHANGES;
	
CREATE TABLE minprecioxsimbolo AS
    SELECT symbol,
           min(price) AS min_price
    FROM trades
    GROUP BY symbol
    EMIT CHANGES;
