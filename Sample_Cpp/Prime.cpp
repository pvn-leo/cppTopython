void main()
{
  int n, i=0;
  int isPrime = 1;

  cout << "Enter a positive integer: ";
  cin >> n;

  for(i = 2; i <= n / 2; ++i)
  {
      if(n % i == 0)
      {
          isPrime = 0;
          break;
      }
  }
  if (isPrime)
      {
	cout << "This is a prime number";
  	}
  else
	{
      cout << "This is not a prime number";
	}
}