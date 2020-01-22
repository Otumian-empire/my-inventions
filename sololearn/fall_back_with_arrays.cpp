#include <iostream>
using namespace std;

int main() {

/*
i intend to calculate the sum of integers in the array
look at the following inputs and their out comes*/


//here is an array
//try to change them and
//explain the outcome

int b[] ={1,2,3,4,5}; //sum = 15
/*
int b[] ={1,2,3,4,}; //sum = 10
int b[] ={1,2,3,4}; //sum = 9, why 9.. and not 10
*/
//so comment the others and cross check the output, please..

int sum = 0;
for(int x = 0; x < 5; x++)
{
    sum += b[x];
}

cout << sum << endl;

    return 0;
}

