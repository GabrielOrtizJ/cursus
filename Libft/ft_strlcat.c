int ft_strlen(const char *c)
{
    int count = 0;
    while (c[count] != '\0')
        count++;
    return count;
}

int ft_strlcat(char *dest, const char *src, int size)
{
	int dest_len = ft_strlen(dest);
	int src_len = ft_strlen(src);
	int i = 0;

	if (size <= dest_len)
		return size + src_len;

	while (src[i] != '\0' && dest_len + i < size - 1)
	{
		dest[dest_len + i] = src[i];
		i++;
	}
	dest[dest_len + i] = '\0';

	return dest_len + src_len;
}
