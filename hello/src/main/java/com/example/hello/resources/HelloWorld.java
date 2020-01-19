package com.example.hello.resources;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping("/hello")
public class HelloWorld {

    @RequestMapping("/{name}")
    public String getHelloWorld(@PathVariable("name") String name){
        return "hello " + name;
    }
}
