gen:
	grep GPIO_PIN /usr/include/sys/gpio.h | \
		awk '{ print "   ", tolower($$2), "=", $$3 }' | \
		sed -e 's/gpio_//'

all: gen

.PHONY: gen 

.include <bsd.own.mk>
