## Inverted Index using Trie data structure.

This project is an implementation of inverted index using a trie data-structure, which is an **in-memory** data-structure.

The trie was implemented in **C++** and is used in Python via **pybind11**.

*Tested in python3.6 and gnu-gcc7.4.0*

### How to run

clone and open terminal in repository
create a virtual environment in *python3.6*

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

compile *pytrie.cpp*

    bash compile.sh

run *app.py*

    python app.py

### How to test

index a *.txt* or *.pdf* file

    curl -X POST -F 'file=@/path/to/file_1.txt' http://<ip_address>/index

do a word search, returns a json object

    curl -X GET -d 'query=lorem' -G http://<ip_address>/word_search


do a prefix search, returns a json object

    curl -X GET -d 'query=lorem' -G http://<ip_address>/prefix_search

clear the index

    curl -X GET http://<ip_address>/clear

These endpoints were also tested with [Postman](https://www.getpostman.com/). Therefore, alternatively, these endpoints can be called via [Postman](https://www.getpostman.com/) too.
