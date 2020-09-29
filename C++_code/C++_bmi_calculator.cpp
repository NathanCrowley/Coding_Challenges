#include <iostream>
int main(){

  //get user weight in KG
  double weight;
  std::cout << "\tEnter your weight in KG: ";
  std::cin >> weight;

  //get users height in meters
  double height;
  std::cout << "\tEnter your height in meters: ";
  std::cin >> height;

  //bmi formula
  double bmi = weight/(height*height);
  std::cout << "\n\tBMI result: " << bmi <<".\n";
  
  //check against BMI scale and return if user is over/under weight
  if (bmi < 18.5){
  	std::cout << "\n\tYou are UNDER-WEIGHT.\n";
  }else if(bmi > 18.5 and bmi < 25){
  	std::cout << "\n\tYou are Normal weight.\n";
  }else if(bmi >25 and bmi <30){
  	std::cout << "\n\tYou are OVER-WEIGHT.\n";
  }else if(bmi > 30){
  	std::cout << "\n\t\tWho ate the all pies? You fat bastard!!\n";
  }else{
  	std::cout << "ERROR !!!!";
  }
}
