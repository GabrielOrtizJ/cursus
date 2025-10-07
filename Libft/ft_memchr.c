/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 13:52:31 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/07 13:53:36 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(void *buf, int c, size_t n)
{
	int				i;
	unsigned char	*str;

	i = 0;
	str = (unsigned char *)buf;
	while (i < n)
	{
		if (str[i] == (unsigned char)c)
		{
			return ((void *)(str + i));
		}
		i++;
	}
	return (0);
}
