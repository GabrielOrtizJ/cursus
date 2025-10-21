#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define la estructura t_list
typedef struct s_list
{
    void            *content;
    struct s_list   *next;
}   t_list;

// Crea un nuevo nodo
t_list *ft_lstnew(void *content)
{
    t_list *node = malloc(sizeof(t_list));
    if (!node)
        return NULL;
    node->content = content;
    node->next = NULL;
    return node;
}

// Añade un nodo al final de la lista
void    ft_lstadd_back(t_list **alst, t_list *new)
{
    t_list  *temporal;

    temporal = (*alst);
    if ((*alst))
    {
        while (temporal->next != NULL)
            temporal = temporal->next;
        temporal->next = new;
    }
    if (!(*alst))
        ((*alst) = new);
}

// Imprime la lista
void print_list(t_list *lst)
{
    while (lst)
    {
        printf("%s\n", (char *)lst->content);
        lst = lst->next;
    }
}

int main(void)
{
    t_list *lista = NULL;

    // Crear nodos
    t_list *nodo1 = ft_lstnew(strdup("Hola"));
    t_list *nodo2 = ft_lstnew(strdup("Mundo"));
    t_list *nodo3 = ft_lstnew(strdup("42"));

    // Añadir al final
    ft_lstadd_back(&lista, nodo1);
    ft_lstadd_back(&lista, nodo2);
    ft_lstadd_back(&lista, nodo3);

    // Mostrar lista
    print_list(lista);

    // Liberar memoria
    t_list *temp;
    while (lista)
    {
        temp = lista->next;
        free(lista->content);
        free(lista);
        lista = temp;
    }

    return 0;
}
