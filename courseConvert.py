# coding=utf-8
import codecs

class course:
	def __init__(self, no, tit, de, ti, ty):
		self.c_no = no
		self.c_title = tit
		self.c_dep = de
		self.c_time = ti
		self.c_type = ty
		self.int_time = []
	def set(self, no, tit, de, ti, ty):
		self.c_no = no
		self.c_title = tit
		self.c_dep = de
		self.c_time = ti
		self.c_type = ty

def convertTime(c_time):
	if c_time == "":
		return "0"
	count = c_time.count("(")
	out = ""
	for i in range(count):
		if "(" in c_time:
			lindex = c_time.index("(")
			rindex = c_time.index(")")
			temp = c_time.partition(c_time[lindex: rindex+1])
			out += temp[0]
			c_time = temp[2]
	out.replace(" ", "")
	return out


def convertType(c_type):
	if "A" in c_type:
		index = c_type.index("A")
		if index+2 <= len(c_type):
			if c_type[index+1].isdecimal():
				if c_type[index+2].isdecimal():
					if index+4 <= len(c_type):
						if c_type[index+3].isdecimal():
							return "0"
					return c_type[index+1:index+3]
				else:
					return c_type[index+1]
	return "0"

def timeToInt(c_time):
	week = ["一","二","三","四","五","六"]
	order = ["A", "B", "C", "D"]
	index = []
	for day in week:
		if day in c_time:
			index.append(c_time.index(day))
	index.append(len(c_time)+1)
	for i in range(len(index)-1):
		temp = c_time[index[i]+1: index[i+1]]
		for j in temp.strip().split(","):
			if j.isdecimal():
				int_time.append(week.index(c_time[index[i]])*15 + int(j))
			else if j in order:
				int_time.append(week.index(c_time[index[i]])*15 + order.index(j) + 12)



course_list = []

# for line in codecs.open("course.txt", "r", "utf-8").readlines():
# 	data = line.split("#")
# 	course_list.append(course(data[0], data[4], data[9], convertTime(data[11]), convertType(data[14])))
# 	print(data[0])

rawData = codecs.open("course.txt", "r", "utf-8").read()
data = rawData.replace("\n", "").split("#")
i = 0
while i + 15 <= len(data):
	if data[i+1] == "":
		data[i+1] = "0"
	course_list.append(course(data[i], data[i+4], data[i+1], convertTime(data[i+11]), convertType(data[i+14])))
	print(data[i])
	i += 15

# output = codecs.open("output.txt", "w", "utf-8")
# for c in course_list:
# 	output.write(c.c_no + " " + c.c_dep + " " + c.c_time + " " + c.c_type + "\n")

for c in course_list:








