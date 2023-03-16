class Solution:
    def maxArea(self, height: List[int]) -> int:

        """ two pointers approach
        
        their indices represents the x-axis in the graph
        the number represents the height
        
        -> find the biggest container (greatest heigh and distance from another)
        -get the greatest hight and compare to the next heights until find the greatest one 
        - it has to compare the smallest hight between them because its a container.
        - area = hight * length -> hight:minimum height, length: right indice - left indice


        initialize l and right pointers
        initialize max_area int

        while l smaller or equal to right
            if new area is > previous area
                update the area 
            #change the pointers, if the right hight is greater, left shift one, same with the other size if it's the greater
        at the end return max_area        
        """

        L = 0
        R = len(height) - 1
        max_area = 0

        #height: min hight between R,L, lenght: R - L
        while L <= R:
            if (min(height[L], height[R]) * (R - L)) > max_area:
                max_area = min(height[L], height[R]) * (R - L)
            #update pointers
            if height[R] > height[L]:
                L += 1
            else:
                R -= 1
        return max_area
