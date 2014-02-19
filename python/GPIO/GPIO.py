#!/usr/bin/env python 
#
# Copyright (c) 2014 Rui Paulo <rpaulo@felyko.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from ctypes import *

class GPIOConfig(Structure):
    _fields_ = [("pin", c_uint),
                ("name", c_char * 64),
                ("caps", c_uint),
                ("flags", c_uint)]

class GPIO:
    def __init__(self, dev=0):
        self.lib = CDLL('libgpio.so')
        self.handle = self.lib.gpio_open(dev)
        if self.handle == -1:
            raise IOError

    def pin_list(self):
        gcp = POINTER(GPIOConfig)
        pins = self.lib.gpio_pin_list(self.handle, byref(gcp))
        if pins > 0:
            da = []
            for i in range(0, pins):
                d = { 'pin': gcp[i].pin,
                      'name': gcp[i].name,
                      'caps': gcp[i].caps,
                      'flags': gcp[i].flags }
                da.append(d)
            return da
        else:
            return OSError

    def pin_config(self, pin):
        gc = GPIOConfig()
        gc.pin = pin
        if self.lib.gpio_pin_config(self.handle, byref(gc)) == 0:
            return gc.config
        else:
            raise OSError
   
    def pin_set_flags(self, pin, flags):
        gc = GPIOConfig()
        gc.pin = pin
        gc.flags = flags
        if self.lib.gpio_pin_set_flags(self.handle, byref(gc)) != 0:
            raise OSError

    def pin_get(self, pin):
        return self.lib.gpio_pin_get(self.handle, pin)

    def pin_set(self, pin, value):
        if self.lib.gpio_pin_set(self.handle, pin, value) != 0:
            raise OSError

    def pin_toggle(self, pin):
        if self.lib.gpio_pin_toggle(self.handle, pin) != 0:
            raise OSError

    def pin_low(self, pin):
        if self.lib.gpio_pin_low(self.handle, pin) != 0:
            raise OSError

    def pin_high(self, pin):
        if self.lib.gpio_pin_high(self.handle, pin) != 0:
            raise OSError

    def pin_input(self, pin):
        if self.lib.gpio_pin_input(self.handle, pin) != 0:
            raise OSError

    def pin_output(self, pin):
        if self.lib.gpio_pin_output(self.handle, pin) != 0:
            raise OSError

    def pin_opendrain(self, pin):
        if self.lib.gpio_pin_opendrain(self.handle, pin) != 0:
            raise OSError

    def pin_pushpull(self, pin):
        if self.lib.gpio_pin_pushpull(self.handle, pin) != 0:
            raise OSError

    def pin_tristate(self, pin):
        if self.lib.gpio_pin_tristate(self.handle, pin) != 0:
            raise OSError

    def pin_pullup(self, pin):
        if self.lib.gpio_pin_pullup(self.handle, pin) != 0:
            raise OSError

    def pin_pulldown(self, pin):
        if self.lib.gpio_pin_pulldown(self.handle, pin) != 0:
            raise OSError

    def pin_invin(self, pin):
        if self.lib.gpio_pin_invin(self.handle, pin) != 0:
            raise OSError

    def pin_invout(self, pin):
        if self.lib.gpio_pin_invout(self.handle, pin) != 0:
            raise OSError

    def pin_pulsate(self, pin):
        if self.lib.gpio_pin_pulsate(self.handle, pin) != 0:
            raise OSError

    # Pin definitions from /usr/include/sys/gpio.h
    pin_low = 0x00
    pin_high = 0x01
    pin_input = 0x0001
    pin_output = 0x0002
    pin_opendrain = 0x0004
    pin_pushpull = 0x0008
    pin_tristate = 0x0010
    pin_pullup = 0x0020
    pin_pulldown = 0x0040
    pin_invin = 0x0080
    pin_invout = 0x0100
    pin_pulsate = 0x0200

if __name__ == "__main__":
    g = GPIO()
    print g.pin_list()
