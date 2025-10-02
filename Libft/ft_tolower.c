char ft_tolower(char c)
{
	if(c >= 'A' && c <= 'Z')
	{
		c = c + ('a' - 'A');
	}
	return (c);
}
