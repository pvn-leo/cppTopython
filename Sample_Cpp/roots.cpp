#include <iostream>
#include <math.h>
using namespace std;
void main() 
{
    float a,b,c,x1,x2,discriminant,realPart,imaginaryPart=0.0;
    cout<<"Enter coefficients a, b and c: ";
    cin>>a>>b>>c;
    discriminant = b*b - 4*a*c;
    if(discriminant > 0) 
{
        x1 = (-b + pow((discriminant),0.5)) / (2*a);
        x2 = (-b - pow((discriminant),0.5)) / (2*a);
        cout<<"Roots are real and different."<<'\n';
        cout<<"x1 ="<<x1<<'\n';
        cout<<"x2 = "<<x2<<'\n';
    }   
    else if(discriminant == 0) 
{
        cout<<"Roots are real and same."<<'\n';
        x1 = (-b + pow((discriminant),0.5)) / (2*a);
        cout<<"x1 = x2 ="<<x1<<'\n';
    }
    else 
{
        realPart = -b/(2*a);
        imaginaryPart =pow((discriminant),0.5)/(2*a);
        cout<<"Roots are complex and different." <<'\n';
        cout<<"x1 = "<<realPart<<"+"<<imaginaryPart<<"i"<<'\n';
        cout<<"x2 = "<<realPart<<"-"<<imaginaryPart<<"i"<<'\n';
    }
}