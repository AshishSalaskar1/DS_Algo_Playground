### Setup Tips
- **TUTORIAL**: https://www.youtube.com/watch?v=C-JKcMM6IXE
- Downlaod Kibana and Elastic Search (run executbale in /bin folder for both)
- Kibana port: http://localhost:5601 
- ES port: http://localhost:9902 
- Python client for elasticsearch: https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html
- Make sure python_client_version == elasticsearch_version of the server
- Kibana default username: elastic, password: found from the terminal when it runs

#### **Local Setup**
First do make sure that you have all the serials and deserializers in plave so that you can then call then to make 
1. Download and extract Kibana and Elasticsearch 
2. Execute /bin/elasticsearch.bat and /bin/kibana.bat in two separate terminals
3. From elasticsearch terminal startup logs you can find password, user: elastic, certificate_fingerprint and also the token to setup kibana
4. Kibana is accesible via the following link: http://localhost:5601/
5. ```python
    es = Elasticsearch(
        "https://localhost:9200",
        ca_certs="elasticsearch_path/cofig/certs/http_ca.cert",
        basic_auth=("elastic", ELASTIC_PASSWORD)
    )

    print(es.info())
    ```

### Connection and authentication
https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/connecting.html

### Notes
- In elasticsearch index == database in RDBMS


### **Kibana/Search query**
- check indices: `GET _cat/indices`



