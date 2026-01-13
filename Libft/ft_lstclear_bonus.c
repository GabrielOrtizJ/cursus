/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 21:51:27 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/14 12:10:01 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*gon;
	t_list	*aux;

	aux = *lst;
	if (!(aux))
		return ;
	while (aux)
	{
		gon = aux->next;
		del(aux->content);
		free(aux);
		aux = gon;
	}
	*lst = NULL;
}
