/*Author: Otumian Empire
*Purpose: To convert year to month
*Purpose after modification: to take input from the user and display it in a form of intelligent timer
*can someone also modify this code: Yes
*/

//this code runs well on a pc
//well, let me know any way i can improve this code..

#include <iostream>
using namespace std;

//created a class 
class WhatSaysTheTime {

//constructor
    WhatSaysTheTime (){
    cout <<"The program has started" <<endl;
    cout <<"what says the time" <<endl;
    }

//destructor
    ~WhatSaysTheTime(){
        cout <<"The program has ended" <<endl;
    }
    
    //i realised that there'd be an error so i decided to make the implementatiin down here a function
   void HelloTime() {
    //time variables
    int second, minutes, hour, day, week, month, year, centry;
    
    second = minutes = hour = day = week = month = year = centry = 0;
    
    cout <<"Enter the number of second: " <<endl;
    cin >> second ;
    
    cout <<"Enter the number of minutes: " <<endl;
    cin >> minutes ;
    
    cout <<"Enter the number of hour: " <<endl;
    cin >> hour ;
    
    cout <<"Enter the number of day: " <<endl;
    cin >> day ;
    
    cout <<"Enter the number of week: " <<endl;
    cin >> week ;
    
    cout <<"Enter the number of month: " <<endl;
    cin >> month ;
    
    cout <<"Enter the number of year: " <<endl;
    cin >> year ;
    
    cout <<"Enter the number of centry: " <<endl;
    cin >> centry ;
    
    
    if (second > 59){
        while (second > 59){
            second -= 60;
            minutes += 1;
        }
    }
    
    if (minutes  > 59){
        while (minutes  > 59){
            minutes -= 60;
            hour += 1;
        }
    }
    
    if (hour > 23){
        while (hour > 23){
            hour -= 24;
            day += 1;
        }
    }
    
    if (day > 6){
        while (day > 6){
            day -= 7;
            week += 1;
        }
    }
    
    if (week > 3){
        while (week > 3){
            week -= 4;
            month += 1;
        }
    }
    
    if (month > 11){
        while (month > 11){
            month -= 12;
            year += 1;
        }
    }
    
    if (year > 99){
        while (year > 99){
            year -= 100;
            centry += 1;
        }
    }
    
    cout << "Time: " << centry <<":" << year <<":" << month <<":" << week << ":" << day << ":" << hour <<":" << minutes << ":" << second <<endl;
    }
};


int main() {
    
    WhatSaysTheTime SayTime;
    
    SayTime.HelloTime ();
    
    
    return 0;
}

