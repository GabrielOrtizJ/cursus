typedef unsigned long size_t;

char *ft_substr(char const *s, unsigned int start, size_t len)
{
    char *substr;
    int i;

    substr = (char *)malloc(len + 1);
    if (!substr)
        return 0;

    i = 0;
    while (i < len && s[start + i] != '\0')
    {
        substr[i] = s[start + i];
        i++;
    } 
    substr[i] = '\0';
    return substr;
}

