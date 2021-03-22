#include <stdio.h>

int main(void)
{
    char name[19];
    printf("What's your name?\n");
    fgets(name, 16 , stdin);
    printf("Hello, %s", name);
    return 0;
}

// clang -o hello hello.c
// ./hello
// mv hello.c hello2.c


// #include <stdio.h>

// int main(void)

// {
//     char c = 'a';
//     printf("%i\n", (int) c);
// }
