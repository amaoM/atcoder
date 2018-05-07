import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    String[] item = {s.substring(1), s.substring(0, 1), s.substring(0, 1)};
    ArrayList<String[]> q = new ArrayList<String[]>();
    q.add(item);
    while (true) {
      String[] it = q.remove(q.size() - 1);
      String ss = it[0];
      int v = Integer.parseInt(it[1]);
      String f = it[2];
      if (ss.length() > 0) {
        int l = Integer.parseInt(ss.substring(0, 1));
        String[] i = {ss.substring(1), String.valueOf(v + l), String.format("%s+%s", f, l)};
        String[] ii = {ss.substring(1), String.valueOf(v - l), String.format("%s-%s", f, l)};
        q.add(i);
        q.add(ii);
      } else if (v == 7) {
        System.out.println(String.format("%s=7", f));
        break;
      }
    }
  }
}
