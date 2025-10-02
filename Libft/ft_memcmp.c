typedef unsigned long size_t;

int ft_memcmp(const void *buf1, const void *buf2, size_t n)
{
	unsigned char *c1;
	unsigned char *c2;
	size_t i;

	i = 0;
	c1 = (unsigned char *)buf1;
	c2 = (unsigned char *)buf2;
	
	while (i < n)
	{
		if (c1[i] != c2[i])
		{
			return (c1[i] - c2[i]);
		}
		i++;
		
	}
	return (0);
}
