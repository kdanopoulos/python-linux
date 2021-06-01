#define _GNU_SOURCE

#include <time.h>
#include <stdio.h>
#include <dlfcn.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/stat.h>
#include <openssl/md5.h>
#include <errno.h>
#include <string.h>


FILE *
fopen(const char *path, const char *mode) 
{

	FILE *original_fopen_ret;
	FILE *(*original_fopen)(const char*, const char*);
	/* call the original fopen function */
	original_fopen = dlsym(RTLD_NEXT, "fopen");
	original_fopen_ret = (*original_fopen)(path, mode);

	FILE *fp;
	fp = fopen64(path,"rb");
	if(fp!=NULL){
		printf("fp is not NULL\n");
		size_t elements;
		char myBuffer[1024];
		elements = fread(myBuffer,1024, 1, fp);
		printf("elements = %d\n", elements);
		fclose(fp);
	}

	return original_fopen_ret;
}
