class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        write = 0
        while i < len(chars):
            ch = chars[i]
            count = 0
            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1
            chars[write] = ch
            write += 1
            if count > 1:
                for x in str(count):
                    chars[write] = x
                    write += 1
        return write 