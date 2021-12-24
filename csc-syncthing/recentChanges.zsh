

curl -H "X-API-Key: $SYNCTHING_APIKEY" localhost:8384/rest/events | grep "\.md" | grep -v "item" | uniq
