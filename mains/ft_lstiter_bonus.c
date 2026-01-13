#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

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

// Función que transforma el contenido a mayúsculas
void to_upper(void *content)
{
    char *str = (char *)content;
    for (int i = 0; str[i]; i++)
        str[i] = toupper(str[i]);
}

// Aplicar función a cada nodo
void    ft_lstiter(t_list *lst, void (*f)(void *))
{
    while (lst)
    {
        f(lst->content);
        lst = lst->next;
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

// Liberar lista
void free_list(t_list *lst)
{
    t_list *temp;
    while (lst)
    {
        temp = lst->next;
        free(lst->content);
        free(lst);
        lst = temp;
    }
}

int main(void)
{
    t_list *lista = NULL;

    // Crear nodos con strdup para tener memoria dinámica
    ft_lstadd_back(&lista, ft_lstnew(strdup("hola")));
    ft_lstadd_back(&lista, ft_lstnew(strdup("mundo")));
    ft_lstadd_back(&lista, ft_lstnew(strdup("42")));

    // Mostrar antes
    printf("Antes de ft_lstiter:\n");
    print_list(lista);

    // Aplicar transformación
    ft_lstiter(lista, to_upper);

    // Mostrar después
    printf("\nDespués de ft_lstiter:\n");
    print_list(lista);

    // Liberar memoria
    free_list(lista);

    return 0;
}
