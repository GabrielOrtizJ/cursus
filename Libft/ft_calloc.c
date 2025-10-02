typedef unsigned long size_t;

void *ft_calloc(size_t num, size_t size)
{
    void *ptr;
    unsigned char *p;
    size_t total;
    size_t i;

    total = num * size;
    ptr = malloc(total);
    if (!ptr)
        return 0;

    p = (unsigned char *)ptr;
    i = 0;
    while (i < total)
    {
        p[i] = 0;
        i++;
    }
    return ptr;
}

