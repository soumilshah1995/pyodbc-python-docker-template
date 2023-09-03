

# Python Template with Pyodbc and Docker Container 

# Step 1: Edit .env File 
```
SQL_SERVER='XXXX'
SQL_USERNAME='XXX'
SQL_PASSWORD='XXX'
SQL_PORT=1443
SQL_DATABASE='XX'
SQL_QUERY='SELECT name FROM sys.databases WHERE database_id > 4;'
```
# Step 2: Run the Container 
```
docker build -t qa-container .
docker run --rm qa-container


```
