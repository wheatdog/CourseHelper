#include <algorithm>
#include <string>
using namespace std;

class course
{
public:
	course();
	~course();
	string sched;
};

bool cmp()
{
	return ;
}

void group(course*)
{
	sort(course, course + 0, cmp);
}