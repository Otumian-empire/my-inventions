#include <iostream>
using namespace std;

int Addition(int j)
{
    int k;
    k=2+j;
    return k + j;
}

string Name(string name)
{
    return "my name is "<<name<<endl;
}

int main()
{    
    cout <<Addition(7);
    cout<<Name("michael");
    
    return 0;
}
