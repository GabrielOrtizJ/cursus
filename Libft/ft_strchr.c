char *ft_strchr(const char *str, int c)
{
	char find;
	
	find = (char)c;
	while (*str)
	{
		if(*str == find)
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
