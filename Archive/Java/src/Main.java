package src;
import src.model.*;

import java.io.*;


// https://www.baeldung.com/java-compile-multiple-files
//javac -classpath libs/*:. -d target -sourcepath . service/CarService.java model/*.java



// https://medium.com/@hrutiksurwade/build-your-first-rest-api-using-java-spring-boot-hello-world-670faefc2aea
// https://medium.com/javajams/creating-a-rest-api-in-spring-boot-68ce785f652f


public class Main {
    public static void main(String argv[]) {
    
    	Person user = new Person("Charlie","XC");
    	String msg = user.sayHello();
    	
        System.out.println(msg);
    }
}
