/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 13:22:42 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/10/07 14:14:41 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	get_word_bounds(char const *s, char c, int *i, int *start)
{
	while (s[*i] == c)
		(*i)++;
	*start = *i;
	while (s[*i] && s[*i] != c)
		(*i)++;
}

int	copy_word(char **res, char const *s, int start, int end)
{
	res[0] = (char *)malloc(end - start + 1);
	if (!res[0])
		return (0);
	ft_strlcpy(res[0], s + start, end - start + 1);
	return (1);
}

char	**ft_split(char const *s, char c)
{
	char	**result;
	int		i;
	int		j;
	int		start;
	int		end;
	int		word_count;

	if (!s)
		return (0);
	word_count = count_words(s, c);
	result = (char **)malloc((word_count + 1) * sizeof(char *));
	if (!result)
		return (0);
	i = 0;
	j = 0;
	while (s[i] && j < word_count)
	{
		get_word_bounds(s, c, &i, &start);
		end = i;
		if (!copy_word(&result[j], s, start, end))
			return (ft_free_split(result, j));
		j++;
	}
	result[j] = 0;
	return (result);
}

char	**ft_free_split(char **split, int j)
{
	while (j >= 0)
	{
		free(split[j]);
		j--;
	}
	free(split);
	return (0);
}

int	count_words(char const *s, char c)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*s)
	{
		if (*s == c)
			in_word = 0;
		else if (!in_word)
		{
			in_word = 1;
			count++;
		}
		s++;
	}
	return (count);
}
