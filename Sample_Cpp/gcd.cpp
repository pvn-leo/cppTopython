#include <iostream>


using namespace std;

void gcd(int, int);
void gcd(int n1,int n2)

{
    
    
if (n1==n2)
    
{
      
return n1;
    
}
    
else if(n1>n2)
   
 {
        
n1=n1-n2;
        
return gcd(n1,n2);
   
 }
    
else
    
{
        
n2=n2-n1;
       
return gcd(n2,n1);
   
 }
    

}



void main()

{

int n1,n2=0;
cout<<"enter two numbers\n";
cin>>n1>>n2;

cout<<"printing the gcd of two numbers through recurssion\n";
    
cout<<gcd(n1,n2);
    

}