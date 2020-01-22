/*
searching algo, given the list, it's length and what item to find from the list
*/
#include <iostream>
using namespace std;

int seqsearch(int mylist[], int mylistlen, int item);

int main() {
	
	int xlist[] = {2, 4, 67, 99, 120, -23};
	int lenxlist = 6;
	cout << seqsearch(xlist, lenxlist, 67)  << endl;
	cout << seqsearch(xlist, lenxlist, -23)  << endl;
	cout << seqsearch(xlist, lenxlist, 99)  << endl;
	cout << seqsearch(xlist, lenxlist, 6)  << endl;
	
	return 0;
}

int seqsearch(int mylist[], int mylistlen, int item) {
	
	int loc = 0;

	while (loc < mylistlen) {
		if (mylist[loc] == item) {
			cout << item << " found" << endl;
			return loc;
		} else {
			++loc;
		}
	}

	cout << item << " not found" << endl;

	return -1;
}

