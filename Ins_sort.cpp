//Сортировка вставкой - "готовая" часть и "входная". Берется первый элемент входной части, сравнивается с предыдущим. если что - меняются местами

#include <iostream>
#include <vector>


using namespace std;

void insertion_sort(vector<int>& arr, int n)
{
	for (int i=1; i<n; i++)
	{
		int key = arr[i];
		int ind = i;
		while (ind > 0 and arr[ind-1] > key)
		{
			arr[ind] = arr[ind-1];
			ind = ind - 1;	
		}
		
		arr[ind] = key;
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
	
	
	insertion_sort(arr, n);

	for (int i=0; i<n; i++)
	{
		if (i != 0)
		{
			cout << " ";
		}
		cout << arr[i];
	}
	
	return 0;
}
