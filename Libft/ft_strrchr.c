char *ft_strrchr(const char *str, int c)
{
	const char *last = 0;
	char find = (char)c;

	while (*str)
	{
		if (*str == find)
			last = str;
		str++;
	}
	if (*str == find)
	{
		last = str;
	} // Para el caso de '\0'
		
	return (char *)last;
}

