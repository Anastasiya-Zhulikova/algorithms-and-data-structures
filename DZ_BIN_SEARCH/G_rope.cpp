#include <iostream>
#include <vector>

using namespace std;

bool good(vector<int>& arr, int n, int k, int m)
{
	int cnt = 0;
	
	if (m == 0)
	{
		return true;
	}
	
	for(int i=0; i<n; i++)
	{
		cnt += int(arr[i] / m);
	}
	return cnt >= k;
}


int main()
{
	vector<int> arr;
	int n;
	int k;
	int len;
	
	cin >> n;
	cin >> k;

	
	for (int i = 0; i < n; i++)
	{
	    cin >> len;
	    arr.push_back(len);
	}

	
	
	int mx = 0;
	for (int i=0; i<n; i++)
	{
		if (arr[i] > mx)
		{
			mx = arr[i];
		}
	}
	
	int l = 0;
	int r = mx+1;
	
	
	while (r - l > 1)
	{
		int m = (l + r) / 2;
		if (good(arr, n, k, m))
		{
			l = m;
		}
		else
		{
			r = m;
		}
	}
	
	cout << l;
}
