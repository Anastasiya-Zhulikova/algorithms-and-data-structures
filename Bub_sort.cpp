//Сравнивают два соседник, так n-1 раз, потом n - i - 1

#include <iostream>
#include <vector>

using namespace std;

void bubble_sort(vector<int>&arr, int n)
{
	for (int i=0; i<(n-1); i++)
	{
		bool swapped = false;
		
		for (int j=0; j<(n-i-1); j++)
		{
			if (arr[j] < arr[j + 1])
			{
				swap(arr[j], arr[j+1]);
				swapped = true;
			}
		}
		
		if (not swapped)
		{
			break;
		}
	}
}


int main()
{
	vector<int> arr;
	int n = 0;
	int number;
	
	while (cin >> number)
	{
		n++;
		arr.push_back(number);
		if (cin.peek() == '\n')
		{
			break;
		}
	}
	
	bubble_sort(arr, n);
	
	for (int i=0; i<n; i++)
	{
		if (i!=0)
		{
			cout << " ";
		}
		cout << arr[i];
	}
	
	return 0;
}
