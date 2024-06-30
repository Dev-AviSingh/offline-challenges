#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char username[50];
    char password[50];
    char command[500];

    // Prompt for username
    printf("Enter username: ");
    fgets(username, sizeof(username), stdin);
    username[strcspn(username, "\n")] = '\0'; // Remove newline character

    // Prompt for password
    printf("Enter password: ");
    fgets(password, sizeof(password)*2, stdin);
    password[strcspn(password, "\n")] = '\0'; // Remove newline character

    // Execute the command
    system(command);

    return 0;
}
