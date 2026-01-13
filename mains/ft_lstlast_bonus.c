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
void    ft_lstadd_back(t_list **alst, t_list *new)
{
    t_list  *temp;

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

// Obtener el último nodo
t_list  *ft_lstlast(t_list *lst)
{
    t_list  *p;

    p = lst;
    if (p == NULL || lst == NULL)
        return (NULL);
    if (p->next == NULL)
        return (p);
    while (p)
    {
        if (p->next == NULL)
            return (p);
        p = p->next;
    }
    return (p);
}

int main(void)
{
    t_list *lista = NULL;

    // Crear nodos con contenido dinámico
    ft_lstadd_back(&lista, ft_lstnew(strdup("Hola")));
    ft_lstadd_back(&lista, ft_lstnew(strdup("Mundo")));
    ft_lstadd_back(&lista, ft_lstnew(strdup("42")));

    // Obtener el último nodo
    t_list *ultimo = ft_lstlast(lista);

    // Mostrar contenido del último nodo
    if (ultimo)
        printf("Último nodo: %s\n", (char *)ultimo->content);
    else
        printf("La lista está vacía.\n");

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
