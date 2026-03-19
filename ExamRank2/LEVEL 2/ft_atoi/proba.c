#include <stdio.h>

int	ft_atoi(const char *str)
{
	int result = 0;
	int sign = 1;
	int i = 0;

	while(str[i]<=32)
		i++;
	if(str[i]== '-')
		sign = -1;
	if(str[i] == '+' || str[i]== '+')
		i++;
	while (str[i] >= "0" && str[i] <= "9")
	{
		result = result * 10 + str[i] - '0';
		i++;
	}
	return (result * sign);
	
};

int main()
{
	printf("%d", ft_atoi("-123"));
}