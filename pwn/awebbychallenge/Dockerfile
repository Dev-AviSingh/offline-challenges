FROM debian

RUN apt-get update
RUN apt-get install socat -y
RUN apt-get install gcc -y

WORKDIR /


COPY main.c .

RUN echo "0CTF{R3ally_m1lk1ng_0v3erwr1t3s}" > /flag

RUN gcc -fno-builtin -O3 -fno-stack-protector -no-pie main.c -o main

EXPOSE 6969

CMD socat TCP-LISTEN:6969,reuseaddr,fork EXEC:./main,pty,rawer