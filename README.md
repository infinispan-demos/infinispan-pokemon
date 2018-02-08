# Infinispan Pokemon

This demo uses the query and REST capabilities of Infinispan Server 9.2 to help you battle Pokemons!

Data is ingested as JSON, and internally stored efficiently as Protobuf. Both query and retrieval happens using JSON
taking advantage of the mapping between Protobuf and JSON present in Infinispan

## Requirements

* Download the dataset ```pokemon.zip``` from https://www.kaggle.com/rounakbanik/pokemon
* Make sure Python 3 installed ```python --version```

## Running 

* Start Infinispan 9.2:

  ```docker run -it --name infinispan-server -p 8080:8080 -e "APP_USER=user" -e "APP_PASS=user" jboss/infinispan-server:9.2.0.CR2```

* Register the protobuf schema
  
  ```curl -u user:user -X POST --data-binary @./pokemon.proto http://127.0.0.1:8080/rest/___protobuf_metadata/pokemon.proto```

* Prepare data

  ```python3 prepare-data.py```
  
* Creating an indexed cache

  ``` ./create-cache.sh ```

* Ingest data

   ``` ./ingest-data.sh```
   
## Querying

Example queries:

* Get Pokemon by key (name)

    [http://localhost:8080/rest/pokemon/Whismur](http://127.0.0.1:8080/rest/pokemon/Whismur)

* Get all Pokemons: 
  
   [from Pokemon](http://localhost:8080/rest/pokemon?action=search&query=from%20Pokemon)
   
* Count Pokemons by generation:

   [select count(p.name) from Pokemon group by generation](http://localhost:8080/rest/pokemon?action=search&query=select%20count(p.name)%20from%20Pokemon%20p%20group%20by%20generation)
   
* Do a full text search on the name

  [from Pokemon where name:'pikachu'](http://localhost:8080/rest/pokemon?action=search&query=from%20Pokemon%20where%20name:%27pikachu%27)
  
* Select top 5 Pokemons that can better withstand fire:

  [from Pokemon order by against_fire](http://localhost:8080/rest/pokemon?action=search&query=from%20Pokemon%20order%20by%20against_fire%20asc&max_results=5)

    