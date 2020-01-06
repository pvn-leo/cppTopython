#include <iostream>
using namespace std;

void main()
{    
    float n1, n2, n3=0.0;
    cout<<"Enter three numbers: ";
    cin>>n1>>n2>>n3;
    if(n1 >= n2 && n1 >= n3)
    {
        cout<<"Largest number: "<<n1;
    }

    if(n2 >= n1 && n2 >= n3)
    {
        cout<<"Largest number: "<<n2;
    }

    if(n3 >= n1 && n3 >= n2) 
{
        cout<<"Largest number: "<<n3;
    }

  
}