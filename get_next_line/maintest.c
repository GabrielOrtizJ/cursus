#include <fcntl.h>     // open
#include <unistd.h>    // read, close
#include <stdlib.h>    // malloc, free
#include <stdio.h>     // printf, perror

#define	BUFFER_SIZE 42

int	main(void)
{
	int		fd;
	ssize_t bytes_read;
	char	*buffer;

	// Abrimos el archivo en modo solo lectura
	fd = open("archivo.txt", O_RDONLY);
	if (fd == -1)
	{
		perror("Error al abrir el archivo");
		return 1;
	}

	// Reservamos memoria para el buffer (+1 para el '\0')
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
	{
		perror("Error al reservar memoria");
		close(fd);
		return 1;
	}

	// Leemos del archivo en bloques de BUFFER_SIZE
	while ((bytes_read = read(fd, buffer, BUFFER_SIZE)) > 0)
	{
		buffer[bytes_read] = '\0'; // Aseguramos que sea una cadena válida
		printf("%s", buffer);      // Mostramos lo leído
	}

	if (bytes_read == -1)
		perror("Error al leer el archivo");

	// Liberamos recursos
	free(buffer);
	close(fd);
	return 0;
}
