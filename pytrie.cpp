#include <bits/stdc++.h>
#include <trie.cpp>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
namespace py = pybind11;

PYBIND11_MODULE(pytrie, m)
{
    py::class_<trie>(m, "trie")
        .def(py::init<>())
        .def("insert", &trie::insert)
        .def("search_word", &trie::search_word)
        .def("get_by_prefix", &trie::get_by_prefix);
}

int main()
{
    vector<string> arr = {
        "siddhant",
        "kushwaha",
        "joker",
        "bale",
        "batman",
        "christian",
    };

    trie inv_idx;

    // insert words from arr to inv_idx
    for (string &word : arr)
        inv_idx.insert(word, "doc_1", 1);

    // return words matching the prefix
    for (auto res : inv_idx.get_by_prefix("ba"))
        cout << res.first << '\n';
}