#!/usr/bin/env bash
set -e

status=0
for f in data/*.json
do 
  curl -u user:user --digest --data-binary @${f}  -H "Content-Type: application/json; charset=UTF-8"  http://127.0.0.1:11222/rest/v2/caches/pokemon/$(basename $f .json)
  let status=status+1
  echo  "Imported $f (total $status pokemons)"
done
