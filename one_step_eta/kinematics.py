import numpy as np

def get_mom_from_lhe(rec):
    e, px, py, pz = rec['e'], rec['px'], rec['py'], rec['pz']
    return np.array([e,px,py,pz])

def pt(p):
    px = p[1]
    py = p[2]
    return np.sqrt(px**2 + py**2)

def rap(p, maxrap=10.):
    px, py, pz = p[1], p[2], p[3]
    
    if px == 0. and py == 0.:
        return maxrap
    if pz == 0.:
        return 0.
    
    pt = np.sqrt(px**2 + py**2)
    
    th = np.arctan(pt/pz)
    if th < 0.:
        th = th + np.pi
    
    return -np.log(np.tan(th/2.))

def theta(p):
    px, py, pz = p[1], p[2], p[3]
    pt = np.sqrt(px**2 + py**2)
    th = np.arctan(pt/pz)
    if th < 0.:
        th = th + np.pi
    return th

def lor_prod(p,v):
    return p[0]*v[0] - p[1]*v[1] - p[2]*v[2] - p[3]*v[3]

def boost(p,v):
    """
     boost v into the restframe of p
     you can show that this expression is equivalent to a boost in an arbitrary direction 
     with gamma = Ep/mp and 3 velocity p/(mp*gamma).
    """
    rsq = np.sqrt(lor_prod(p,p))
    v0 = lor_prod(p,v)/rsq
    c1 = (v[0] + v0)/(rsq + p[0])
    boosted_v = [v0, v[1] - c1*p[1], v[2] - c1*p[2], v[3] - c1*p[3]]
    
    return np.array(boosted_v)

def invariant_mass(p1,p2):
    """
    Lorentz invariant mass sqrt( (p1 + p2)^2 )
    """
    psum = np.asarray(p1) + np.asarray(p2)
    return np.sqrt(lor_prod(psum,psum))


def boost_matrix(v):
    """
    Lorentz transformation matrix parametrized by the three-velocity v. 
    This matrix transforms a four-vector into the rest frame of v
    """
    vx = v[0]
    vy = v[1]
    vz = v[2]
    vabs = np.linalg.norm(v)
    g = 1./np.sqrt(1. - vabs**2) 
    lorentz_matrix = np.array([[g    , -g*vx                   , -g*vy                 , -g*vz], \
                                 [-g*vx, 1+(g-1)*(vx*vx/vabs**2) ,  (g-1)*(vx*vy/vabs**2),  (g-1)*(vx*vz/vabs**2)], \
                                 [-g*vy,   (g-1)*(vy*vx/vabs**2) ,1+(g-1)*(vy*vy/vabs**2),  (g-1)*(vy*vz/vabs**2)], \
                                 [-g*vz,   (g-1)*(vz*vx/vabs**2) ,  (g-1)*(vz*vy/vabs**2),1+(g-1)*(vz*vz/vabs**2)]])

    return lorentz_matrix

