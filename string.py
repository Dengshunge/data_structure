#字符串模式匹配
def Index(S,T,pos=0):
   i = int(pos)
   j = 0
   Slen,Tlen = len(S),len(T)
   while i<Slen and j<Tlen:
       if S[i] == T[j]:
           i += 1
           j += 1
       else:
           i = i - j + 1#回到此次匹配的点并前进一个
           j = 0
       if j >= Tlen:
           return i - Tlen
       elif j == 0 and ((Slen-i) < Tlen):
           return None

#KMP模式匹配
def get_next(s,next):
    #next数组表示失配位之前最大的公共前后缀
    i = 0
    j = -1
    next[0] = -1
    while i< (len(s)-1):
        if j == -1 or s[i] == s[j]:#当j越界或者两个字符相等的时候，前移一个，并更新next数组
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]#当两个字符不相等时，选择j前的最大公共前缀，用其对应的字符与a[i]比较。

def get_nextval(s,next):
    #此时的next应该是“优化相同真前后缀”，是为了防止跳转后，字符串相同，做多余的比较。
    i = 0
    j = -1
    next[0] = -1
    while i< (len(s)-1):
        if j == -1 or s[i] == s[j]:
            i += 1
            j += 1
            if s[i] != s[j]:#当两位不相等的时候，像以前一样幅值
                next[i] = j
            else:#当两位相等的时候，跳转到更前的地方。
                next[i] = next[j]
        else:
            j = next[j]

#s1为主串，s2位子串，pos表示从第pos位开始搜索
def KMP(s1,s2,pos=0):
    i = int(pos)#表示s1从第pos位开始搜索
    j = 0#表示s2从第0位开始搜索
    next_ = [0] * len(s2)
    get_next(s2,next_)#获取next数组
    s1len = len(s1) ; s2len = len(s2)
    while i < s1len and j < s2len:
        if j == -1 or s1[i] == s2[j]:#j==-1说明主串和子串在该为不匹配，所以前移。而s1[i] == s2[j]说明在该位相等
            i += 1
            j += 1
        else:
            j = next_[j]
    if j == s2len:#只有当s1未循环完，s2=s2len时，才说明成功匹配上
        return i - j
    else:
        return None

#s1为主串，s2位子串，pos表示从第pos位开始搜索
def KMP_optimization(s1,s2,pos=0):
    i = int(pos)#表示s1从第pos位开始搜索
    j = 0#表示s2从第0位开始搜索
    next_ = [0] * len(s2)
    get_nextval(s2,next_)#获取next数组
    s1len = len(s1) ; s2len = len(s2)
    while i < s1len and j < s2len:
        if j == -1 or s1[i] == s2[j]:#j==-1说明主串和子串在该为不匹配，所以前移。而s1[i] == s2[j]说明在该位相等
            i += 1
            j += 1
        else:
            j = next_[j]
    if j == s2len:#只有当s1未循环完，s2=s2len时，才说明成功匹配上
        return i - j
    else:
        return None


if __name__ == '__main__':
    import time
    s1 = 'aaaaaaab'
    s2 = 'aab'
    start = time.time()
    for i in range(100000):
        Index(s1,s2)
    end = time.time()
    print('朴素匹配：',end-start)
    start = time.time()
    for i in range(100000):
        KMP(s1,s2)
    end = time.time()
    print('KMP:',end-start)
    start = time.time()
    for i in range(100000):
        KMP_optimization(s1,s2)
    end = time.time()
    print('KMP_optimization:',end - start)

