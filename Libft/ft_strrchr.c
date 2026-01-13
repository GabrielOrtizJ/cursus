/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 14:28:10 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/07 14:29:00 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strrchr(const char *str, int c)
{
	const char	*last;
	char		find;

	last = 0;
	find = (char)c;
	while (*str)
	{
		if (*str == find)
			last = str;
		str++;
	}
	if (*str == find)
	{
		last = str;
	}
	return ((char *)last);
}
