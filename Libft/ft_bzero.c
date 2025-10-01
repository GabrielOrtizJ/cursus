typedef unsigned long size_t;

void bzero(void *str, size_t num)
{
	unsigned char *ptr = (unsigned char *)str;
	while (num--)
	{
		*ptr++ = 0;
	}	
}