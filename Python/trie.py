words = ["ab","ba","aaab","abab","baa"]

trie = {}

for w in words:
    tmp = trie
    for c in w:
        if c not in tmp:
            tmp[c] = {}
        tmp = tmp[c]
    tmp['word'] = True

def printTrie(trie, space):
    if not trie or type(trie) == type(True):
        return
    for k, v in trie.items():
        print(space, k)
        printTrie(v, space + '     ')

printTrie(trie, '')