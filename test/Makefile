all: load  main

load: load.c
	gcc -Wall -fPIC -shared -o load.so load.c -lcrypto -ldl 

main: main.c 
	gcc main.c -o main

run: load.so main
	LD_PRELOAD=./load.so ./main

clean:
	rm -rf load.so
	rm -rf main
