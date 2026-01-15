/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/14 17:06:00 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/12/14 17:06:00 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/*	Pushes the top element of src stack to the top of dest stack. DISTINTO*/
/*tmp = *src;
	tmp->next = *dst;
	*dst = tmp;
	*src = (*src)->next;*/
static void	push(t_stack **src, t_stack **dst)
{
	t_stack	*tmp;

	if (*src == NULL)
		return ;
	tmp = (*src)->next;
	(*src)->next = *dst;
	*dst = *src;
	*src = tmp;
}

/*	Pushes the top element of stack b to the top of stack a.
	Prints "pa" to the standard output. */

void	do_pa(t_stack **stack_a, t_stack **stack_b)
{
	push(stack_b, stack_a);
	ft_putstr("pa\n");
}

/*	Pushes the top element of stack a to the top of stack b.
	Prints "pb" to the standard output. */

void	do_pb(t_stack **stack_a, t_stack **stack_b)
{
	push(stack_a, stack_b);
	ft_putstr("pb\n");
}
