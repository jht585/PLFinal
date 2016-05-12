import java.util.*;

public class makeObject {

    public static Object jarray(List<Object> arg) {
        List<Object> output = new ArrayList<Object>();

        for (Object item: arg) {
            //System.out.println(item.getClass());
            output.add(item);
        }



        return (output);

    }
}