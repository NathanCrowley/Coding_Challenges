/*
function that takes two numbers and an operatora and returns the calculations answer.
	syntax = 2 + 2
			12 - 8
			10 * 2
			100 / 10
	
1) take in string from user (Scanner)
2) split the string to seperate out the numbers from operand (string.split())
3) compare users operand with '+-/*' when it matches run this function
4) return the answer in format '2+2 = 4'
*/


import java.util.*;
class basic_calculator{
	public static void main(String[] args){
		//1)
		Scanner myScanner = new Scanner(System.in);		//create scanner
		System.out.print("Please enter your equation (Syntax: '2 + 2')>>>> ");		
		String user = myScanner.nextLine();				//save input in user String
		//2)
		String[] items = user.split(" ");
		//3)
		String op = items[1];
		char operator = op.charAt(0);
		int x = Integer.parseInt(items[0]);
		int y = Integer.parseInt(items[2]);
		float answer = 0;
		if (operator == '+'){
			//add
			answer = x+y;
		}
		else if (operator == '-'){
			//minus
			answer = x-y;
		}
		else if (operator == '*'){
			//mutliply
			answer = x*y;
		}
		else if (operator == '/'){
			//divide
			answer = x/y;
		}
		System.out.println(user+" = "+answer);
	}
}
