char ft_toupper(char c)
{
	if(c >= 'a' && c <= 'z')
	{
		c = c - ('a' - 'A');
	}
	return (c);
}
