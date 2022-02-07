/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef {

	static BigInteger factorial(int n) {
		BigInteger res = BigInteger.valueOf(1);
		for (int i = 2; i <= n; i++) {
			res = res.add(res.multiply(BigInteger.valueOf(i)));
		}
		return res;
	}

	static BigInteger nCr(int n, int r) {
		BigInteger res;
		res = factorial(n).divide(factorial(r).multiply(factorial(n - r)));

		return res;
	}

	public static void main(String[] args) throws java.lang.Exception {

		System.out.println(nCr(2,1));

		Scanner input = new Scanner(System.in);
		int t = Integer.parseInt(input.nextLine());

		BigInteger mod = BigDecimal.valueOf(1e9 + 7).toBigInteger();

		for (int i = 0; i < t; i++) {
			int n = Integer.parseInt(input.nextLine());

			BigInteger ans = BigDecimal.valueOf(0).toBigInteger();
			for (int j = 1; j <= n; j++) {
				double up = Math.pow(-1, j);
				BigInteger a = BigDecimal.valueOf(up).toBigInteger();
				System.out.println(a);
				a = a.multiply(nCr(n, j));
				System.out.println("ncr:");
				System.out.println(a);
				BigInteger b = BigDecimal.valueOf(1 - Math.pow(1/2, j)).toBigInteger().modInverse(mod);
				System.out.println(b);
				ans = ans.add(a.multiply(b));
			}
			ans = ans.negate();
			ans = ans.mod(mod);

			System.out.println(ans);
		}
		input.close();
	}
}
