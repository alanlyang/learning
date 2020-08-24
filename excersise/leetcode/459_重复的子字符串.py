######################
# 给定一个非空滋肤疮，判断是否可以由它的一个子串重复多次构成
# 字符串只含有小写英文字母，且长度不超过10000
# 2020-08-24
########################

class Solution:
    def repeatedSubStringPattern1(self, s: str) -> bool:
        """
        设字符串长度为n , 子串长度为t,则有
        1、n为t的整数倍
        2、子串为原串的前缀
        3、原串某个位置的字符满足 s[i] = s[i - t]

        复杂度分析：
            时间 O(n*n): 枚举i 为 O(n), 遍历s为O(n)
            空间复杂度O(1): 仅使用了s i j 三个变量
        """

        n = len(s)
        
        for i in range(1, n//2 + 1):
            # 满足第二个条件
            if n % i == 0:
                if all(s[j] == s[j-i] for j in range(i, n)):
                    return True

        return False
    
    def answer2(self, s):
        """
        字符串匹配：
        利用s+s 去除头部和尾部字符后，s 必定为s+s的一个字串
        """
        return (s+s).find(s, 1) != len(s)

    def answer3(self, s):
        """
        kmp算法实现

        """
        def kmp(query, pattern):
            n ,m = len(query), len(pattern)
            # 初始化pmt数组
            fail = [-1] * m
            # 计算pmt数组
            for i in range(1, m):
                j = fail[i-1]
                while j != -1 and pattern[j+1] != pattern[i]:
                    j = fail[j]
                if pattern[j+1] == pattern[i]:
                    fail[i] = j+1
            
            print("fail: {}".format(fail))

            match = -1

            for i in range(1, n-1):
                while match != -1 and pattern[match+1] != query[i]:
                    match = fail[match]
                if pattern[match+1] == query[i]:
                    match += 1

                    if match == m-1:
                        return True
            return False
        
        return kmp(s+s, s)

        pass    



if __name__ == "__main__":
    soul = Solution()
    print(soul.answer3("abab"))


"""
kmp算法：（一种用于字符串查找的算法)
    kmp算法核心：部分匹配表(Partial Match Table)
        PMT中的value是字符串前缀集合与后缀集合的交集中最长元素的长度
        next数组为模式串自匹配上的长度
"""