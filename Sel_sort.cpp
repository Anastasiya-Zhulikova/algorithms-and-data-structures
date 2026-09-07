//Сортировка выбором - ищется МАКСИМУМ (по заданию), вставляется в начало, сдвигается от начала на 1

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
		
		//Ищем МАКСИМУМ
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
			//Поменяли с началом отсчёта
			swap(arr[i], arr[ind]);
		}
	}
}


int main()
{
	//Ввод массива
	vector<int> arr;
    int number;
    int n = 0;

    //Вводим числа по очереди
    while (cin >> number) 
    {	
    	n++;
        arr.push_back(number); //Число в конец массива
        
        //Если нажать Enter, то останавливаем ввод
        if (cin.peek() == '\n') 
        {
            break; 
        }
    }
    
    //Сортировка
    selection_sort(arr, n);
    
    //Вывод массива
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
