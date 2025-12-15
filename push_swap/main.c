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

int main(int argc, char **argv)
{
    t_stack_node    *a;
    t_stack_node    *b;

    a = NULL;
    b = NULL;
    if(1 == argc || (2 == argc && !argv[1][0]))
        return (0);
    else if(2 == argc)
        argv = ft_split(argv[1],' ');
    stack_init(&a, argv + 1, 2 == argc);
    if(!stack_sorted(a))
    {
        if(stack_len(a) == 2)
            sa(&a, false);
        else if (stack_len(a) == 3)
            tiny_sort(&a);
        else
            push_swap(&a, &b);
     
    }
}

