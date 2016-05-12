
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class streamOp {



    public static List<Object> ops(List<Object> arg) {

        ArrayList<List<Object>> arr = new ArrayList<List<Object>>();
        List<Object> output = new ArrayList<Object>();

        arg.stream().forEach(d -> {output.add(d);} );


        return (output);
    }

    //code for "where" opertation
    public static List<Object> where(List<ArrayList<Object>> arg) {

        List<Object> output = new ArrayList<Object>();


        arg.stream()
                .filter(e -> (Integer) e.get(0) < 40)
                .forEach (e -> {output.add(e);});
                //.forEach(e -> {System.out.println(e.get(0));} );


        return (output);
    }

    //code for "orber by" opertation
    public static List<Object> orderBy(List<ArrayList<Object>> arg) {

        List<Object> output = new ArrayList<Object>();


        arg.stream()
                .sorted((e,a) -> ((Integer)e.get(0)).compareTo((Integer)a.get(0)))
                .forEach (e -> {output.add(e);});
        //.forEach(e -> {System.out.println(e.get(0));} );


        return (output);
    }
}


//(where (list (jArray (list 50 50 50)) (jArray (list 4 5 6)) ))
// (orderby (list (jArray (list 50 50 50)) (jArray (list 4 5 6)) (jArray (list 7 8 9)) ))
// (where (orderby (list (jArray (list 50 50 50))  (jArray (list 7 8 9)) (jArray (list 4 5 6)) )))