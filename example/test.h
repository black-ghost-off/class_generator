#ifndef EXAMPLE_TEST_H
#define EXAMPLE_TEST_H

#include <stdio.h>

#define MAX_BUFFER_SIZE 1024

typedef enum Status {
    OK = 0,
    ERROR,
    INPROGRESS,
    TEST = 10,
} Status;

void example_function1(int16_t arg1, float arg2);
void example_function2(int16_t arg1, float arg2);


typedef struct test {
    int16_t test;
    int16_t vasya;
} test;

int16_t test_get_test(const test* self);
void test_set_test(test* self, int16_t value);
int16_t test_get_vasya(const test* self);
void test_set_vasya(test* self, int16_t value);

void test_example_function3(struct test, int16_t arg1, float arg2);
void test_example_function4(struct test, int16_t arg1, float arg2);


typedef struct test2 {
    int16_t test;
    int16_t vasya;
} test2;

int16_t test2_get_test(const test2* self);
void test2_set_test(test2* self, int16_t value);
int16_t test2_get_vasya(const test2* self);
void test2_set_vasya(test2* self, int16_t value);

void test2_example_function(struct test2, int16_t arg1, float arg2);


#endif // EXAMPLE_TEST_H