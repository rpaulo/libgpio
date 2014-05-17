LIB=	gpio
SHLIB_MAJOR=1
SRCS=	gpio.c
INCS=	libgpio.h

CFLAGS += -I${.CURDIR}

WARNS?=	3

#MAN=	libgpio.3

#MLINKS+= \
#	libgpio.3 gpio_open.3 \

.include <bsd.lib.mk>
