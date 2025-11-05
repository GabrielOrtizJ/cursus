/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   maintest2.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/26 13:52:36 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/11/03 15:40:53 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <fcntl.h>
#include <stdio.h>
#include "get_next_line.h"


#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include "get_next_line.h"

/*
int main(void)
{
    int     fd1 = open("donquijote.txt", O_RDONLY);
    int     fd2 = open("donquijote.txt", O_RDONLY);
    int     fd3 = open("donquijote.txt", O_RDONLY);
    char    *line1;
    char    *line2;
    char    *line3;

    if (fd1 < 0 || fd2 < 0 || fd3 < 0)
    {
        perror("Error al abrir los archivos");
        return (1);
    }

    // Leer intercaladamente de los tres descriptores
    while (1)
    {
        line1 = get_next_line(fd1);
        line2 = get_next_line(fd2);
        line3 = get_next_line(fd3);

        if (!line1 && !line2 && !line3)
            break;

        if (line1)
        {
            printf("FD1: %s", line1);
            free(line1);
        }
        if (line2)
        {
            printf("FD2: %s", line2);
            free(line2);
        }
        if (line3)
        {
            printf("FD3: %s", line3);
            free(line3);
        }
    }

    close(fd1);
    close(fd2);
    close(fd3);
    return (0);
}
*/

int main(void)
{
    int     fd;
    char    *line;

    fd = open("donquijote.txt", O_RDONLY);
    if (fd < 0)
    {
        perror("Error al abrir el archivo");
        return (1);
    }
    while ((line = get_next_line(fd)) != NULL)
    {
        printf("%s", line);
        free(line);
    }
    close(fd);
    return (0);
}
/*	
int main(void)
{
    char    *line;

    printf("write lines (Ctrl+D for finish):\n");
    line = get_next_line(0);
    while (line != NULL)
    {
        printf("recibed: %s", line);
        free(line);
        line = get_next_line(0);
    }
    return (0);
}
*/