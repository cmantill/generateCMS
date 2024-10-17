# EtaToGammaAp_ApToEE MC simulation

"""
Pythia8 simulation of meson production in collisisons, followed by their decay into photons and dark photons.

Based on example provided by Nikita Blinov

**PYTHIA must be compiled with the python interface enabled for this notebook to work**
"""

import numpy as np
import sys
import mc
import kinematics as kin
import time
import vector
import math
import csv
import argparse
import pythia8

def generate_meson_decay_chain(p_meson, m_vector, mf):
    """
    Generate decay chain meson > gamma + V, V > f f
    Args:
        p_meson - four-momentum of the parent meson
        m_vector - dark vector mass in the decay meson > gamma + V
        mf - final state mass in the dark vector decay V > f f
    Returns:
        list of four vectors [p_meson, p_gamma, p_vector, p1, p2]
    """
    m_meson = np.sqrt(kin.lor_prod(p_meson,p_meson))
    p_gamma, p_vector  = mc.gen_two_body_decay_products(p_meson, m_meson, 0., m_vector)
    p1, p2 = mc.gen_two_body_decay_products(p_vector, m_vector, mf, mf)
    
    return [p_meson, p_gamma, p_vector, p1, p2]

def main(args):
    nevents = args.nevents
    m_vector = args.mvector
    ptfilter = args.ptfilter
    seed = args.seed
    ptstring = "" if ptfilter is None else f"EtaPt{ptfilter}"
    
    # Generate some mesons from LHC collisions, while disabling $\eta$ decays, so that we can collect them and decay by hand.
    pythia = pythia8.Pythia()
    pythia.readString("Beams:eCM = 13600.");
    
    #pythia.readString("111: mayDecay = false") # pi0
    pythia.readString("221: mayDecay = false"); # eta

    pythia.readString("Random:setSeed = on");
    pythia.readString(f"Random:seed = {seed}");
    
    # Pick either HardQCD or SoftQCD but not both
    
    # SoftQCD
    # pythia.readString("SoftQCD:all = on")
    
    # HardQCD must be accompanied by a minimum pT cut:
    # "The pT_min cut cannot be put too low, or else unreasonably large jet cross sections will be obtained."
    # (from Pythia8 docs)
    pythia.readString("HardQCD:all = on");
    pythia.readString("PhaseSpace:pTHatMin = 20.");
    pythia.readString("Next:numberCount = 10000")    
    pythia.init();
    
    # run one event to make sure interface is working
    print(pythia.next())

    # Run main loop to generate LHC events, and collect produced mesons of interest
    pi0_total = 0
    eta_total = 0
    eta_prime_total = 0
    
    pi0_four_vector_list = []
    eta_four_vector_list = []
    eta_prime_four_vector_list = []
    
    starttime = time.time()

    # Begin event loop. Generate event. Skip if error. List first one.
    iEvent = 0
    while iEvent < nevents:
        if not pythia.next(): continue

        if ptfilter is not None:
            eta_pt = 0
            eta_eta = 9999
            for prt in pythia.event:
                four_mom = vector.obj(E=prt.e(), px=prt.px(), py=prt.py(), pz=prt.pz())
                if prt.isFinal() and prt.id() == 221:
                    eta_pt = four_mom.pt
                    eta_eta = abs(four_mom.eta)
            if eta_pt < ptfilter or eta_eta < 2.4:
                continue
            #print(iEvent, eta_pt)

        if iEvent % 10 == 0:
            print(f"!!! Processing event {iEvent}...")
            
        for prt in pythia.event:
            if prt.isFinal() and prt.id() == 111:
                pi0_total += 1
                pi0_four_vector_list.append(np.array([prt.e(), prt.px(), prt.py(), prt.pz()]))

            if prt.isFinal() and prt.id() == 221:
                eta_total += 1
                eta_four_vector_list.append(np.array([prt.e(), prt.px(), prt.py(), prt.pz()]))

            if prt.isFinal() and prt.id() == 331:
                eta_prime_total += 1
                eta_prime_four_vector_list.append(np.array([prt.e(), prt.px(), prt.py(), prt.pz()]))
        iEvent+=1
                
    # End of event loop. Statistics. Histogram. Done.
    pythia.stat();

    print("Total # of pi0s = ", pi0_total)
    print("Total # of etas = ", eta_total)
    print("Total # of etas primes = ", eta_prime_total)
    print("pi0 per interaction = ", pi0_total/nevents)
    print("eta per interaction = ", eta_total/nevents)
    print("eta prime per interaction = ", eta_prime_total/nevents)
    endtime = time.time()
    print("total time in mins = ", (endtime - starttime)/60.0)
    
    pi0_four_vector_list = np.array(pi0_four_vector_list)
    eta_four_vector_list = np.array(eta_four_vector_list)
    eta_prime_four_vector_list = np.array(eta_prime_four_vector_list)
    
    # Decay the collected $\eta$s as $\eta \to \gamma V$, with $V\to e^+ e^-$
    mf = 0.000511 # GeV # mass of electron
    eta_decay_events = [generate_meson_decay_chain(p_meson, m_vector, mf) for p_meson in eta_four_vector_list]
    
    # particle order: [p_meson, p_gamma, p_vector, p_fermion1, p_fermion2]
    print(eta_decay_events[0])

    # Check momentum conservation
    event = 0
    print("m_eta = ", np.sqrt(kin.lor_prod(eta_decay_events[event][0],eta_decay_events[event][0])))
    print("p_eta - p_vector - p_gamma = ", eta_decay_events[event][0] - eta_decay_events[event][1]-eta_decay_events[event][2])
    print("m_vector = ", np.sqrt(kin.lor_prod(eta_decay_events[event][2],eta_decay_events[event][2])))
    print("p_vector - p1 - p2 = ", eta_decay_events[event][2] - eta_decay_events[event][3]-eta_decay_events[event][4])
    print("m_fermion = ", np.sqrt(kin.lor_prod(eta_decay_events[event][4],eta_decay_events[event][4])))

    print("Write eta decay events")
    mass = f"{m_vector:.3f}".replace(".","p")
    with open(f'EtaToGammaAp_ApToEE_Ap{mass}GeV_{nevents}{ptstring}_seed{seed}.csv', 'w') as f:
        writer = csv.writer(f, delimiter=' ')
        for evt in eta_decay_events:
            for part in evt:
                writer.writerow([str(part[0]), str(part[1]), str(part[2]), str(part[3])])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--nevents",
        required=True,
        help="number of events to generate",
        type=int,
    )
    parser.add_argument(
        "--mvector",
        required=True,
        help="mass of Aprime in GeV",
        type=float,
    )
    parser.add_argument(
        "--ptfilter",
        default=None,
        help="filter of Eta pT in GeV",
        type=float,
    )
    parser.add_argument(
        "--seed",
        type=int,
        required=True,
        help="seed",
    )
    args = parser.parse_args()
    sys.exit(main(args))
