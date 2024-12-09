#ifndef PROVER_H
#define PROVER_H

#include <iostream>
#include <string>
#include "miracl.h"

class Prover {
public:
    big SK_P;    // Prover's private key
    epoint *PK_P;  // Prover's public key
    epoint *PK_AI; // AIK public key
    signature sigma_AIK; // AIK signature

    Prover();
    ~Prover();
    void registerWithCA(CA &ca);
    void generateAIK();
    signature signReport(report &REP);
};

#endif
