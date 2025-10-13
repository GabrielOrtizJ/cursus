/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 21:58:40 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/13 21:58:40 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list *gon;
	t_list *aux;
	t_list *auxgon;

	aux = lst;
	if (!(gon = malloc(sizeof(t_list))))
		return (0);
	auxgon = gon;
	while (aux)
	{
		auxgon->content = f(aux->content);
		if (!(auxgon->next = malloc(sizeof(t_list))))
			ft_lstclear(&aux, del);
		aux = aux->next;
		auxgon = auxgon->next;
	}
	return (gon);
}
