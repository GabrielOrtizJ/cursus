#ifndef LIBFT_H
# define LIBFT_H

typedef unsigned long size_t;

int ft_atoi(const char *str);
void ft_bzero(void *str, size_t num);
void *ft_calloc(size_t num, size_t size);
int ft_isalnum(int c);
int ft_isalpha(char c);
int ft_isascii(int c);
int ft_isdigit(int c);
int ft_isprint(char c);
void *ft_memchr(void *buf, int c, size_t n);
int ft_memcmp(const void *buf1, const void *buf2, size_t n);
void *ft_memcpy(void *dest, const void *src, size_t n);
void *ft_memmove(void *dest, const void *src, size_t count);
void ft_menset(void *str, int byte, size_t c);
char *ft_strchr(const char *str, int c);
char *ft_strdup(const char *s);
int ft_strlcat(char *dest, const char *src, int size);
int ft_strlen(const char *c);
int ft_strncmp(const char *src, const char *dest, int n);
char *ft_strnstr(const char *s1, const char *s2, size_t n);
char *ft_strrchr(const char *str, int c);
char ft_tolower(char c);
char ft_toupper(char c);

//new ft
char *ft_substr(char const *s, unsigned int start,size_t len);

#endif
