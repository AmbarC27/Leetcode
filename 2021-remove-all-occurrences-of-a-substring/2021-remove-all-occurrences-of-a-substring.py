class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_list = []
        for char in part:
            part_list.append(char)
        for char in s:
            stack.append(char)
            if len(stack) >= len(part_list) and stack[-len(part_list):] == part_list:
                for _ in range(len(part_list)):
                    stack.pop()
        return "".join(stack)

