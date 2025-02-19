#ifndef EXAMPLE_TEST_HPP
#define EXAMPLE_TEST_HPP

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


class test {
private:
    int16_t test;
    int16_t vasya;
public:
    test();
    ~test();

    void serialize(char* buffer) const;
    void deserialize(const char* buffer);

    int16_t get_test();
    void set_test(int16_t value);
    int16_t get_vasya();
    void set_vasya(int16_t value);

    void example_function3(int16_t arg1, float arg2);
    void example_function4(int16_t arg1, float arg2);
};


class test2 {
private:
    int16_t test;
    int16_t vasya;
public:
    test2();
    ~test2();

    void serialize(char* buffer) const;
    void deserialize(const char* buffer);

    int16_t get_test();
    void set_test(int16_t value);
    int16_t get_vasya();
    void set_vasya(int16_t value);

    void example_function(int16_t arg1, float arg2);
};


#endif // EXAMPLE_TEST_HPP