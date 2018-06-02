import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    char[] s = sc.next().toCharArray();
    ArrayList<Integer> q = new ArrayList<Integer>();
    ArrayList<Integer> idx = new ArrayList<Integer>();
    q.add(0);
    idx.add(0);
    while (q.size() > 0) {
      int qs = q.remove(q.size() - 1);
      int i = idx.remove(idx.size() - 1);
      if (i >= s.length) {
        break;
      }
      if (s.length > i + 1) {
        if (qs > 9) {
          System.out.println("AAA");
          System.out.println((qs + Integer.parseInt(s[i] + "")) * 10);
          q.add((qs + Integer.parseInt(s[i] + "")) * 10);
        } else {
          System.out.println("BBB");
          System.out.println(qs + Integer.parseInt(s[i] + "") * 10);
          q.add(qs + Integer.parseInt(s[i] + "") * 10);
        }
        idx.add(i + 1);
        System.out.println("CCC");
        System.out.println(qs + Integer.parseInt(s[i] + ""));
        q.add(qs + Integer.parseInt(s[i] + ""));
        idx.add(i + 1);
      }
    }
  }
}
