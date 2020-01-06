#include<iostream.h>
using namespace std;
float add1(float,float);
float sub(float, float);
float mult(float, float);
float div(float,float);

float add1(float a, float b)
{
return(a+b);
}

float sub(float c, float d)
{
if(c>d)
{
return (c-d);
}
else
{
return(d-c);
}
}

float mult(float a, float b)
{
return (a*b);
}

float div(float c, float d)
{
return (c/d);
}

void main()
{
cout<<"enter two numbers";
float a,b=0.0;
cin>>a>>b;
cout<<" sum is"<<add1(a,b)<<'\n'<<"diff is"<<sub(a,b);
cout<<"\nmult is"<<mult(a,b)<<'\n'<<"divison is"<<div(a,b);
}
