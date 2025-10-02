typedef unsigned long size_t;

char *strdup(const char *s)
{
	size_t i;
	char *copy;
	size_t len;

	len = 0;
	i = 0;
	while (s[len])
		len++;
	copy = (char *)malloc(len + 1);
	if (!copy)
		return (0);
	while (i < len)
	{
		copy[i] = s[i];
		i++;
	}
	copy[len] = '\0';
	return (copy);
}
