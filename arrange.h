#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>
using namespace std;

class course
{
public:
	course(int, string, int);
	~course();
	string sched;
	int number, group;
};

course::course(int num, string sch, int grp): number(num), sched(sch), group(grp)
{}
course::~course(){}

vector<course> v;
vector< vector<course> > divided;

bool cmp(const course& a, const course& b)
{
	return a.sched < b.sched;
}

void get()
{
	fstream file;
	file.open("course_time_type.txt", ios::in);
	stringstream ss;
	string str;

	while (getline(file, str))
	{
		ss.clear ();
		ss.str ("");
		ss << str;
		string sch;
		int num, grp;
		ss >> num >> sch >> grp;
		v.push_back(course(num, sch, grp));
	}

	file.close();
}

void divide()
{
	sort(v.begin(), v.end(), cmp);
	int count = 0;
	for(unsigned int i = 0; i < v.size(); ++i)
	{
		if(v[i].group == 1) ++count; 
	}
	cout << count << endl;
}