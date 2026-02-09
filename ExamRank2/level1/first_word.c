/*
Assignment name  : first_word
Expected files   : first_word.c
Allowed functions: write
--------------------------------------------------------------------------------

Write a program that takes a string and displays its first word, followed by a
newline.

A word is a section of string delimited by spaces/tabs or by the start/end of
the string.

If the number of parameters is not 1, or if there are no words, simply display
a newline.

Examples:

$> ./first_word "FOR PONY" | cat -e
FOR$
$> ./first_word "this        ...    is sparta, then again, maybe    not" | cat -e
this$
$> ./first_word "   " | cat -e
$
$> ./first_word "a" "b" | cat -e
$
$> ./first_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
$>

*/

#include <unistd.h>

int main(int argc, char **argv )
{
	char **param;
	//si hay dos paramentros pasa por aqui
	if(argc == 2)
	{
		unsigned int i;
        
		i = 0;
		//si el elemento es tab o espacio pasa al siguiente
		while (argv[1][i] == 32 || argv[1][i] == 9)
        	i++;
		//si el elemento es diferente a espacio o tab imprime el elemento actual 
		//hasta que queden elementos 
		while ((argv[1][i] != 32 && argv[1][i] != 9) && argv[1][i])
            write(1, &argv[1][i++], 1);
    }
	//el salto de linea
	write(1, "\n", 1);
}