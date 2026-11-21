class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)

        for i in range(1,n):
            adj[parent[i]].append(i)

        resultSize = [1] * n 
        lastChar = [-1] * 26

        def dfs(currnode):
            c = ord(s[currnode]) - ord('a')
            nearestAncestor = lastChar[c]
            lastChar[c] = currnode

            for nei in adj[currnode]:
                dfs(nei)

            lastChar[c] = nearestAncestor
            
            if currnode != 0:
                newParent = parent[currnode]
                if nearestAncestor != -1:
                    newParent = nearestAncestor
                
                parent[currnode] = newParent
                resultSize[newParent] += resultSize[currnode]

        dfs(0)
        return resultSize
        
