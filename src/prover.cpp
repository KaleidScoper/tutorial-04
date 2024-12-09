#include "prover.h"

Prover::Prover() {
    miracl *mip = mirsys(1000, 0);
    SK_P = mirvar(0);
    PK_P = epoint_init();
    PK_AI = epoint_init();
}

Prover::~Prover() {
    mirkill(SK_P);
    epoint_free(PK_P);
    epoint_free(PK_AI);
}

void Prover::registerWithCA(CA &ca) {
    // Prover generates key pair and sends to CA
    big q, K;
    epoint *temp = epoint_init();
    drand(K, q);
    ecurve_mult(g, K, PK_P, MR_PROJECTIVE);
    ca.registerProver(PK_P, SK_P, sigma);
}

void Prover::generateAIK() {
    // Generate AIK
    big q, K;
    epoint *temp = epoint_init();
    drand(K, q);
    ecurve_mult(g, K, PK_AI, MR_PROJECTIVE);
    sign(SK_P, PK_AI, sigma_AIK);
}
