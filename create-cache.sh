#!/usr/bin/env bash

docker exec -ti infinispan-server /opt/jboss/infinispan-server/bin/ispn-cli.sh -c command="/subsystem=datagrid-infinispan/cache-container=clustered/configurations=CONFIGURATIONS/distributed-cache-configuration=pokemonConfig:add(start=EAGER,mode=SYNC,template=false)"
docker exec -ti infinispan-server /opt/jboss/infinispan-server/bin/ispn-cli.sh -c command="/subsystem=datagrid-infinispan/cache-container=clustered/configurations=CONFIGURATIONS/distributed-cache-configuration=pokemonConfig/indexing=INDEXING:add(auto-config=true,indexing=LOCAL)"
docker exec -ti infinispan-server /opt/jboss/infinispan-server/bin/ispn-cli.sh -c command="/subsystem=datagrid-infinispan/cache-container=clustered/distributed-cache=pokemon:add(configuration=pokemonConfig)"