#include "include/header.h"
#include <string>

int t_check(std::string type_arg) {

    if (type_arg == "level") {
        return 1;
    } else if (type_arg == "player") {
        return 2;
    } else if (type_arg == "reset") {
        return 3;
    } else {
        return 0;
    }

}

int level(std::string act_arg) {

    
}