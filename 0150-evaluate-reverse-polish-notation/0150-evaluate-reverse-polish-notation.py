class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "/*+-":
                r = int(stack.pop())
                l = int(stack.pop())
                
                match(t):
                    case("/"):
                        total = l / r
                        # if total < 0:
                        #     total = 0
                        print("Performing operation ", l  ," // " , r)
                    case("*"):
                        total = l * r
                        print("Performing operation ", l , " * ", r)
                    case("+"):
                        total = l + r
                        print("Performing operation ", l , " + ",  r)
                    case("-"):
                        total = l - r
                        print("Performing operation ", l , " - ",  r)
                
                stack.append(int(total))

            else:
                stack.append(t)
        
        return int(stack.pop())

        