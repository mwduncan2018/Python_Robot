# Python_Robot

```
Local Series Test Execution
robot -P . -d results tests/

Local Parallel Test Execution
pabot -P . -d results --processes 4 tests/

Docker Build Image
docker build -t robot:1.0 .

Docker Series Test Execution
docker run --rm -v "${PWD}/results:/opt/robotframework/tests/results" robot:1.0 robot -d results tests/

Docker Parallel Test Execution
docker run --rm -v "${PWD}/results:/opt/robotframework/tests/results" robot:1.0 pabot -d results --processes 2 tests/
```
