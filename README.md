# Infinispan Pokemon

This demo uses the query and REST capabilities of Infinispan Server to help you battle Pokemons!

Data is ingested as JSON, and internally stored efficiently as Protobuf. Both query and retrieval happens using JSON
taking advantage of the mapping between Protobuf and JSON present in Infinispan

## Requirements

* Download the dataset ```archive.zip``` from https://www.kaggle.com/rounakbanik/pokemon
* Make sure Python 3 installed ```python --version```

## Running 

* Start Infinispan Server:

  ```docker run -it --name infinispan-server -p 11222:11222 -e "USER=user" -e "PASS=user" infinispan/server:13.0```

* Prepare data

  ```python3 prepare-data.py```
  
* Creating an indexed cache

  ```curl -u user:user --digest -H "Content-Type: application/json" -d '{"distributed-cache":{"mode":"SYNC","encoding":{"key":{"media-type":"application/x-protostream"},"value":{"media-type":"application/x-protostream"}},"indexing":{"indexed-entities":["Pokemon"]}}}' http://127.0.0.1:11222/rest/v2/caches/pokemon ```

* Register the protobuf schema

  ``` curl -u user:user --digest --data-binary @./pokemon.proto http://127.0.0.1:11222/rest/v2/schemas/pokemon.proto ```

* Ingest data

   ```./ingest-data.sh```
   
## Querying

Example queries:

* Get Pokemon by key (name)

    [http://localhost:11222/rest/v2/caches/pokemon/Whismur](http://localhost:11222/rest/v2/caches/pokemon/Whismur)

* Get all Pokemons: 
  
   [from Pokemon](http://localhost:11222/rest/v2/caches/pokemon?action=search&query=from%20Pokemon)
   
* Count Pokemons by generation:

   [select count(p.name) from Pokemon group by generation](http://localhost:11222/rest/v2/caches/pokemon?action=search&query=select%20count(p.name)%20from%20Pokemon%20p%20group%20by%20generation)
   
* Do a full text search on the name

  [from Pokemon where name:'pikachu'](http://localhost:11222/rest/v2/caches/pokemon?action=search&query=from%20Pokemon%20where%20name:%27pikachu%27)
  
* Select top 5 Pokemons that can better withstand fire:

  [from Pokemon order by against_fire](http://localhost:11222/rest/v2/caches/pokemon?action=search&query=from%20Pokemon%20order%20by%20against_fire%20asc&max_results=5)

