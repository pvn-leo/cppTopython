# cppTopython
This code has been written in Python. Works and tested well with python 3.5+<br>



### About the project:
<ul>
   <li>This program takes a CPP file as input and produces a python file as output with the required code conversion form C++ to python</li>
   <li>The program is written in python language and is written in simple language for better readability.The program makes use of several core concepts of python programming language such as defining functions,using inbuilt functions,file concepts along with multiple iterative and conditional statements and basic concepts of lists,tuples and dictionaries to read,create and print the lines of code in C++ into another  file after conversion</li>
   <li>The program relies heavily on line by line iteration of the input data after which defined functions are called to detect the presence  of specific statements or words in the line of code to change it to the corresponding python code syntax</li>
</ul>



##### Note: 
The above code doesnt work for any of the OOP principles in C++. It works well with simple C++ programs.
This program was designed, keeping in mind those individuals who transition from C++ to Python, and almost want to quickly get to  know the syntax of the the language.


###  To run:<br>
1. Execute the cpptopy.py file on a terminal or an IDE etc.
2. Enter the name of your input file in .cpp or .txt format.(Sample C++ files are placed in Sample_Cpp folder)
3. Enter the name of the final output file in a .py file. You can execute the newly created .py file to check if it works.
!! Ensure you take care of brackets !!

### Limitations:
<ul>
   <li>The C++ code taken as the input should always contain only one line of code in a single line and should NOT include multiple lines separated by  ";" 
Ex:"cout<<"hello";
   cin>>a;" works
but "cout<<"hello";cin>>a;" doesn't work.</li>
   <li>Multiple variable declaration is not supported in the same line but inizialization works.
Ex:
"int a=10;
 int b=10; 
 int a,b=10;" works
but "int a,b" doesn't work.</li>
   <li>Multiple cin and cout cascading not supported.
Ex:"cin>>a>>b;" doesn't work.
</li>
   <li>Prototypes are required before function call regardless of where the function is defined.
Ex:
void amstr(int);
void amstr(int a)
{...
....
....}
works but
void amstr(int a)
{...
....
....}
without prototype will not be identified as a function.</li>
   <li>condition statements or iterative statements won't work if they do not contain flower brackets.
Ex:
if (a==5)
cout<<"hello";
works in C++ but for proper conversion it has to be in the form
if (a==5)
{
cout<<"hello";
}</li>
   <li>Opening and Closing of Brackets for each block should be in seperate lines and these lines should not have any statememnts.
Ex:
"if(i<=90)
{
cout<<i;
}"works
"if(i<=90)
{cout<<i;}"doesn't work

"if(i<=90)
{cout<<i;
}"doesn't work


"if(i<=90)
{
cout<<i;}"doesn't work</li>
   <li>void main() works but int main() dosen't.</li>
   <li>Classes with only inline functions work. </li>
   <li>  int k = func(); doesn't work but func() and cout of func() works</li>
  
   </ul>

___________________________________________________________________________________________________________________________________
#### Scope:
-This program can be used in educational institutions for better understanding of how python works.<br>
-Can be used as a tool for beginners to understand Python code by comparing with the corresponding C++ code.<br>
-Is effective when instant switching is required for professionals since python supports much more libraries and is more powerful when compared to C++.

#### Commits are entertained.
