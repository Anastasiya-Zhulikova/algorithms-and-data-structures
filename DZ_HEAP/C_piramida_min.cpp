#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Heap
{	
	public:
		vector<int> heap = {0};
		int size = 0;
		
		void clear()
		{
			heap = {0};
			size = 0;
		}
		
		
		void shiftUp(int i)
		{
			while (i/2 > 0 && heap[i] < heap[i/2])
			{
				swap(heap[i], heap[i/2]);
				i = i/2;
			}
		}
		
		void add(int el)
		{
			heap.push_back(el);
			size += 1;
			shiftUp(size);
		}
		
		int indMinChild(int i)
		{
			if (2*i+1 > size)
			{
				return 2*i;
			}
			if (heap[2*i] < heap[2*i+1])
			{
				return 2*i;
			}
			return 2*i+1;
		}
		
		void shiftDown(int i)
		{
			while (2*i <= size)
			{
				int j = indMinChild(i);
				if (heap[i] > heap[j])
				{
					swap(heap[i], heap[j]);
					i = j;
				}
				else
				{
					break;
				}
			}
		}
		
		int extract()
		{	
			int removed = heap[1];
			heap[1] = heap[size];
			heap.pop_back();
			size -= 1;
			shiftDown(1);
			return removed;
		}
	
};

int main()
{
	Heap heap;
	string command;
	int el;
	
	while (cin >> command)
	{
		if (command == "CLEAR")
		{
			heap.clear();
		}
		if (command == "ADD")
		{
			cin >> el;
			heap.add(el);
		}
		if (command == "EXTRACT")
		{
			if (heap.size == 0)
			{
				cout << "CANNOT" << endl;
			}
			else
			{
				cout << heap.extract() << endl;
			}
		}
	}
	
	return 0;
}
