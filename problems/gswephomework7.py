# 1) You have a stack of n boxes, with widths w;, heights h,, and depths d, 
# The boxes cannot be rotated and can only be stacked on top of one another 
# if each box in the stack is strictly larger than the box above it in width, 
# height, and depth. Implement a method to compute the height of the tallest 
# possible stack. The height of a stack is the sum of the heights of each box. 
 
class Box:
	def __init__(self, w, h, d):
		self.w = w
		self.h = h
		self.d = d
	
def getNextBox(boxes, n):
    n_w = boxes[n].w
    n_h = boxes[n].h
    n_d = boxes[n].d
    for i in range(n - 1, -1, -1):
        if n_w > boxes[i].w and n_h > boxes[i].h and n_d > boxes[i].d:
            return i
    return -1  # there are none valid anymore

def stack(boxes, n, dp):
    if n == 0:
        return boxes[0].h
    if n == -1:
        return 0
    if n in dp:
        return dp[n]
    
    option1 = stack(boxes, n - 1, dp) # without
    
    next_box_index = getNextBox(boxes, n) # with
    option2 = stack(boxes, next_box_index, dp) + boxes[n].h
    
    dp[n] = max(option1, option2)
    return dp[n]

def tallest_stack(boxes):
    boxes = sorted(boxes, key=lambda x: (x.w, x.h, x.d))
    dp = {}
    return stack(boxes, len(boxes) - 1, dp)

boxes = [Box(5, 4, 10), Box(3, 3, 10), Box(2, 3, 1), Box(1, 2, 1)]
print(tallest_stack(boxes))

#2) Given a circular linked list, implement an algorithm that returns the node 
# at the beginning of the loop. A circular linked list is a corrupt linked list
# in which one node's next pointer points to an earlier node, so as to make a loop.

   