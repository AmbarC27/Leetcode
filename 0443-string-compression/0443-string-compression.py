class Solution:
    def compress(self, chars: List[str]) -> int:
        idx_of_insertion = 0
        last_char = chars[0]
        consec_length = 1
        for i in range(1,len(chars)):
            if chars[i] == last_char:
                consec_length += 1
            else:
                if consec_length == 1:
                    string_to_insert = last_char
                else:
                    string_to_insert = last_char + str(consec_length)
                for j in range(len(string_to_insert)):
                    chars[idx_of_insertion] = string_to_insert[j]
                    idx_of_insertion += 1
                ## reset
                last_char = chars[i]
                consec_length = 1
        if consec_length == 1:
            string_to_insert = last_char
        else:
            string_to_insert = last_char + str(consec_length)
        for j in range(len(string_to_insert)):
            chars[idx_of_insertion] = string_to_insert[j]
            idx_of_insertion += 1
        return idx_of_insertion