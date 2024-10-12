#include "include/header.h"

int main(int argc, char* argv[]) {

    std::string uc_arg[4];
    std::stringstream ts_arg[4];

    for (int i = 0; i < 4; i++) {
        ts_arg[i] << argv[i];
        ts_arg[i] >> uc_arg[i];
    }

    switch(t_check(uc_arg[1])) {
        case 0:
            std::cout << "unknown type" << std::endl;
            return 0;
            break;
        case 1:
            level(uc_arg[2]);
            break;
        case 2:

            break;
        case 3:

            break;
    }

    return 0;

}