#ifndef EXAMPLE_TEST_HPP
#define EXAMPLE_TEST_HPP

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


class test {
private:
    struct Struct {
       int16_t id;
       int16_t value;
    };
public:
    test();
    ~test();

    void serialize(char* buffer, int buffer_size);
    void deserialize(const char* buffer, int buffer_size);

    int16_t get_id();
    void set_id(int16_t value);
    int16_t get_value();
    void set_value(int16_t value);

    void example_function3(int16_t arg1, float arg2);
    void example_function4(int16_t arg1, float arg2);
};


class system {
private:
    struct Struct {
       int16_t id;
       int16_t voltage0;
       int16_t voltage1;
       int16_t voltage2;
    };
public:
    system();
    ~system();

    void serialize(char* buffer, int buffer_size);
    void deserialize(const char* buffer, int buffer_size);

    int16_t get_id();
    void set_id(int16_t value);
    int16_t get_voltage0();
    void set_voltage0(int16_t value);
    int16_t get_voltage1();
    void set_voltage1(int16_t value);
    int16_t get_voltage2();
    void set_voltage2(int16_t value);

    void example_function(int16_t arg1, float arg2);
};


#endif // EXAMPLE_TEST_HPP