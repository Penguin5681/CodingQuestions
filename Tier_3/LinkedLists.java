package Tier_3;
import java.util.LinkedList;

public class LinkedLists {
    
    public static void main(String[] args) {
        LinkedList<Integer> myList = new LinkedList<>();

        for (int i = 0; i < 11; i++) {
            myList.addFirst(i);
        }

        for (Integer ls : myList) {
            System.out.println(ls);
        }
    }
}
