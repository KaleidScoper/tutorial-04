#include "ca.h"

CA::CA() {
    miracl *mip = mirsys(1000, 0);  // set up the big number library
    SK_CA = mirvar(0);
    PK_CA = epoint_init();
}

CA::~CA() {
    mirkill(SK_CA);
    epoint_free(PK_CA);
}

void CA::init() {
    // Generate CA's private and public keys
    big q, a, x;
    q = mirvar(0);
    a = mirvar(0);
    x = mirvar(0);
    cinstr(q, "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F", 16);
    cinstr(a, "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F", 16);
    ecurve_init(a, 4, 97);
    drand(K, q);
    g = epoint_init();
    ecurve_mult(g, K, PK_CA, MR_PROJECTIVE);
    itoa(K, SK_CA, 10);
}

void CA::registerProver(epoint *PK_P, big SK_P, signature &sigma) {
    // CA signs prover's public key
    epoint *temp = epoint_init();
    epoint_copy(PK_P, temp);
    sign(SK_CA, PK_P, sigma);
}

void CA::issueAIK(epoint *PK_AI, signature &sigma_AIK) {
    // Issue AIK to prover
    sign(SK_CA, PK_AI, sigma_AIK);
}
