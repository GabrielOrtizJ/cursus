#include <ctype.h>
#include <stdio.h>
#include <string.h>
int ft_strlen(const char *c)
{
	int i;

	i = 0;
	while(c[i])
	{
		i++;
	}
	return (i);
	
}

int main() {
    char caracter1 = '5';
    char caracter2 = 'a';

    if (isdigit(caracter1)) {
        printf("'%c' es un dígito\n %lu" , caracter1,isdigit(caracter1)); // Se imprimirá
    } else {
        printf("'%c' no es un dígito\n %lu" , caracter1 ,isdigit(caracter1));
    }

    if (isdigit(caracter2)) {
        printf("'%c' es un dígito\n", caracter2);
    } else {
        printf("'%c' no es un dígito\n", caracter2); // Se imprimirá
    }

    return 0;
}
