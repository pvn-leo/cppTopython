#include<iostream.h>
#include<conio.h>

void main()
{
int bin,p,q,r,x=0;
bin=1;
q=0;
cout<<"\t\t\tDisplay pascal Triangle";
cout<<"\n\n\nHow Many Row Do you want to input:";
cin>>r;

cout<<"\nPascal's Triangle:\n";

while(q<r)
{
for(p=40-3*q;p>0;--p)
{
cout<<" ";
}
for(x=0;x<=q;++x)
{
if(x==0 || q==0)
{
bin=1;
}
else
{
bin=(bin*(q-x+1))/x;
}
cout<<"      ";
cout<<int(bin);
}
cout<<"\n\n\n";
++q;
}

}