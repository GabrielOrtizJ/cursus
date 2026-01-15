# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gortiz-j <gortiz-j@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/05 12:45:10 by gortiz-j          #+#    #+#              #
#    Updated: 2025/12/05 12:46:11 by gortiz-j         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

SRCS = main.c \
		algorithm/cost.c \
		algorithm/do_moves.c \
		algorithm/position.c \
		algorithm/sort_three.c \
		algorithm/sort.c \
		movements/push.c \
		movements/reverse_rotate.c \
		movements/rotate.c \
		movements/stack.c \
		movements/swap.c \
		utils/start.c \
		utils/split.c \
		utils/utils.c

OBJS = $(SRCS:.c=.o)
DEPS = $(OBJS:.o=.d)

CC = gcc
CFLAGS = -Wall -Wextra -Werror -I.

RM = rm -f

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(OBJS) -o $(NAME)
	@echo "Created $(NAME)"

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS) $(DEPS)
	@echo "Object files removed"

fclean: clean
	$(RM) $(NAME)
	@echo "Executable removed"

re: fclean all

.PHONY: all clean fclean re
