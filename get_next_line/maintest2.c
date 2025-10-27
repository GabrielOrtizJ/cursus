/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   maintest2.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/26 13:52:36 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/26 13:52:36 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <fcntl.h>      // open
#include <unistd.h>     // close
#include <stdio.h>      // printf
#include "get_next_line.h"  // tu header con el prototipo

int main(void)
{
    int fd;
    char *line;

    // Abrimos el archivo de prueba
    fd = open("texto.txt", O_RDONLY);
    if (fd == -1)
    {
        perror("Error al abrir el archivo");
        return 1;
    }

    // Leemos línea por línea usando get_next_line
    while ((line = get_next_line(fd)) != NULL)
    {
        printf("Línea leída: %s", line); // ya incluye \n si lo tiene
        free(line); // liberamos la memoria de cada línea
    }

    // Cerramos el archivo
    close(fd);
    return 0;
}