
def solution(s1, s2):
	s1 = [char for char in s1]
	s2 = [char for char in s2]
	total = 0
	for x in s1:
		if x in s2:
			s2.remove(x)
			total += 1
	print(s1,s2)
	return total

result = solution("aaa", "a")

print(result)





