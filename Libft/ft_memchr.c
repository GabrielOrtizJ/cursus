typedef unsigned long size_t; 

void *ft_memchr(void *buf, int c, size_t n)
{
	int i;
	unsigned char *str;

	i = 0;
	str = (unsigned char *)buf;

	while (i < n )
	{
		if (str[i] == (unsigned char)c)
		{
			return ((void *)(str + i));
		}
		i++;
	}
	return (0);
}
