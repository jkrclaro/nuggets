# GET /containers

List running containers

# Usage
```bash
python server.py
```

# Get data via CURL
- Please ensure the server is currently running (see Usage)
- Paste the curl command in your terminal
```bash
curl -s -X GET -H 'Accept: application/json' http://localhost:8080/containers?state=running | python -mjson.tool
```

You should get the same result as you would if you were to visit
http://localhost:8080/containers?state=running in your browser