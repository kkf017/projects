package src.model;

import java.io.*;



public class Person {
	private String firstname;
	private String lastname;
	
	public Person(){}
	
	public Person(String firstname, String lastname){
		this.firstname = firstname;
		this.lastname = lastname;
	}
	
	public String sayHello(){
		return "Hello, I am "+firstname+" "+lastname+".";
	}
    
}
