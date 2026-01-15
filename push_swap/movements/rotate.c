/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/11 23:36:43 by gortiz-j          #+#    #+#             */
/*   Updated: 2026/01/11 23:36:43 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/* The top element of the stack is sent to the bottom. */

static void	rotate(t_stack **stack)
{
	t_stack	*tmp;
	t_stack	*tail;

	tmp = *stack;
	*stack = (*stack)->next;
	tail = get_bottom(*stack);
	tmp->next = NULL;
	tail->next = tmp;
}

/*	Sends the top element of stack a to the bottom. 
	Prints "ra" to the standard output */

void	do_ra(t_stack **stack_a)
{
	rotate(stack_a);
	ft_putstr("ra\n");
}

/*	Sends the top element of stack b to the bottom.
	Prints "rb" to the standard output. */

void	do_rb(t_stack **stack_b)
{
	rotate(stack_b);
	ft_putstr("rb\n");
}

/* Sends the top element of both stack a and stack b to the bottom
	of their stacks. Prints "rr" to the standard output. */

void	do_rr(t_stack **stack_a, t_stack **stack_b)
{
	rotate(stack_a);
	rotate(stack_b);
	ft_putstr("rr\n");
}
