import json

from kafka import KafkaConsumer

result = {}
counter = {}

consumer = KafkaConsumer(
  bootstrap_servers=["localhost:9092"],
  group_id="demo-group",
  auto_offset_reset="earliest",
  enable_auto_commit=False,
  consumer_timeout_ms=5000,
  value_deserializer=lambda m: json.loads(m.decode("ascii")),
)
consumer.subscribe("stock-updates")

try:
    for message in consumer:
        data = message.value
        result.setdefault(data["symbol"],{"weighted_price": 0, "total_volume": 0, "min_offset": 10000000000000, 
                                          "trx_qty": 0, "max_price": 0, "min_price": 0 },)
        result[data["symbol"]]["weighted_price"] += data["price"] * data["volume"]
        result[data["symbol"]]["total_volume"] += data["volume"]
        result[data["symbol"]]["min_offset"] = min([result[data["symbol"]]["min_offset"], message.offset])
        result[data["symbol"]]["trx_qty"] += 1
        result[data["symbol"]]["max_price"] = max([result[data["symbol"]]["max_price"], data["price"]])
        result[data["symbol"]]["min_price"] = min([result[data["symbol"]]["min_price"], data["price"]])
        
        print(data)
except Exception as e:
    print(f"Error occurred while consuming messages: {e}")
finally:
    for key in result:
        print(f"Weighted average price for {key}: {result[key]['weighted_price']/result[key]['total_volume']}")
        print(f"TRX count for {key}: {result[key]['trx_qty']}")
        print(f"Max price for {key}: {result[key]['max_price']}")
        print(f"Min price for {key}: {result[key]['min_price']}")
    consumer.close()
