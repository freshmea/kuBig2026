package com.example;

public class HelloService {
    private final String name;

    public HelloService(String name) {
        this.name = name;
    }

    public String greet() {
        return "hello, " + name + " from Java!";
    }

    public static int add(int left, int right) {
        return left + right;
    }
}
