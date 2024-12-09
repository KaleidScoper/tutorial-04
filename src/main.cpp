#include <iostream>
#include "ca.h"
#include "prover.h"
#include "verifier.h"

int main() {
    miracl *mip = mirsys(1000, 0);  // set up the big number library

    CA ca;
    ca.init();

    Prover prover;
    prover.registerWithCA(ca);
    prover.generateAIK();

    Verifier verifier(ca.PK_CA);
    if (verifier.verifyAIK(prover.PK_AI, prover.sigma_AIK)) {
        std::cout << "AIK verification successful!" << std::endl;
    } else {
        std::cout << "AIK verification failed!" << std::endl;
    }

    report REP;
    // Populate REP with PCR data sequence
    signature sigma_REPORT = prover.signReport(REP);
    if (verifier.verifyReport(REP, sigma_REPORT, prover.PK_AI, prover.sigma_AIK)) {
        std::cout << "Report verification successful!" << std::endl;
    } else {
        std::cout << "Report verification failed!" << std::endl;
    }

    return 0;
}
