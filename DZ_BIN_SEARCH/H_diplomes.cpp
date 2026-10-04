#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;

bool good(long long n, long long w, long long h, long long x)
{
	return (x/w) * (x/h) >= n;
}

int main()
{
	long long w;
	long long h;
	long long n;
	
	cin >> w;
	cin >> h;
	cin >> n;
	
	long long l = 0;
	long long r = n * max(w, h);
	while (r - l > 1)
	{
		long long m = (l + r) / 2;
		if (good(n, w, h, m))
		{
			r = m;
		}
		else
		{
			l = m;
		}
	}
	
	cout << r;
}
