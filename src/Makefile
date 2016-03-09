.PHONY: default help object executable all clean
CC = gcc

LD = $(CC)

SOURCE_C = $(wildcard *.c)
OBJECTS_C = $(patsubst %.c, %_c.o, $(SOURCE_C))

LIBRARY_SO = libaddarrays.so

default: help

help:
	@echo "\
Options:\n\n\
  make objects:       compiler makes objects for every *.c and *.f90\n\
  make library:       compiler makes shared object\n\
  make all:           build all previous\n\
  make clean:         delete output files\n\
  make help:          display this help"

objects: $(OBJECTS_C)

library: $(LIBRARY_SO)

all: objects library

%_c.o: %.c
	$(CC) -fPIC -c $^ -o $@

%.so: $(OBJECTS_C)
	$(LD) -shared $^ -o $@

clean:
	rm -rfv $(OBJECTS_C) $(LIBRARY_SO) 
