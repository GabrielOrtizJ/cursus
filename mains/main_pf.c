#include "ft_printf.h"

int main(void)
{
    int     ret;
    int     num = 42;
    unsigned int unum = 4294967295;
    char    *str = "Hola 42";
    void    *ptr = str;

    // Prueba de texto simple
    ret = ft_printf("Texto simple\n");
    ft_printf("Caracteres impresos: %d\n\n", ret);

    // Prueba de %c
    ret = ft_printf("Caracter: %c\n", 'A');
    ft_printf("Caracteres impresos: %d\n\n", ret);

    // Prueba de %s
    ret = ft_printf("Cadena: %s\n", str);
    ft_printf("Caracteres impresos: %d\n\n", ret);

    // Prueba de %p
    ret = ft_printf("Puntero: %p\n", ptr);
    ft_printf("Caracteres impresos: %d\n\n", ret);

    // Prueba de %d / %i
    ret = ft_printf("Entero con signo:   %d ---- %i\n", num,num);
    ft_printf("Caracteres impresos: %d\n\n", ret);

    // Prueba de %u
    ret = ft_printf("Entero sin signo: %u\n", unum);
    ft_printf("Caracteres impresos: %d\n\n", ret);

    // Prueba de %x y %X
    ret = ft_printf("Hexadecimal minúsculas: %x\n", 255);
    ft_printf("Caracteres impresos: %d\n", ret);
    ret = ft_printf("Hexadecimal mayúsculas: %X\n", 255);
    ft_printf("Caracteres impresos: %d\n\n", ret);

    // Prueba de %%
    ret = ft_printf("Porcentaje: %%\n");
    ft_printf("Caracteres impresos: %d\n\n", ret);

    return (0);
}
