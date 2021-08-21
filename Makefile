all: clean build

clean:
	rm -fr dist/
	rm -rf pyspark_starter.zip
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.ipynb_checkpoints' -exec rm -f {} +
	find . -name 'coverage.xml' -exec rm -f {} +
	find . -name '.coverage' -exec rm -f {} +

build:
	mkdir ./dist/
	cp ./src/main.py ./dist/
	cd ./src && zip -x main.py -r ../dist/jobs.zip .