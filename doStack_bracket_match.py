#学习栈的用法
#括号匹配
#括号匹配思路： 当遇到左括号的时候就进栈，当遇到右括号，就调用栈顶元素看是否匹配。
#如果匹配了就把这个元素出栈，因为下一个元素要来了。 不匹配就直接报错。最后需要验证下栈是否为空栈
#空栈才表示正确
class Stack(object):
    def __init__(self,limit):
        self.stack = []
        self.limit = limit

    def push(self,data):
        if len(self.stack) >= self.limit:
            raise IndexError('超出限制')
        else:
            self.stack.append(data)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('空栈')
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError('空栈')
    
    def is_empty(self):
        return not bool(self.stack)

def balanced_parentheses(parentheses):
    """
    括号匹配的核心思想
    遇到左括号 入栈
    遇到右括号，看顶端元素，一样出栈判断下一组，不一样报错。遇到右括号还要先判断是不是空栈
    最后判断是不是空栈
    """
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        else:
            if stack.is_empty():
                return False    #一来就是右括号
            else:
                left = stack.peek()
                if left == '(':
                    stack.pop()
                    continue
                else:
                    return False
    return stack.is_empty()

print(balanced_parentheses('()'))


        