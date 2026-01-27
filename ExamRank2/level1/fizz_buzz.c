/*
Assignment name  : fizzbuzz
Expected files   : fizzbuzz.c
Allowed functions: write
--------------------------------------------------------------------------------

Write a program that prints the numbers from 1 to 100, each separated by a
newline.

If the number is a multiple of 3, it prints 'fizz' instead.

If the number is a multiple of 5, it prints 'buzz' instead.

If the number is both a multiple of 3 and a multiple of 5, it prints 'fizzbuzz' instead.

Example:

$>./fizzbuzz
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
[...]
97
98
fizz
buzz
$>
*/



#include <unistd.h>

void ft_putnbr(int i)
{
    /* 
	Si el número es mayor que 9, volvemos a llamar a la función
	con el número dividido entre 10, de modo que eliminamos un dígito
	al final (123 => 12)
     */
    if (i > 9)
        ft_putnbr(i / 10);
    /* 
	Entonces podemos imprimir el carácter en el índice i % 10 (123 => 3)
	en una cadena que contiene todos los dígitos del 0 al 9
     */
    write(1, &"0123456789"[i % 10], 1);
	/*  Explicaré lo que escribí arriba:
	En C, las cadenas no existen. Cuando almacenamos una cadena, almacenamos un 
	array de caracteres que termina en un carácter NUL.
	Así que lo que hice arriba fue escribir una cadena, y luego hice
	lo mismo que harías para seleccionar un elemento de array con el
	corchete para seleccionar un índice específico.
	El segundo argumento de la función de escritura es un carácter.
	Por eso añadí el carácter & delante de la cadena.
	De esta manera, le doy a write() un puntero al carácter específico que 
	quiero escribir.
	*/
}

int main(void)
{
    int i;
    
    i = 1;
    while (i <= 100)
    {
        if (i % 3 == 0 && i % 5 == 0)
            write(1, "fizzbuzz", 8);
        else if  (i % 3 == 0)
            write(1, "fizz", 4);
        else if (i % 5 == 0)
            write(1, "buzz", 4);
        else
            ft_putnbr(i);
        i++;
        write(1, "\n", 1);
    }
	return (0);
}