'''
In this problem, we have considered only one or two steps at a time

'''


class StairCase:
    def climbStairs(n):
        if n<=0:
            print("Enter valid stair number")
            return 0
        if n<=2 and n>0:
            return n
        steps = [0]*(n+1) #creating an empty list
        steps[2],steps[1] = 2,1 #number of steps needed to reach level 2 and 1 is two and respectively
        
        #here we have given condition with that person can take one or two step a time
        for i in range(3,n+1):
            steps[i] = steps[i-1]+steps[i-2]
        return steps[n]
        

if __name__ == "__main__":
    s = StairCase
    res = s.climbStairs(n=4)
    print(res)