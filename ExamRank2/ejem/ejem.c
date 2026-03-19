#include <unistd.h>
int	ft_atoi(char *str)
{
	int res = 0;
	int i = 0;
	while (str[i])
	{
		res = res * 10 + str[i] - '0';
		i++;
		write(1, "\n", 1);

	}
	return (res);
}

void	print_hex(int n)
{
	char hex_digits[] = "0123456789";

	if (n >= 10)
		print_hex(n / 10);
	write(1, &hex_digits[n % 16], 1);
}


int	main(int argc, char **argv)
{
	if (argc == 2)
		print_hex(ft_atoi(argv[1]));
	write(1, "\n", 1);
}