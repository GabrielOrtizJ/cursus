typedef unsigned long size_t;

void menset(void *str, int byte, size_t c)
{
	unsigned char *ptr = (unsigned char *)str;
	while (c--)
		*ptr++ = (unsigned char)byte;
}
