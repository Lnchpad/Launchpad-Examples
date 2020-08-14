import app_pb2
import base64
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

app = app_pb2.PortalAppDeployment()
app.appName = "christian"

#base64encoded = base64.b64encode(app.SerializeToString())
producer.send('launchpad.app.deployment', app.SerializeToString())
producer.flush()

