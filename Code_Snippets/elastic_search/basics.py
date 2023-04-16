from elasticsearch import Elasticsearch

config = {
    "host": "localhhost",
    "port": 9200
}


ELASTIC_PASSWORD = "ivNbJFD-QHXZZZ3KhFPR"
CERT_FINGERPRINT  = "aaef55be51c34aec52942c598356c1bc53b2fd17356efd029368151977b567bb"
CA_CERT_PATH = "D:\Program Files\elasticsearch-8.7.0-windows-x86_64\elasticsearch-8.7.0\config\certs\http_ca.crt"

# Create the client instance
es = Elasticsearch(
    "https://localhost:9200",
    ca_certs=CA_CERT_PATH,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

# Successful response!
print(es.info())
print(es.ping)

# create indices
# es.indices.create(index="hello")

# display all existing indexes
existing_indexes = es.indices.get_alias(index="*", pretty=True)
print(f"\nExisting indexes: ")
for index in existing_indexes:
    print(f"-->{index}")

# check if index is available -> throws exception if index not found
check_index = es.search(index="hello")
print(check_index)