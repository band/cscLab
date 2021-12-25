

curl -H "X-API-Key: $SYNCTHING_API_KEY" localhost:8384/rest/events | grep "\.md" | grep -v "item" | uniq
