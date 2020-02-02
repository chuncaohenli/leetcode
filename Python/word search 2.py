class Solution:
    def findWords(self, board, words):
        trie = {}
        for word in words:
            tmp = trie
            for c in word:
                if c not in tmp:
                    tmp[c] = {'visited': False}
                tmp = tmp[c]
            tmp['word'] = word

        visited = {}

        def dfs(i, j, trie):
            if board[i][j] in trie and visited.get((i, j), False) == False:
                if 'word' in trie[board[i][j]]:
                    res.append(trie[board[i][j]]['word'])
                cur = board[i][j]
                board[i][j] = '#'
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N:
                        dfs(ni, nj, trie[cur])
                board[i][j] = cur
                visited[(i, j)] = True

        if not board or not board[0]:
            return []
        M, N = len(board), len(board[0])
        res = []
        for i in range(M):
            for j in range(N):
                if i == 1 and j == 3:
                    print(1)
                dfs(i, j, trie)

        return list(set(res))

s = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(s.findWords(board, words))