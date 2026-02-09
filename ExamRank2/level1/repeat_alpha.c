/*
Assignment name  : repeat_alpha
Expected files   : repeat_alpha.c
Allowed functions: write
--------------------------------------------------------------------------------

Escriba un programa llamado repeat_alpha que tome una cadena y la muestre,
repitiendo cada carácter alfabético tantas veces como su índice,
seguido de un salto de línea.

"a" se convierte en "a", "b" en "bb", "e" en "eeeee", etc.

Se mantiene la distinción entre mayúsculas y minúsculas.

Si el número de argumentos no es 1, simplemente se muestra un salto de línea.

Examples:

$>./repeat_alpha "abc"
abbccc
$>./repeat_alpha "Alex." | cat -e
Alllllllllllleeeeexxxxxxxxxxxxxxxxxxxxxxxx.$
$>./repeat_alpha 'abacadaba 42!' | cat -e
abbacccaddddabba 42!$
$>./repeat_alpha | cat -e
$
$>
$>./repeat_alpha "" | cat -e
$
$>
*/

#include <unistd.h>

int main(int ac, char *av[])
{
    int i;
    int j;
    
    if (ac == 2)
    {
        i = 0;
        while (av[1][i])
        {
            if (av[1][i] >= 65 && av[1][i] <= 90)
            {
                j = 0;

                while (j < av[1][i] - 64)
                {
                    write(1, &av[1][i], 1);
                    j++;
                }
            }
            else if (av[1][i] >= 97 && av[1][i] <= 122)
            {
                j = 0;

                while (j < av[1][i] - 96)
                {
                    write(1, &av[1][i], 1);
                    j++;
                }
            }
            else
                write(1, &av[1][i], 1);
            i++;
        }
    }
    write(1, "\n", 1);
}