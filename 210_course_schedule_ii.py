# 210. Course Schedule II
#
# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs,
# return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them.
# If it is impossible to finish all courses, return an empty array.
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So the correct course order is [0,1]
#
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take.
# To take course 3 you should have finished both courses 1 and 2.
# Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
#
# Note:
# The input prerequisites is a graph represented by a list of edges,
# not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# click to show more hints.
#
# Hints:
# This problem is equivalent to finding the topological order in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera
# explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.


class Solution(object):
    # BFS
    def findOrder(self, numCourses, prerequisites):
        """
        http://bookshadow.com/weblog/2015/05/14/leetcode-course-schedule-ii/

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degrees = [0] * numCourses
        children = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            degrees[pair[0]] += 1
            children[pair[1]].append(pair[0])
        courses = set(range(numCourses))
        flag = True
        ans = []
        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if degrees[x] == 0:
                    for child in children[x]:
                        degrees[child] -= 1
                    removeList.append(x)
                    flag = True
            for x in removeList:
                ans.append(x)
                courses.remove(x)
        return [[], ans][len(courses) == 0]

    # DFS
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        # 0 == unknown, 1 == visiting, 2 == visited
        v = [0] * numCourses
        ans = []
        for i in range(numCourses):
            if self.dfs(i, v, graph, ans):
                return []
        ans.reverse()
        return ans

    def dfs(self, cur, v, graph, ans):
        if v[cur] == 1:
            return True
        if v[cur] == 2:
            return False
        v[cur] = 1

        for t in graph[cur]:
            if self.dfs(t, v, graph, ans):
                return True
        v[cur] = 2
        # ans.insert(0, cur)
        ans.append(cur)

        return False

if __name__ == '__main__':
    print Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print Solution().findOrder(2, [[1, 0], [0, 1]])
