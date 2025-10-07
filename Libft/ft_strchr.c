/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 14:12:24 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/07 14:14:20 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strchr(const char *str, int c)
{
	char	find;

	find = (char)c;
	while (*str)
	{
		if (*str == find)
		{
			return ((char *)str);
		}
		str++;
	}
	if (*str == find)
	{
		return ((char *)str);
	}
	return (0);
}
