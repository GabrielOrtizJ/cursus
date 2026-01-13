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
t_list *ft_lstnew(void *content)
{
    t_list *node = malloc(sizeof(t_list));
    if (!node)
        return NULL;
    node->content = content;
    node->next = NULL;
    return node;
}

// Añadir al principio
void    ft_lstadd_front(t_list **alst, t_list *new)
{
    new->next = *alst;
    *alst = new;
}

// Imprimir lista
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

    // Añadir al principio (orden inverso)
    ft_lstadd_front(&lista, nodo1); // lista: Hola
    ft_lstadd_front(&lista, nodo2); // lista: Mundo → Hola
    ft_lstadd_front(&lista, nodo3); // lista: 42 → Mundo → Hola

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
