import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int y = sc.nextInt();
    for (int a = n; a >= 0; a--) {
      for (int b = n - a; b >= 0; b--) {
        int c = n - a - b;
        if (a * 10000 + b * 5000 + c * 1000 == y) {
          System.out.println(String.format("%d %d %d", a, b, c));
          return;
        }
      }
    }
    System.out.println("-1 -1 -1");
  }
}
