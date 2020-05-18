class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 边界情况
        if path == "" or path[0] != "/":
            return ""

        res = []
        path = [p for p in path.split("/") if p]

        for p in path:
            if p == ".":
                continue
            elif p == "..":
                if res == []:
                    continue
                else:
                    res.pop()
            else:
                res.append(p)

        res = "/" + "/".join(res)

        return res

if __name__ == '__main__':
    path = "/a/./b/../../c/"
    res = Solution().simplifyPath(path)
    print(res)
