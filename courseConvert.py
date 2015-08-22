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

	def timeToInt(self):
		week = ["一","二","三","四","五","六"]
		order = ["A", "B", "C", "D"]
		index = []
		for day in week:
			if day in self.c_time:
				index.append(self.c_time.index(day))
		index.append(len(self.c_time)+1)
		for i in range(len(index)-1):
			temp = self.c_time[index[i]+1: index[i+1]]
			for j in temp.strip().split(","):
				if j.isdecimal():
					self.int_time.append(week.index(self.c_time[index[i]])*15 + int(j) + 1)
				elif j in order:
					self.int_time.append(week.index(self.c_time[index[i]])*15 + order.index(j) + 12)

class schedule:
	def __init__(self):
		self.schedule_list = [0]*90

		# pre-disabled class
		# 0th class and night class
		for i in range(6):
			self.schedule_list[15*i] = 1
			for j in range(4):
				self.schedule_list[15*i+j+11] = 1

		# SAT
		for i in range(15):
			self.schedule_list[75+i] = 1

	schedule_list = []
	class_list = []
	course_list = []

	def filter(self):
		temp_list = []
		must_list = []

		for i in range(len(self.schedule_list)):
			if self.schedule_list[i] == 2:
				must_list.append(i)

		#filter A1~8
		for aClass in self.course_list:
			if aClass.c_type != "0":
				temp_list.append(aClass)




		# remove the one not in must_list
		indexToRemove = []
		new_list = []
		for i in range(len(temp_list)):
			for j in must_list:
				if j not in temp_list[i].int_time:
					indexToRemove.append(i)
		for i in range(len(temp_list)):
			if i not in indexToRemove:
				new_list.append(temp_list[i])
		temp_list = new_list
		indexToRemove = []
		new_list = []

		# remove unwanted
		for i in range(len(temp_list)):
			for aTime in temp_list[i].int_time:
				if self.schedule_list[aTime] == 1:
					indexToRemove.append(i)
		for i in range(len(temp_list)):
			if i not in indexToRemove:
				new_list.append(temp_list[i])
		temp_list = new_list

		return temp_list




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
	out = out.replace(" ", "")
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





aSchedule = schedule()

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
	aSchedule.course_list.append(course(data[i], data[i+4], data[i+1], convertTime(data[i+11]), convertType(data[i+14])))
	# print(data[i])
	i += 15
for c in aSchedule.course_list:
	c.timeToInt()

# output = codecs.open("output.txt", "w", "utf-8")
# for c in course_list:
# 	c.timeToInt()
# 	output.write(c.c_no + " " + c.c_dep + " " + str(len(c.int_time)) + " " + " ".join(str(x) for x in c.int_time) + " " + c.c_type + "\n")

#test filter
aSchedule.schedule_list[35] = 2
for ob in aSchedule.filter():
	print(ob.c_no)
	print(ob.c_time)
	print(ob.c_type)

# aSchedule.schedule_list[35] = 2
# aSchedule.filter()
# for i in range(6):
# 	print(aSchedule.schedule_list[15*i: 15*i+15])






