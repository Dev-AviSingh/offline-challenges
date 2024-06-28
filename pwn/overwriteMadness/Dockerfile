FROM debian

RUN apt-get update
RUN apt-get install socat -y
RUN apt-get install gcc -y


WORKDIR /


COPY main.c .
COPY key .
COPY flag . 

RUN gcc -fno-builtin -O3 -fno-stack-protector -no-pie main.c -o main

EXPOSE 6969

CMD socat TCP-LISTEN:6969,reuseaddr,fork EXEC:./main,pty,rawer