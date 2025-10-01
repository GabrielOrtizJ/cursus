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

#include <stdio.h>
#include <ctype.h> // Incluye la cabecera para isdigit

int main() {
    char caracter1 = '5';
    char caracter2 = 'a';
    char caracter3 = '#';

    if (isdigit(caracter1)) {
        printf("'%c' es un dígito.\n", caracter1); // Esto se imprimirá
    } else {
        printf("'%c' no es un dígito.\n", caracter1);
    }

    if (isdigit(caracter2)) {
        printf("'%c' es un dígito.\n", caracter2);
    } else {
        printf("'%c' no es un dígito.\n", caracter2); // Esto se imprimirá
    }
    
    if (isdigit(caracter3)) {
        printf("'%c' es un dígito.\n", caracter3);
    } else {
        printf("'%c' no es un dígito.\n", caracter3); // Esto se imprimirá
    }

    return 0;
}
