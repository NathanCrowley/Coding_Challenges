import java.util.*;
//get user to input a string and count the words in this string
class word_count{
	public static void main(String[] args){
		/*	1) create scanner object for string
			2) save users input to variable (user)
			3) split the sentence on spaces
			4) print the length of the String array holding each word
		*/
	//1)
		Scanner myScanner = new Scanner(System.in);
		System.out.print("Please enter a sentence >>> ");
	//2)
		String user = myScanner.nextLine();
	//3)
		String[] words = user.split(" ");
	//4)
		System.out.println(words.length);
	}
}
