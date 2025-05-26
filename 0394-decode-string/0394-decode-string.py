class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                decoded_string = ""
                # get the encoded string
                while stack and stack[-1] != '[':
                    decoded_string = stack.pop() + decoded_string
                # pop '[' from stack
                stack.pop()

                # get the number k (may be multiple digits)
                k = 0
                base = 1
                while stack and stack[-1].isdigit():
                    k = k + int(stack.pop()) * base
                    base *= 10

                # push the decoded string k times back onto the stack
                expanded = decoded_string * k
                for ch in expanded:
                    stack.append(ch)

            else:
                stack.append(char)

        return ''.join(stack)
