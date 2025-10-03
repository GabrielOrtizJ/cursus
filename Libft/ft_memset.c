typedef unsigned long size_t;

void ft_menset(void *str, int byte, size_t c)
{
	unsigned char *ptr = (unsigned char *)str;
	while (c--)
		*ptr++ = (unsigned char)byte;
}
