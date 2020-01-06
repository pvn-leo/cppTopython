#include<iostream.h>
#include<conio.h>

void main()
{
int no, i=0;
cout<<"Enter Range of numbers: ";
cin>>no;
for(i=1;i<=no;i++)
{
if(i % (3*5) == 0)
{
cout<<"FizzBuzz\n";
}
else if (i % 5 == 0)
{
cout<<"Buzz\n";
}
else if (i % 3 == 0)
{
cout<<"Fizz\n";
}
else
{
cout<<i<<'\n';
}
}

}