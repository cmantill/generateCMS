import numpy as np
from kinematics import *

def gen_phi():
    return 2.*np.pi*np.random.rand()

def gen_costh():
    return -1.+2.*np.random.rand()

def gen_two_body_decay_products_rest_frame(M, m1, m2):
    """
    Randomly selects four-vectors in the rest frame of the decay particle 
    with two body kinemtics. The angular distribution is flat for two body decays.
    M = mass of decaying particle; m1, m2 = daughter particle masses;
    Output is two four-vectors p1, p2 corresponding to m1, m2
    """
    if m1+m2>M:
        return -1,-1
    
    costh = gen_costh()
    if np.random.rand() > 0.:
        sinth = np.sqrt(1.-costh**2.)
    else:
        sinth = -np.sqrt(1.-costh**2.)

    ph = gen_phi()
    
    p = np.sqrt((M**2 - (m1+m2)**2)*(M**2 - (m1-m2)**2))/(2.*M)
    
    E1 = np.sqrt(m1**2 + p**2)
    E2 = np.sqrt(m2**2 + p**2)
    
    v1 = np.array([E1, p*sinth*np.cos(ph), p*sinth*np.sin(ph), p*costh])
    v2 = np.array([E2, -p*sinth*np.cos(ph), -p*sinth*np.sin(ph), -p*costh])
    
    return v1, v2



def get_rotation_matrix(v):
    """
    Find a rotation matrix s.t. R v = |v|(0,0,1)
    """
    
    vx = v[0]; vy = v[1]; vz = v[2]
    
    # Find first rotation to set y component to 0
    if np.fabs(vx) > 0. and np.fabs(vy) > 0.:
        ta = np.fabs(vy/vx)
        a = np.arctan(ta)
        
        if vx > 0. and vy > 0.:
            a = -a
        if vx < 0. and vy > 0.:
            a = -(np.pi - a)
        if vx < 0. and vy < 0.:
            a = -(np.pi + a)
        if vx > 0. and vy < 0.:
            a = -(2.*np.pi - a)
              
        ca = np.cos(a)
        sa = np.sin(a)
    elif np.fabs(vy) > 0.:
        ca = 0.
        sa = 1.
    else:
        ca = 1.
        sa = 0.
        
    Ra = np.array([[ca, -sa, 0.],[sa,ca,0.],[0.,0.,1.]])

    #sa = 0.
    #ca = 1.
    
    # Find second rotation to set x component to 0
    vxp = vx*ca - vy*sa
    if np.fabs(vz) > 0. and np.fabs(vxp) > 0.:
        tb = np.fabs(vxp/vz)
        b = np.arctan(tb)

        if vz > 0. and vxp > 0.:
            b = -b
        if vz < 0. and vxp > 0.:
            b = -(np.pi - b)
        if vz < 0. and vxp < 0.:
            b = -(np.pi + b)
        if vz > 0. and vxp > 0.:
            b = -(2.*np.pi - b)

        cb = np.cos(b)
        sb = np.sin(b)
    elif vxp > 0.:
        cb = 0.
        sb = -1.
    elif vxp < 0.:
        cb = 0.
        sb = 1.
    else:
        cb = 1.
        sb = 0.
        
    Rb = np.array([[cb, 0., sb],[0., 1., 0.],[-sb, 0., cb]])
    
    #return Rb
    
    #print "Rb v = ", np.matmul(Rb,v)
    
    return np.matmul(Rb,Ra)

def gen_two_body_decay_products(p_mother, M, m1, m2):
    """
    Generate proper decay product four_vectors in the 
    frame where the mother particle has four momentum p_mother
    """
   
    # Get four vectors in mother rest frame
    p1, p2 = gen_two_body_decay_products_rest_frame(M, m1, m2)
    rest_frame_events = [[p1, p2]]

    # Boost back to lab frame
    lab_frame_events = boost_events_to_lab_frame(p_mother, rest_frame_events)
    
    p1 = lab_frame_events[0,0]
    p2 = lab_frame_events[0,1]
    
    return p1, p2
    
def boost_events_to_lab_frame(p_mother, rest_frame_events):
    """
    Given a set of rest frame events (list of daughter-particle four momenta) 
    boost them to the lab frame in which the mother particle has four momentum p_mother.
    The events are assumed to have format [[p1,p2,p3],...]
    This is a version that does the boost in a slightly different way, 
    based on the implementation by Meg & Elizabeth
    """

    v_mother = p_mother[1:4]/p_mother[0]
    # boost_matrix transforms into the rest frame, so we need its inverse
    lorentz_transformation = boost_matrix(-v_mother) 

    lab_frame_events = []

    for evt in rest_frame_events: 
        evt_lab_frame = []
        for p_rf in evt:
            p_lab = np.matmul(lorentz_transformation,p_rf)
            evt_lab_frame.append(p_lab)
        lab_frame_events.append(evt_lab_frame)

    return np.array(lab_frame_events)


