# ATUTOR
 
## PART I: HIGH LEVEL ASSEMBLY

### Lesson 1.1: HELLO, WORLD

    program helloWorld; 
    #include("stdlib.hhf");

    begin helloWorld;
        stdout.put("Hello, World of Assembly Language",nl);
    end helloWorld; 

### Lesson 1.2: VARIABLES

    Program DemoVars; #include("stdlib.hhf");

    static
        InitDemo:       int32 := 5;
        NotInitialized: int32;

    begin DemoVars;
        // Display the value of the pre-initialized variable:
        stdout.put("InitDemo's value is ", InitDemo,nl);

        // Input an integer value from the user and display that value:
        stdout.put("Enter an integer value: ");
        stdin.get(NotInitialized);
        stdout.put("You entered: ",NotInitialized,nl);
    end DemoVars;
