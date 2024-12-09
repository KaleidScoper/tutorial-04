#include "verifier.h"

Verifier::Verifier(epoint *pk_ca) {
    PK_CA = pk_ca;
}

bool Verifier::verifyAIK(epoint *PK_AI, signature &sigma_AIK) {
    // Verify AIK
    return sign(SK_CA, PK_AI, sigma_AIK);
}

bool Verifier::verifyReport(report &REP, signature &sigma_REPORT, epoint *PK_AI, signature &sigma_AIK_CA) {
    // Verify report
    if (!sign(PK_AI, REP, sigma_REPORT)) return false;
    return sign(PK_CA, PK_AI, sigma_AIK_CA);
}
