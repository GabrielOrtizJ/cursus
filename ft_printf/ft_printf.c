/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 12:43:03 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/11/04 13:10:40 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdarg.h>

void ft_putformat(va_list format)
{
	
	 if (*format == '%') {
            format++;
			n = va_arg(args, int);

            if (*format == 'c') // Imprime un solo carácter.
                ft_putnbr(n);
			if (*format == 's') // Imprime una string (como se define por defecto en C).
                ft_putnbr(n);
			if (*format == 'p') // El puntero void * dado como argumento se imprime en formato hexadecimal.
                ft_putnbr(n);
			if (*format == 'd') // Imprime un número decimal (base 10)
                ft_putnbr(n);
			if (*format == 'i') // Imprime un entero en base 10.
                ft_putnbr(n);
			if (*format == 'u') // Imprime un número decimal (base 10) sin signo.
                ft_putnbr(n);
			if (*format == 'x') // Imprime un número hexadecimal (base 16) en minúsculas
                ft_putnbr(n);
			if (*format == 'X') // Imprime un número hexadecimal (base 16) en mayúsculas.
                ft_putnbr(n);
			if (*format == '%') // para imprimir el símbolo del porcentaje
                ft_putnbr(n);
        } else {
            ft_putchar(*format);
        }
}

int ft_printf(const char *format, ...) {
    va_list args;
    va_start(args, format);
	int n;
    while (*format) {
       
        format++;
    }
    va_end(args);
    return (0);
}

