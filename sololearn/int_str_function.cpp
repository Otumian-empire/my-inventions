#include <iostream>
using namespace std;

int Addition(int j)
{
    return 2 + j + j;
}

string Name(string name)
{
    return "my name is " + name;
}

int main()
{    
    cout << Addition(7) << endl;
    cout << Name("michael") << endl;;
    
    return 0;
}
