#include <iostream>
#include <vector>

using namespace std;

bool good(vector<int> arr, int n, int k, int r)
{
	int count_cows = 1;
	int last_box = arr[0];
	for(int i=1; i<n; i++)
	{
		int box = arr[i];
		if (box - last_box >= r)
		{
			last_box = box;
			count_cows += 1;
		}
	}
	return count_cows >= k;
}


int main()
{
	vector<int> arr;
	int n;
	int k;
	int coord;
	
	cin >> n;
	cin >> k;

	
	while (cin >> coord)
	{
		arr.push_back(coord);
		if (cin.peek() == '\n')
		{
			break;
		}
	}
	
	
	int l = 0;
	int r = arr[n-1] - arr[0] + 1;
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
