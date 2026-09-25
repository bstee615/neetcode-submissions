from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # looked up the answer: topo sort.
        # if we made a graph of the dependencies, we would be able to take nodes one-by-one off the graph (zero prereqs).
        num_prereqs = defaultdict(int)
        dependents = defaultdict(set)
        for p, q in prerequisites:
            dependents[q].add(p)
            num_prereqs[p] += 1
            if p == q:
                return False
        for i in range(numCourses):
            if i not in num_prereqs:
                num_prereqs[i] = 0
        # process all nodes with no prerequisites first. Keep processing nodes with no prerequisites until we consume the whole tree
        queue = deque([n for n, c in num_prereqs.items() if c == 0])
        consumed = 0
        while queue:
            n = queue.popleft()
            c = num_prereqs[n]
            consumed += 1
            # get all ones depending on this one and remove the connection
            # if that leaves zero, process that next
            to_queue = set()
            for p in dependents[n]:
                num_prereqs[p] -= 1
                if num_prereqs[p] == 0:
                    to_queue.add(p)
            queue.extend(to_queue)
        return consumed == numCourses
