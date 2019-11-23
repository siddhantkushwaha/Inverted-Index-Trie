#include "bits/stdc++.h"
using namespace std;

class trie {
   private:
    static const int CHAR_SIZE = 256;

    struct node {
        int count;
        bool is_leaf;
        set<string> doc_ids;

        node *children[CHAR_SIZE];
        node(int count) {
            this->count = count;
            is_leaf = false;
            for (int i = 0; i < CHAR_SIZE; i++) children[i] = nullptr;
        }
    };

    node *root = nullptr;

    /* return all phrases from  a given point */
    void dfs(node *ptr, string &path, vector<pair<string, set<string>>> &results) {
        if (ptr == nullptr)
            return;

        if (ptr->is_leaf)
            results.push_back(make_pair(path, ptr->doc_ids));

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
    void insert(const string &word, const string &doc_id) {
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
        pCrawl->doc_ids.insert(doc_id);
        pCrawl->is_leaf = true;
    }

    /* exact word search */
    set<string> search_word(const string &word) {
        int len = word.length();
        node *pCrawl = root;
        for (int level = 0; level < len; level++) {
            int index = word[level];
            if (!pCrawl->children[index])
                return {};
            pCrawl = pCrawl->children[index];
        }
        return pCrawl->doc_ids;
    }

    /* returns all phrases matching prefix */
    vector<pair<string, set<string>>> get_by_prefix(const string &word) {
        node *ptr = search_prefix(word);
        string path = "";
        vector<pair<string, set<string>>> results;
        dfs(ptr, path, results);
        for (int i = 0; i < results.size(); i++)
            results[i].first = word + results[i].first;
        return results;
    }
};