int ft_strncmp(const char *src, const char *dest, int n)
{
    int i = 0;
    while (i < n && (src[i] != '\0' || dest[i] != '\0'))
    {
        if (src[i] != dest[i])
            return ((unsigned char)src[i] - (unsigned char)dest[i]);
        i++;
    }
    return 0;
}
