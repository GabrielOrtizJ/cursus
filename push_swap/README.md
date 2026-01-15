<h1 align="center">
	Push swap
</h1>

*_This project has been created as part of the 42 curriculum by gortiz-j_*

---


It is a simple algorithm project from 42 in which the goal is to output, through standard output, a series of instructions to sort the received numbers in stack A from smallest to largest. The main objective is to achieve this using the smallest possible number of actions. The numbers may be positive or negative, but never duplicated. Stack B must start empty. There is a maximum number of allowed actions for each case:

Sorting 3 values: no more than 3 actions.
Sorting 5 values: no more than 12 actions.

Sorting 100 values (scoring based on the number of moves):

•	5 points for fewer than 700 actions.
•	4 points for fewer than 900 actions.
•	3 points for fewer than 1,100 actions.
•	2 points for fewer than 1,300 actions.
•	1 point for fewer than 1,500 actions.

Sorting 500 values (scoring based on the number of moves):

•	5 points for fewer than 5,500 actions.
•	4 points for fewer than 7,000 actions.
•	3 points for fewer than 8,500 actions.
•	2 points for fewer than 10,000 actions.
•	1 point for fewer than 11,500 actions.

#### 	FUNCTIONS PER FILE

	•	COST: cost, cheapest_move.

	•	DO_MOVE: reverse_both, rotate_both, rotate_a, rotate_b
		do_move.

	•	MAIN: push_swap, get_numbers, main.

	•	POSITION: get_position, get target, position_lowest_index
		get_target position.

	•	PUSH: push, do_pa, do_pb.

	•	ROTATE: rotate, do_ra, do_rb, do_rr.

	•	REVERSE_ROTATE: rev_rotate, do_rra, do_rrb, do_rrr.

	•	SORT THREE: biggest_index, sort_three.
+
	•	SORT: push_init, sort_stack, sort.

	•	SPLIT: ft_strlen, countwords, word_dup, ft_cpy, ft_split.

	•	STACK: stack_new, stack_add, get_bottom, before_bottom ,
		get_stack_size.

	•	START: input_is_correct, is_duplicate, get_index.

	•	SWAP: swap, do_sa, do_sb, do_ss.

	•	UTILS: free_stack, error_exit, ft_atoi, ft_putstr, abs.

####	MOVEMENTS TO BE PERFORMED

	•	sa: swap a – swaps the first two elements at the top of stack a. Does 		nothingif 	there are one or zero elements.

	•sb: swap b – swaps the first two elements at the top of stack b. Does nothing if there are one or zero elements.

	•	ss: swap a and swap b at the same time.

	•	pa: push a – takes the first element at the top of stack b and places it on top of stack a. Does nothing if b is empty.

	•	pb: push b – takes the first element at the top of stack a and places it on top
	of stack b. Does nothing if a is empty.

	•	ra: rotate a – shifts all elements of stack a up by one position, so the first element becomes the last.

	•	rb: rotate b – shifts all elements of stack b up by one position, so the first element becomes the last.

	•	rr: rotate a and rotate b – shifts all elements of both stacks up by one position at the same time, so the first element becomes the last.

	•	rra: reverse rotate a – shifts all elements of stack a down by one position, so the last element becomes the first.

	•	rrb: reverse rotate b – shifts all elements of stack b down by one position, so the last element becomes the first.

	•	rrr: reverse rotate a and reverse rotate b – shifts all elements of both stacks down by one position at the same time, so the last element becomes the first.

####	APPROACH AND ALGORITHM

	The project is implemented using linked lists. In each node, we will store 6 values ​​that will allow us to calculate the most efficient move to sort our stack. This project allows us to achieve the highest score and perform the correction in fewer moves than the maximum score. Furthermore, it will allow us to accept arguments as a string, mixed strings, or only numbers.

# Instructions
`make`: first we need to copile our push_swap.  
`make clean`: deletes all ***.o** created by **make**.  
`make fclean`: executes **make clean** and deletes **push_swap** program.  
`make re`: executes **make fclean** and compiles the program again.  
`./push_swap <numbers>`: push_swap program will be executed using the numbers given and only show the moves made to sort them. It will only accept numbers, an error message will be shown otherwise. Also, the numbers must not repeat and be between the **INT.LIMITS**, if not the error message will appear.  
`./push_swap <numbers> | wc -l`: will only show the number of moves made.

# Resources

While working on this project, I watched a couple of videos to better understand it, which were helpful in getting started. [helpful video](https://www.youtube.com/watch?v=OaG81sDEpVk) [helpful video](https://www.youtube.com/watch?v=wRvipSG4Mmk)

When starting this task, it's a good idea to use an online visualizer for push_swap; it's very helpful to be able to see what you're doing and every move the program makes.[PushSwap Visualizer](https://push-swap42-visualizer.vercel.app/) [PushSwap Visualizer](https://push.eliotlucas.ch/) it's really intuitive.

**_NO AI WAS USED FOR THIS PROJECT_**