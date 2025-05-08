package src;
import src.Model.User.*;

import java.io.*;



//javac -d compiled $(find src -name *.java)
// https://www.baeldung.com/java-compile-multiple-files



javac -classpath libs/*:. -d target -sourcepath . service/CarService.java model/*.java


public class Main {
    public static void main(String argv[]) {
    
    	User user = new User("Charlie","XC");
    	String msg = User.sayHello();
    	
        System.out.println(msg);
    }
}
