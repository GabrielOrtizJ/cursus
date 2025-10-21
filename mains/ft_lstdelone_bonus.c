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

// Eliminar contenido
void    del(void *content)
{
    free(content);
}

// Eliminar un solo nodo
void    ft_lstdelone(t_list *lst, void (*del)(void *))
{
    if (lst)
    {
        del(lst->content);
        free(lst);
    }
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

    // Mostrar lista original
    printf("Lista original:\n");
    print_list(lista);

    // Eliminar el segundo nodo ("Mundo")
    t_list *segundo = lista->next;
    lista->next = segundo->next; // desconectar el nodo antes de borrarlo
    ft_lstdelone(segundo, del);

    // Mostrar lista después de borrar
    printf("\nDespués de eliminar el segundo nodo:\n");
    print_list(lista);

    // Liberar el resto de la lista
    while (lista)
    {
        t_list *temp = lista->next;
        ft_lstdelone(lista, del);
        lista = temp;
    }

    return 0;
}
