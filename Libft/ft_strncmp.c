/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 14:23:30 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/07 14:24:59 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strncmp(const char *src, const char *dest, int n)
{
	int	i;

	i = 0;
	while (i < n && (src[i] != '\0' || dest[i] != '\0'))
	{
		if (src[i] != dest[i])
			return ((unsigned char)src[i] - (unsigned char)dest[i]);
		i++;
	}
	return (0);
}
