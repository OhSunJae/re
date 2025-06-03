from collections import deque

def printer_queue(priorities, location):
    queue = deque([(i, p) for i , p in enumerate(priorities)])
    count = 0
    
    while queue:
        cur = queue.popleft()
        if any(cur[1] < other[1] for other in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[0] == location:
                return count