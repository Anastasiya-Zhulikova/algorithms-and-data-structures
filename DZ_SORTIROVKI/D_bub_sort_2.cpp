#include <iostream>
#include <vector>

using namespace std;


int bubble_sort_count(int arr[], int n)
{
	int count_swapped = 0;
	for (int i=0; i<(n-1); i++)
	{
		bool swapped = false;
		for (int j=0; j<(n-i-1); j++)
		{
			if (arr[j] > arr[j+1])
			{
				swap(arr[j], arr[j+1]);
				count_swapped++;
				swapped = true;
			}
		}
		if (not swapped)
		{
			break;
		}	
	}
	
	return count_swapped;
}

int main()
{
	int n;
	cin >> n;
	int arr[n];
	
	for (int i=0; i<n; i++)
	{
		cin >> arr[i];
	}
	
	cout << bubble_sort_count(arr, n);
	
	return 0;
}
