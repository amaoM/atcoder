import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    long c = sc.nextLong();
    long[] x = new long[n + 1];
    long[] v = new long[n + 1];
    for (int i = 1; i <= n; i++) {
      x[i] = sc.nextLong();
      v[i] = sc.nextLong();
    }
    long[] a = new long[n + 1];
    long[] aa = new long[n + 1];
    long asum = 0;
    for (int i = 1; i <= n; i++) {
      asum += v[i];
      a[i] = Math.max(a[i - 1], asum - x[i]);
      aa[i] = Math.max(aa[i - 1], asum - x[i] * 2);
      System.out.println(String.format("i: %d, a: %d, aa: %d", i, a[i], aa[i]));
    }
    long[] b = new long[n + 2];
    long[] bb = new long[n + 2];
    long bsum = 0;
    for (int i = n; i > 0; i--) {
      bsum += v[i];
      b[i] = Math.max(b[i - 1], bsum - (c - x[i]));
      bb[i] = Math.max(bb[i - 1], bsum - (c - x[i]) * 2);
      System.out.println(String.format("i: %d, b: %d, bb: %d", i, b[i], bb[i]));
    }
    long res = 0;
    for (int i = n + 1; i > 0; i--) {
      res = Math.max(res, Math.max(a[i - 1] + bb[i], aa[i - 1] + b[i]));
      System.out.println(String.format("i: %d, a: %d, aa: %d, b: %d, bb: %d", i, a[i - 1], aa[i - 1], b[i], bb[i]));
    }
    System.out.println(res);
  }
}
