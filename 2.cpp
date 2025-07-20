#include <windows.h>
#include <iostream>
#include <psapi.h>
using namespace std;
int main()
{
    DWORD b[512];
    DWORD a;
    DWORD cProcesses;
    unsigned int l;
    EnumProcesses(b, sizeof(b), &a);
    cProcesses = a / sizeof(DWORD);
    for ( l = 0; l < cProcesses; l++ )
    {
        if( b[l] != 0 )
        {
            int c = b[l];
            cout << c << endl;
        }
    }
    return 0;
}
