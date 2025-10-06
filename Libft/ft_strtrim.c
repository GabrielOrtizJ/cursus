#include "libft.h"

char *ft_strtrim(char const *s1, char const *set)
{
    char *trimmed;
    int start;
    int end;

    if (!s1 || !set)
        return (0);
    start = 0;
    end = ft_strlen(s1);
    while (s1[start] && ft_strchr(set, s1[start]))
        start++;
    while (end > start && ft_strchr(set, s1[end - 1]))
        end--;
    trimmed = malloc(end - start + 1);
    if (!trimmed)
        return (0);
    ft_strlcpy(trimmed, s1 + start, end - start + 1);
    return (trimmed);
}
