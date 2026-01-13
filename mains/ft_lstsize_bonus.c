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

// Añadir al final
void ft_lstadd_back(t_list **alst, t_list *new)
{
    t_list *temp;

    if (!*alst)
    {
        *alst = new;
        return;
    }
    temp = *alst;
    while (temp->next)
        temp = temp->next;
    temp->next = new;
}

// Contar nodos
int ft_lstsize(t_list *lst)
{
    int n = 0;
    while (lst != NULL)
    {
        ++n;
        lst = lst->next;
    }
    return n;
}

// Liberar lista
void ft_lstclear(t_list **lst)
{
    t_list *temp;
    while (*lst)
    {
        temp = (*lst)->next;
        free((*lst)->content);
        free(*lst);
        *lst = temp;
    }
}

int main(void)
{
    t_list *lista = NULL;

    // Crear lista con 3 nodos
    ft_lstadd_back(&lista, ft_lstnew(strdup("Hola")));
    ft_lstadd_back(&lista, ft_lstnew(strdup("Mundo")));
    ft_lstadd_back(&lista, ft_lstnew(strdup("42")));

    // Obtener tamaño
    int tamano = ft_lstsize(lista);
    printf("La lista tiene %d nodos.\n", tamano);

    // Liberar memoria
    ft_lstclear(&lista);

    return 0;
}
