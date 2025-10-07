/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 14:07:20 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/07 14:08:29 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_memset(void *str, int byte, size_t c)
{
	unsigned char	*ptr;

	ptr = (unsigned char *)str;
	while (c--)
		*ptr++ = (unsigned char)byte;
}
