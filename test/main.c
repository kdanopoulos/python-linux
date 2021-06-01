#include <stdio.h>
#include <string.h>
#include <pwd.h>
#include <sys/types.h>

int main() 
{
	char text[100];
	sprintf(text, "this is a text");
	FILE *fp;
	fp = fopen("koukou.txt","a");
	if(fp!=NULL){
		fputs(text, fp);
		fclose(fp);
	}

}
