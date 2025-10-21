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

// Liberar contenido
void del(void *content)
{
    free(content);
}

// Limpiar lista
void ft_lstclear(t_list **lst, void (*del)(void *))
{
    t_list *temp;
    while (*lst)
    {
        temp = (*lst)->next;
        del((*lst)->content);
        free(*lst);
        *lst = temp;
    }
}

// Transformar contenido (duplicar cadena)
void *duplicar(void *content)
{
    char *str = (char *)content;
    char *nuevo = malloc(strlen(str) * 2 + 1);
    if (!nuevo)
        return NULL;
    strcpy(nuevo, str);//Hola
    strcat(nuevo, str);//HolaHola
    return nuevo;
}

// Mapear lista
t_list *ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
    t_list *new_list = NULL;
    t_list *new_node;

    while (lst)
    {
        new_node = ft_lstnew(f(lst->content));
        if (!new_node)
        {
            ft_lstclear(&new_list, del);
            return NULL;
        }
        ft_lstadd_back(&new_list, new_node);
        lst = lst->next;
    }
    return new_list;
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
    t_list *original = NULL;

    // Crear lista original
    ft_lstadd_back(&original, ft_lstnew(strdup("Hola")));
    ft_lstadd_back(&original, ft_lstnew(strdup("Mundo")));
    ft_lstadd_back(&original, ft_lstnew(strdup("42")));

    // Mapear lista
    t_list *duplicada = ft_lstmap(original, duplicar, del);

    // Mostrar listas
    printf("Original:\n");
    print_list(original);

    printf("\nDuplicada:\n");
    print_list(duplicada);

    // Liberar ambas listas
    ft_lstclear(&original, del);
    ft_lstclear(&duplicada, del);

    return 0;
}
