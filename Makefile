CC=gcc
CFLAGS?=-Wall -Wno-unused-result -march=haswell -Isrc/include -std=c99 -fopenmp -O3

# source code
SRC=layers.c network.c volume.c

# object files
BASELINE_OBJ=$(SRC:%.c=src/baseline/%.o)
OPTIMIZED_OBJ=$(SRC:%.c=src/optimized/%.o)
OBJ=$(BASELINE_OBJ) $(OPTIMIZED_OBJ) src/benchmark.o

optimized: src/benchmark.o $(OPTIMIZED_OBJ)
	$(CC) $(CFLAGS) -o optimized $^ -lm

baseline: src/benchmark.o $(BASELINE_OBJ)
	$(CC) $(CFLAGS) -o baseline $^ -lm

$(OBJ): %.o : %.c
	$(CC) $(CFLAGS) -o $@ -c $<

clean:
	rm -f $(OBJ)
	rm -f baseline
	rm -f optimized

.PHONY: clean compare
