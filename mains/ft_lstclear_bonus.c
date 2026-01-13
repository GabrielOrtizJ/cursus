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

// Liberar contenido
void    del(void *content)
{
    free(content);
}

// Limpiar toda la lista
void    ft_lstclear(t_list **lst, void (*del)(void *))
{
    t_list  *gon;
    t_list  *aux;

    aux = *lst;
    if (!aux)
        return;
    while (aux)
    {
        gon = aux->next;
        del(aux->content);
        free(aux);
        aux = gon;
    }
    *lst = NULL;
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
    ft_lstadd_back(&lista, ft_lstnew(strdup("Hola")));
    ft_lstadd_back(&lista, ft_lstnew(strdup("Mundo")));
    ft_lstadd_back(&lista, ft_lstnew(strdup("42")));

    // Mostrar lista antes de limpiar
    printf("Antes de limpiar:\n");
    print_list(lista);

    // Limpiar lista
    ft_lstclear(&lista, del);

    // Verificar que está vacía
    if (!lista)
        printf("Lista vacía después de ft_lstclear ✅\n");

    return 0;
}
