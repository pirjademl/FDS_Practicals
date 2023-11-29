#include <iostream>
#include <cstring> // Header file for strlen function
#define max 50

using namespace std;

class STACK
{

private:
    char a[max];
    int top;

public:
    STACK()
    {
        top = -1;
    }

    void push(char);
    void reverse();
    void convert(char[]);
    void palindrome();
};

void STACK::push(char c)
{
    top++;
    a[top] = c;
    a[top + 1] = '\0';

    cout << endl
         << c << " is pushed on stack ...";
}

void STACK::reverse()
{
    cout << "\n\nReverse string is : ";
    for (int i = top; i >= 0; i--)
    {
        cout << a[i];
    }
    cout << endl;
}

void STACK::convert(char str[])
{
    for (int i = 0; str[i] != '\0'; i++)
    {
        if ((int)str[i] >= 97 && (int)str[i] <= 122)
            str[i] = (char)((int)str[i] - 32);
    }

    cout << endl
         << "Converted String : " << str << "\n";
}

void STACK::palindrome()
{
    char str[max];
    int j = 0;

    for (int i = top; i >= 0; i--, j++)
    {
        str[j] = a[i];
    }
    str[j] = '\0';

    if (strcmp(str, a) == 0)
        cout << " n\nString is palindrome...";
    else
        cout << "\n\nString is not palindrome...";
}

int main()
{
    STACK stack;

    char str[max];
    int i = 0;

    cout << "\nEnter string to be reversed and check if it's a palindrome or not : \n\n";
    cin.getline(str, 50);

    stack.convert(str);

    while (str[i] != '\0')
    {
        stack.push(str[i]);
        i++;
    }

    stack.palindrome();

    stack.reverse();

    return 0;
}
