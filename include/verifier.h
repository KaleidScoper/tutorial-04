#ifndef VERIFIER_H
#define VERIFIER_H

#include <iostream>
#include <string>
#include "miracl.h"

class Verifier {
public:
    epoint *PK_CA; // CA's public key

    Verifier(epoint *pk_ca);
    bool verifyAIK(epoint *PK_AI, signature &sigma_AIK);
    bool verifyReport(report &REP, signature &sigma_REPORT, epoint *PK_AI, signature &sigma_AIK_CA);
};

#endif
