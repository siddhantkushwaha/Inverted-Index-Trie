c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` pytrie.cpp -o pytrie`python3-config --extension-suffix`
