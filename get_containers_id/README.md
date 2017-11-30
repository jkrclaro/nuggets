# GET /containers/<container_id>

Inspect a specific container

# Usage
```bash
python server.py
```

# Get data via CURL
- Please ensure the server is currently running (see Usage)
- Paste the curl command in your terminal
```bash
curl -s -X GET -H 'Accept: application/json' http://localhost:8080/containers/12345 | python -mjson.tool
# where 12345 is an actual docker container ID ! You can check via docker ps
```

You should get the same result as you would if you were to visit
http://localhost:8080/containers/12345 in your browser
