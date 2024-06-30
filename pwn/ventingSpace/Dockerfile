FROM debian

RUN apt-get update
RUN apt-get install socat -y
RUN apt-get install gcc -y
RUN apt-get install openssh-server -y

WORKDIR /

# Set root password for SSH access (change 'your_password' to your desired password)
RUN echo 'ilak:password' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
EXPOSE 22

COPY main.c .

RUN echo "0CTF{Just_L1st3n_B3tt3r}" > /flag

RUN gcc -fno-builtin -O3 -fno-stack-protector -no-pie main.c -o main

EXPOSE 6969

ENV user_ssh="ilak"
ENV pass_ssh="password"

CMD service ssh start && socat TCP-LISTEN:6969,reuseaddr,fork EXEC:./main,pty,rawer