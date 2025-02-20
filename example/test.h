#ifndef EXAMPLE_TEST_H
#define EXAMPLE_TEST_H

#include <stdio.h>

#define MAX_BUFFER_SIZE 1024

typedef enum Status {
    OK = 0,
    ERROR,
    INPROGRESS,
    TEST = 10,
    TEST2,
} Status;

void example_function1(int16_t arg1, float arg2);
void example_function2(int16_t arg1, float arg2);


typedef struct test {
    int16_t id;
    int16_t value;
    int16_t array[10];
} test;

int16_t test_get_id(const test* self);
void test_set_id(test* self, int16_t value);
int16_t test_get_value(const test* self);
void test_set_value(test* self, int16_t value);
int16_t test_get_array(const test* self);
void test_set_array(test* self, int16_t value);

void test_example_function3(test self, int16_t arg1, float arg2);
void test_example_function4(test self, int16_t arg1, float arg2);


typedef struct system {
    int16_t id;
    int16_t voltage0;
    int16_t voltage1;
    int16_t voltage2;
} system;

int16_t system_get_id(const system* self);
void system_set_id(system* self, int16_t value);
int16_t system_get_voltage0(const system* self);
void system_set_voltage0(system* self, int16_t value);
int16_t system_get_voltage1(const system* self);
void system_set_voltage1(system* self, int16_t value);
int16_t system_get_voltage2(const system* self);
void system_set_voltage2(system* self, int16_t value);

void system_example_function(system self, int16_t arg1, float arg2);


#endif // EXAMPLE_TEST_H