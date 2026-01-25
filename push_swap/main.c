/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/14 17:17:17 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/12/14 17:17:17 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/* Frees a split array created by ft_split */
void	free_split(char **param)
{
	int	i;

	if (!param)
		return ;
	i = 0;
	while (param[i])
	{
		free(param[i]);
		i++;
	}
	free(param);
}

/* Returns 1 if the stack is sorted, 0 otherwise */
int	is_sorted(t_stack *stack)
{
	while (stack->next != NULL)
	{
		if (stack->value > stack->next->value)
			return (0);
		stack = stack->next;
	}
	return (1);
}

/* Chooses the sorting method based on stack size */
static void	push_swap(t_stack **stack_a, t_stack **stack_b, int size)
{
	if (size == 2 && !is_sorted(*stack_a))
		do_sa(stack_a);
	else if (size == 3)
		sort_three(stack_a);
	else if (size > 3 && !is_sorted(*stack_a))
		sort(stack_a, stack_b);
}

/* Splits input, validates numbers, converts and pushes them to stack_a */
void	get_numbers(char *av, t_stack **stack_a)
{
	char		**param;
	long int	n;
	int			i;

	param = ft_split(av, ' ');
	if (!param)
		error_exit(stack_a, NULL);
	i = 0;
	while (param[i])
	{
		if (!input_is_correct(param[i]))
		{
			free_split(param);
			error_exit(stack_a, NULL);
		}
		n = ft_atoi(param[i]);
		if (n > INT_MAX || n < INT_MIN)
		{
			free_split(param);
			error_exit(stack_a, NULL);
		}
		stack_add(stack_a, stack_new(n));
		free(param[i]);
		i++;
	}
	free(param);
}

/* Initializes stacks, validates input, sorts and frees everything */
int	main(int ac, char **av)
{
	t_stack *stack_a;
	t_stack *stack_b;
	int     size;
	int     i;

	i = 1;
	stack_a = NULL;
	stack_b = NULL;
	while (i < ac)
	{
		get_numbers(av[i], &stack_a);
		i++;
	}
	if (is_duplicate(stack_a))
		error_exit(&stack_a, NULL);
	size = get_stack_size(stack_a);
	get_index(stack_a, size + 1);
	push_swap(&stack_a, &stack_b, size);
	free_stack(&stack_a);
	free_stack(&stack_b);
	return (0);
}
