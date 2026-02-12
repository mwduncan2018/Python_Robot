# Python_Robot

### Test Execution

```
Local Series
robot -P . -d results tests/

Local Parallel
pabot -P . -d results --processes 4 tests/

Docker Build Image
docker build -t robot:1.0 .

Docker Series
docker run --rm -v "${PWD}/results:/opt/robotframework/tests/results" robot:1.0 robot -d results tests/

Docker Parallel
docker run --rm -v "${PWD}/results:/opt/robotframework/tests/results" robot:1.0 pabot -d results --processes 2 tests/
```
