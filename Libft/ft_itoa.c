/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 13:10:51 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/07 13:51:11 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	get_length(int n)
{
	int	len;

	len = 0;
	if (n <= 0)
		len = 1;
	while (n)
	{
		len++;
		n /= 10;
	}
	return (len);
}

void	fill_number(char *str, int n, int len)
{
	while (n)
	{
		str[--len] = (n % 10) + '0';
		n /= 10;
	}
}

char	*ft_itoa(int n)
{
	char	*str;
	int		len;
	int		is_negative;

	len = get_length(n);
	str = (char *)malloc(len + 1);
	if (!str)
		return ((char *)0);
	str[len] = '\0';
	if (n == 0)
	{
		str[0] = '0';
		return (str);
	}
	is_negative = 0;
	if (n < 0)
	{
		is_negative = 1;
		n = -n;
	}
	fill_number(str, n, len);
	if (is_negative)
		str[0] = '-';
	return (str);
}
