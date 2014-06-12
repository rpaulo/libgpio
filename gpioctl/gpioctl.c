/*-
 * Copyright (c) 2014 Rui Paulo <rpaulo@felyko.com>
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
 * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <err.h>
#include <sysexits.h>

#include <sys/ioctl.h>
#include <sys/types.h>

#include <libgpio.h>

static void
usage(void)
{
	errx(EX_USAGE,"usage: gpioctl [-f ctldev] [-v] [-t pin] [-c pin flag]");
}

int
main(int argc, char **argv)
{
	char c;
	gpio_handle_t handle;
	int toggle, verbose, list, config;
	char *ctlfile;
	int i, j;

	ctlfile = NULL;
	toggle = verbose = config = list = 0;
	while ((c = getopt(argc, argv, "c:f:lt:v")) != -1) {
		switch (c) {
		case 'c':
			config = 1;
			break;
		case 'f':
			ctlfile = optarg;
			break;
		case 'l':
			list = 1;
			break;
		case 't':
			toggle = 1;
			break;
		case 'v':
			verbose = 1;
			break;
		default:
			usage();
			break;
		}
	}
	argv += optind;
	argc -= optind;

	if (list && (config || toggle))
		errx(EX_USAGE, 
		    "-l is mutually exclusive with PIN configuration");
	if (ctlfile == NULL)
		handle = gpio_open(0);
	else
		handle = gpio_open_device(ctlfile);
	if (handle == GPIO_INVALID_HANDLE)
		err(EX_IOERR, "could not open the GPIO device");

	if (list) {
		for (i = 0; i < 20; i++)
			for (j = 0; j < 10; j++) {
			}
	
	}

	return (EXIT_SUCCESS);
}
