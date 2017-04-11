class Request:

	def __init__(self, start, finish, value):
		self.start = start
		self.finish = finish
		self.value = value

def getP(requests):
	pValues = []
	for i in range(0, len(requests)):
		if(i == 0):
			pValues.append(0)
		elif(i > 0):
			for j in range(i - 1, -1, -1):
				if(requests[j].finish <= requests[i].start):
					pValues.append(j+1)
					break
				elif(j == 0 and requests[j].finish > requests[i].start):
					pValues.append(0)
					break
				else:
					continue
		else:
			continue
	return pValues

requests = []
a = Request(1, 3, 2)
b = Request(5, 7, 1)
c = Request(2, 10, 4)
d = Request(9, 15, 1)
e = Request(12, 15, 24)
f = Request(7, 17, 15)
g = Request(13, 26, 3)

requests.append(a)
requests.append(b)
requests.append(c)
requests.append(d)
requests.append(e)
requests.append(f)
requests.append(g)

print(getP(requests))