#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estructura de nodo
typedef struct s_list
{
    void            *content;
    struct s_list   *next;
}   t_list;

// Crear nuevo nodo
t_list  *ft_lstnew(void const *content)
{
    t_list  *prueba;

    prueba = (t_list *)malloc(sizeof(t_list));
    if (!prueba)
        return (NULL);
    prueba->content = (void *)content;
    prueba->next = NULL;
    return (prueba);
}

int main(void)
{
    // Crear contenido dinámico
    char *texto = strdup("Hola mundo");

    // Crear nodo con ese contenido
    t_list *nodo = ft_lstnew(texto);

    // Mostrar contenido
    if (nodo)
        printf("Contenido del nodo: %s\n", (char *)nodo->content);
    else
        printf("Error al crear el nodo.\n");

    // Liberar memoria
    free(nodo->content);
    free(nodo);

    return 0;
}
