typedef unsigned char size_t;

void *ft_memmove(void *dest, const void *src, size_t count)
{

}
typedef unsigned long size_t;

void *memmove(void *dest, const void *src, size_t n)
{
	unsigned char *d = (unsigned char *)dest;        
	const unsigned char *s = (const unsigned char *)src;

	if (d == s || n == 0)
		return dest;

	if (d < s) {
		while (n--)
			*d++ = *s++;
	} else {
		d += n;
		s += n;
		while (n--)
			*(--d) = *(--s);
	}
	return dest;
}
