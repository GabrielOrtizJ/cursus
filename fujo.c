/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fujo.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 12:05:14 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/11/05 12:22:12 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include "ft_printf.h"

// Función que interpreta el tipo de formato y llama a la función correspondiente para imprimir el argumento.
void    ft_format(va_list va, char *str, size_t *counter)
{
    // Si el formato es 'c', imprime un carácter (extraído como int).
    if (*str == 'c')
        ft_putchar_pf(va_arg(va, int), counter);
    // Si el formato es 's', imprime una cadena (char *).
    else if (*str == 's')
        ft_putstr_pf(va_arg(va, char *), counter);
    // Si el formato es 'p', imprime un puntero como dirección hexadecimal.
    else if (*str == 'p')
        ft_putptr_pf(va_arg(va, void *), counter);
    // Si el formato es 'i' o 'd', imprime un entero con signo.
    else if (*str == 'i' || *str == 'd')
        ft_putnbr_pf(va_arg(va, int), counter);
    // Si el formato es 'u', imprime un entero sin signo.
    else if (*str == 'u')
        ft_putuint_pf(va_arg(va, unsigned int), counter);
    // Si el formato es 'x' o 'X', imprime el número en hexadecimal.
    else if (*str == 'x' || *str == 'X')
    {
        // Si es 'x', usa minúsculas.
        if (*str == 'x')
            ft_puthex_pf(va_arg(va, unsigned int), counter, HEX_LOW_BASE);
        // Si es 'X', usa mayúsculas.
        else
            ft_puthex_pf(va_arg(va, unsigned int), counter, HEX_UPP_BASE);
    }
    // Si el formato es '%', imprime el carácter '%' literalmente.
    else if (*str == '%')
        ft_putchar_pf(*str, counter);
}
// Implementación personalizada de printf que interpreta la cadena de formato y los argumentos variables.
int ft_printf(char const *str, ...)
{
    va_list     va;        // Lista de argumentos variables.
    size_t      counter;   // Contador de caracteres impresos.

    // Si la cadena de formato es nula, no se imprime nada.
    if (!str)
        return (0);

    counter = 0;           // Inicializa el contador.
    va_start(va, str);     // Inicializa la lista de argumentos variables.

    // Recorre cada carácter de la cadena de formato.
    while (*str)
    {
        // Si encuentra un '%', significa que viene un especificador de formato.
        if (*str == '%')
        {
            str++; // Avanza al carácter siguiente (el tipo de formato).
            ft_format(va, (char *)str, &counter); // Llama a la función que interpreta el formato.
        }
        else
            // Si no es '%', imprime el carácter tal cual.
            ft_putchar_pf(*str, &counter);

        str++; // Avanza al siguiente carácter.
    }

    va_end(va); // Finaliza el uso de la lista de argumentos.
    return (counter); // Devuelve el número total de caracteres impresos.
}
