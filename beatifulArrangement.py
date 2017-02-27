def helper(temp, start, end, k, res, used):
    if len(temp) == k:
	print(temp)
	res.append(temp)
        return

    for i in range(start, end+1):
        if i not in used or used[i] == 0:
            used[i] = 1
            temp.append(i)
            helper(temp, start+1, end, k, res, used)
            temp.pop()
            used[i] = 0



def combine(n, k):
    res = []
    helper([], 1, n, k, res, dict())
    return res





print(combine(4, 2))
