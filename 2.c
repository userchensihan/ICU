#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>
#include <arpa/inet.h>
int main() {
    int s;
    struct sockaddr_in e;
    char r[1024];
    char p[128];
    s=socket(AF_INET,SOCK_STREAM,0);    
    memset(&e, 0, sizeof(e));
    e.sin_family = AF_INET;
    e.sin_port = htons(80);
    inet_pton(AF_INET,"192.168.1.1",&e.sin_addr);
    if (connect(s,(struct sockaddr *)&e, sizeof(e)) < 0) {
        perror("fuck!");
        close(s);
        exit(EXIT_FAILURE);
    }
    snprintf(r, sizeof(r), 
             "POST /cgi-bin/luci HTTP/1.1\r\n"
	     "Content-Type: application/x-www-form-urlencoded\r\n"
	     "Content-Length: 23\r\n"
	     "Host: 192.168.1.1\r\n"
             "Connection: close\r\n\r\n"             
             "username=useradmin&psd=" 
             );
    send(s,r,strlen(r),0); 
    close(s);
    return 0;
}
