import java.util.*;

public class PasswordGenerator 
{
	public static void main(String[] args) 
	{		
		Scanner sc = new Scanner(System.in);
		int length = sc.nextInt();
		if(length > 0) {
		    System.out.print("Generated Password: ");
		    System.out.print(generatePassword(length));
		}
		else {
		    System.out.println("Enter valid password length");
		}
	}
	public static char[] generatePassword(int length)
	{
		String upr_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		String lwr_chars = "abcdefghijklmnopqrstuvwxyz";
		String numbers = "0123456789";
		String spl_chars ="!@#$&*_";
		String pattern = upr_chars + lwr_chars + numbers + spl_chars;
		Random generate = new Random();
		char[] password = new char[length];
		for (int i = 0; i < password.length; i++)  {
		     password[i] = pattern.charAt(generate.nextInt(pattern.length()));
		}
		return password;
	}
}
