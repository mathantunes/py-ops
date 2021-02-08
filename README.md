# py-ops

## Build docker image

docker build -t pyops .

## Run docker image

docker run -d -p 5000:5000 pyops

## Unit test python

python src/hello_test.py