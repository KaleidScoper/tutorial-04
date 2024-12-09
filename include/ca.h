#ifndef CA_H
#define CA_H

#include <iostream>
#include <string>
#include "miracl.h"

class CA {
public:
    big SK_CA;   // CA's private key
    epoint *PK_CA;  // CA's public key

    CA();
    ~CA();
    void init();  // Initialize CA (generate keys)
    void registerProver(epoint *PK_P, big SK_P, signature &sigma);
    void issueAIK(epoint *PK_AI, signature &sigma_AIK);
};

#endif
