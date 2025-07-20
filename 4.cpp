#define _WIN32_WINNT 0x0501
#include <windows.h>
#include <iostream>
#include <shlobj.h>
#include <string>
int main() {
	const wchar_t* s = L"C:\\Users\\Administrator\\Desktop\\Panda.exe";
	wchar_t p[MAX_PATH];
	HRESULT b = SHGetFolderPathW(NULL,
	CSIDL_STARTUP,
	NULL,
	0,
	p
	);
	std::wstring f = L"\\Panda.exe";
	std::wstring u = p + f;
	std::wcout << u << std::endl;
	if (CopyFileW(s,u.c_str(),TRUE)) {
		std::cout << "Succeess" << std::endl;
	} else {
		DWORD e = GetLastError();
		std::cerr << e << std::endl;
	}
	return 0;
}
