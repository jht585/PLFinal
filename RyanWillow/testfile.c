print HelloWorld;
var a;          //variable instantiation allocates storage space in the VariableMap
print a;        //access variable
var c = 5;      //instantiate and assign
print c;

// ifelse uses boolean operator and includes variable reassignment and math operator with assignment
if (5 == '5') {
    a = 5 * 5;
    print a;
} else {
    a = 5 + 5;
    print a;
}

5 - 3;       // math operator without assignment sends output to console

def fun() {
    print 'z';
    5 + 5;
}

var b = (float) a;
print b;
var c = (float) 'a';
print c;
var d = (float) 5;
print d;

fun();