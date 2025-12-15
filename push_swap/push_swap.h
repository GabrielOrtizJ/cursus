/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gortiz-j <gortiz-j@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/14 17:45:20 by gortiz-j          #+#    #+#             */
/*   Updated: 2025/12/14 17:45:20 by gortiz-j         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <limits.h>
# include <stdbool.h> 
# include <unistd.h>

typedef struct s_stack_node
{
int					value;
int					current_position;
int					final_index;
int					push_price;
bool				above_median;
bool				cheapest;
struct s_stack_node *target_node;
struct s_stack_node *next;
struct s_stack_node *prev;
}			t_stack_node;
#endif