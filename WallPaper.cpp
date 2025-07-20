#include <iostream>
#include <windows.h>
#include <cstdio>
using namespace std;
int main ()
{
	char p[MAX_PATH];
	for(int a=1;a<520;a++)
	{
		snprintf(p,MAX_PATH,"C:\\Users\\Administrator\\Desktop\\%d.bmp",a);
		Sleep(520);	
		SystemParametersInfoA(SPI_SETDESKWALLPAPER,0,p,SPIF_UPDATEINIFILE);
	}
	return 0;
}
