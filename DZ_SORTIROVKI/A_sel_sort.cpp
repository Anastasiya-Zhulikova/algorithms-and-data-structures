#include <iostream>
#include <vector>

using namespace std;

void selection_sort(vector<int>& arr, int n)
{
    
    for (int i=0; i<(n-1); i++)
	{
		int mx;
		mx = arr[i];
		int ind;
		ind = i;
		
		for (int j=i+1; j<n; j++)
		{
			if (arr[j] > mx)
			{
				mx = arr[j];
				ind = j;
			}
		}
		
		if (i != ind)
		{
			swap(arr[i], arr[ind]);
		}
	}
}


int main()
{
	vector<int> arr;
    int number;
    int n = 0;

    while (cin >> number) 
    {	
    	n++;
        arr.push_back(number);
        
        if (cin.peek() == '\n') 
        {
            break; 
        }
    }
    
    selection_sort(arr, n);
    
    for (int i=0; i < n; i++)
    {
    	if (i != 0)
    	{
    		cout << " ";
		}
        cout << arr[i];
    }

    return 0;
}
