#include "bits/stdc++.h"
using namespace std;

typedef set<pair<string, int>> doc_set;

class trie {
   private:
    static const int CHAR_SIZE = 256;

    struct node {
        int count;
        bool is_leaf;
        doc_set docs;

        node *children[CHAR_SIZE];
        node(int count) {
            this->count = count;
            is_leaf = false;
            for (int i = 0; i < CHAR_SIZE; i++) children[i] = nullptr;
        }
    };

    node *root = nullptr;

    /* return all phrases from a given point */
    void dfs(node *ptr, string &path, vector<pair<string, doc_set>> &results) {
        if (ptr == nullptr)
            return;

        if (ptr->is_leaf)
            results.push_back(make_pair(path, ptr->docs));

        for (int i = 0; i < CHAR_SIZE; i++)
            if (ptr->children[i] != nullptr) {
                path.push_back(i);
                dfs(ptr->children[i], path, results);
                path.pop_back();
            }
    }

    /* return node pointing to last character of the prefix, return nullptr if prefix doesn't exist */
    node *search_prefix(const string &word) {
        int len = word.length();
        node *pCrawl = root;
        for (int level = 0; level < len; level++) {
            int index = word[level];
            if (!pCrawl->children[index])
                return nullptr;
            pCrawl = pCrawl->children[index];
        }
        return pCrawl;
    }

   public:
    trie() {
        root = new node(-1);
    }

    /*insert a phrase to trie */
    void insert(const string &word, const string &doc_id, int const &count) {
        int len = word.length();
        node *pCrawl = root;
        for (int level = 0; level < len; level++) {
            int index = word[level];
            if (!pCrawl->children[index])
                pCrawl->children[index] = new node(1);
            else
                (pCrawl->children[index]->count)++;
            pCrawl = pCrawl->children[index];
        }
        pCrawl->docs.insert(make_pair(doc_id, count));
        pCrawl->is_leaf = true;
    }

    /* exact word search */
    doc_set search_word(const string &word) {
        int len = word.length();
        node *pCrawl = root;
        for (int level = 0; level < len; level++) {
            int index = word[level];
            if (!pCrawl->children[index])
                return {};
            pCrawl = pCrawl->children[index];
        }
        return pCrawl->docs;
    }

    /* returns all phrases matching prefix */
    vector<pair<string, doc_set>> get_by_prefix(const string &word) {
        node *ptr = search_prefix(word);
        string path = "";
        vector<pair<string, doc_set>> results;
        dfs(ptr, path, results);
        for (int i = 0; i < results.size(); i++)
            results[i].first = word + results[i].first;
        return results;
    }
};