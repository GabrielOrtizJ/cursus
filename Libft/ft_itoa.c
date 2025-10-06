char *ft_itoa(int n)
{
	char *str;
	int temp = n;
	int len = (n <= 0) ? 1 : 0; // Space for '-' sign or '0'

	while (temp) {
		len++;
		temp /= 10;
	}

	str = (char *)malloc(len + 1);
	if (!str)
		return (0);

	str[len] = '\0';
	if (n == 0) {
		str[0] = '0';
		return str;
	}

	int is_negative = (n < 0);
	if (is_negative)
		n = -n;

	while (n) {
		str[--len] = (n % 10) + '0';
		n /= 10;
	}

	if (is_negative)
		str[0] = '-';

	return str;
}
