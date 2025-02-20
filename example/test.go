// Generated Go code

package main

const MAX_BUFFER_SIZE = 1024

type Status int
const (
    OK Status = 0
    ERROR = 1
    INPROGRESS = 2
    TEST = 10
    TEST2 = 11
)

type test struct {
    id int16;
    value int16;
    array [10]int16;
}

func test_example_function3(self test, arg1 int16, arg2 float32) {

}
func test_example_function4(self test, arg1 int16, arg2 float32) {

}


type system struct {
    id int16;
    voltage0 int16;
    voltage1 int16;
    voltage2 int16;
}

func system_example_function(self system, arg1 int16, arg2 float32) {

}


func example_function1(self system, arg1 int16, arg2 float32) {

}
func example_function2(self system, arg1 int16, arg2 float32) {

}


