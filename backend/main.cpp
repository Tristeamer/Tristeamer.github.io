//website manager.cpp 
//by Tristeamer

#include <iostream>
#include <fstream>
#include <windows.h>
#include <cstdio>
using namespace std;

string name = "< \033[0;34mWebsite\033[0m >: ";
string red = "\033[0;31m";
string green = "\033[0;32m";
string rst = "\033[0m";
string menuopt;
ifstream mtmode;
bool mainmenu = false;
bool maintenance;
bool yn;

void opt1() {

    char mtnameold [] = "index.html";
    char mtnamenew [] = "maintenance.html";
    char mtnametemp [] = "temp.html";

    if (maintenance == true) {

        rename(mtnameold , mtnamenew);
        rename(mtnametemp , mtnameold);

    } else if (maintenance == false) {

        rename(mtnameold , mtnametemp);
        rename(mtnamenew , mtnameold);

    }

    mainmenu=true;

}


menu () {

    while (mainmenu == true) {

        system("CLS");

        mtmode.open("temp.html");

        if (mtmode) {

            maintenance = true;
            mtmode.close();

        } else {

            maintenance = false;

        }


        cout << name << "Main Menu, please select an option (or type 'Q' to exit):" << endl;

        if (maintenance == false) {

            cout << "1) Toggle maintenance mode " << "[" << green << "DISABLED" << rst << "]" << endl;
        
        } else if (maintenance == true) {

            cout << "1) Toggle maintenance mode " << "[" << red << "ENABLED" << rst << "]" << endl;

        }

        cout << "=> ";
    
        cin >> menuopt;
    
        if (menuopt == "1"){

            mainmenu = false;

            cout << name << "Do you really want to toggle maintenance mode? (Y/n):" << endl;
            
            yn = true;
            while (yn == true){

                cout << "=> ";

                string ync1;
                cin >> ync1;

                if (ync1 == "N" || ync1 == "n"){

                    mainmenu = true;
                    yn = false;
                    system("CLS");

                } else if (ync1 == "Y" || ync1 == "y") {

                    yn = false;
                    opt1();

                } else {

                    cout << name << red << "ERROR: invalid option, please try again." << rst << endl;

                }

            }

        } else if (menuopt == "q" || menuopt == "Q") {
            
            return 0;

        } else {

            cout << name << red << "ERROR: Unknown option, please try again." << endl;
            Sleep(200);

        }


    }

}


int main(){

    mainmenu = true;
    menu();

}