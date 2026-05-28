class Solution(object):
  def carFleet(self,target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)
    stack = []
    for p, s in cars:
        time = (target - p*1.0) / s
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)

b=Solution()
target=10
position=[6,7,8]
speed=[2,3,4]
b.carFleet(target,position,speed)