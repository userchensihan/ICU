#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <linux/wireless.h>
int csh(const char *a,int b){
    int s;
    struct iwreq y;
    if ((s=socket(AF_INET,SOCK_DGRAM,0))<0) {
        perror("Fuck You");
        return -1;
    }
    memset(&y,0,sizeof(y));
    snprintf(y.ifr_name,IFALIASZ,"%s",a);
    y.u.freq.m = b;
    y.u.freq.flags = IW_FREQ_FIXED;
    if (ioctl(s,SIOCSIWFREQ,&y)<0) {
        perror("Syntax Not OK");
        close(s);
        return -1;
    }
    close(s);
    return 0;
}

int main() {
    const char *a = "wlan0";
    int b = 1;
    if (csh(a,b)==0) {
        printf("Syntax OK");
    }
    return 0;
}
