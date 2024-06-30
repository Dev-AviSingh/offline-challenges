#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Get the USER environment variable
    char *user_env = getenv("user_ssh");
    if (user_env) {
    } else {
        printf("USER environment variable is not set.\n");
    }

    // Get the PASS environment variable
    char *pass_env = getenv("pass_ssh");
    if (pass_env) {
    } else {
        printf("PASS environment variable is not set.\n");
    }
    char ambition[500];
    printf("What is your ambition? ");
    fgets(ambition, 500, stdin);

    printf(ambition);

    printf(ambition);

    printf(ambition);

    printf("Saying it 3 times makes it true.");
    return 0;
}
