#include <iostream>

using namespace std;

bool good(long long n, long long x, long long y, long long t)
{
	return (t/x) + (t/y) >= n;
}

int main()
{
	long long n;
	long long x;
	long long y;
	
	cin >> n;
	cin >> x;
	cin >> y;
	
	//Snachala ishem bistkiy skaner i bistro delaem kopiy
	//x - bistriy
	if (x > y)
	{
		swap(x, y);
	}
	
	long long l = 0;
	long long r = (n-1) * y;
	while (r - l > 1)
	{
		long long m = (l + r) / 2;
		if (good(n-1, x, y, m))
		{
			r = m;
		}
		else
		{
			l = m;
		}
	}
	
	cout << r + x;
}
