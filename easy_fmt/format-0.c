#include <stdio.h>
#include <stdlib.h>

void vuln(char* flag)
{
	char buf[64];
	printf("Type something get fmt>");
	fgets(buf, sizeof(buf), stdin);
	printf(buf);
}

int main()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	char flag[256];
	FILE* f = fopen("./flag.txt", "r");
	if (f == NULL) {
		exit(1);
	}
	else {
		fgets(flag, sizeof(flag), f);
	}
	vuln(flag);
	return 0;
}
