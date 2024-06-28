#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to give the flag if conditions are met
void giveFlag() {
    FILE *f;
    char flag[100];

    f = fopen("flag", "r");
    if (f != NULL) {
        fgets(flag, sizeof(flag), f);
        printf("%s\n", flag);
        fclose(f);
        exit(0);
    } else {
        printf("Take ss and show to admin, the flag file is missing.\n");
        exit(1);
    }
}

int main() {
    FILE *f;
    char key[750];
    int keySize = 0;
    char c;
    
    // Open the "key" file and read its content
    f = fopen("key", "r");
    if (f == NULL) {
        printf("Key file is missing.\n");
        return 1;
    }
    
    while ((c = fgetc(f)) != EOF) {
        key[keySize] = c;
        keySize++;
    }
    fclose(f);
    
    int keyKeys[26] = {88, 85, 92, 92, 88, 97, 85, 95, 94, 95, 97, 91, 86, 89, 85, 89, 86, 86, 88, 92, 96, 86, 93, 86, 81, 89};
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++) {
            key[i * 26 + j] = key[i * 26 + j] ^ keyKeys[j];
        }
    }

    // User interaction
    char name[100];
    printf("Helloooo, what is your good name?? ");
    fgets(name, 100, stdin);
    // getchar(); // To consume the newline character left by scanf
    printf("Greetings :");
    printf(name);
    printf("\n");
    printf("What do you want to be when you grow up??\n");

    char a[500];
    fgets(a, 5000, stdin);
    printf("That's a great goal to : ");
    printf(a);
    printf("\n");
    printf("I hope you do become that!! (unless you're old[>21])\n");

    // Check the key and call giveFlag if the condition is met
    if (key[0] == 'u' &&
        key[1] == '_' &&
        key[2] == 'w' &&
        key[3] == 'i' &&
        key[4] == 'n') {
        giveFlag();
    } else {
        printf("U did not win though.\n");
        exit(0);
    }

    return 0;
}
