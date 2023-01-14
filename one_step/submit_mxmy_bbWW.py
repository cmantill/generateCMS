username = "cmantill"
eosdir = "/store/group/lpcpfnano/miniaod/2017/XHYPrivate/"

# masses in X
massX = [650, 700, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3500, 4000]
# masses in Y (some are commented )
massY = [#60, #70, 80, 90, 
         100, 125, 150, 190, 250, 300, 350, 400, 450, 
         500, 600, 700, 800, 900, 1000, # 1100,
         1200, # 1300, 
         1400, 1600, 1800, 2000, 2200, 2400,
         #2500, 2600, 2800
     ]

massX_dict = {
    "cmantill": [#1000, 1200, 
                 1400, 1600],
    "rkansal": [650, 700, 1800, 2000, 2200],
    "amitav": [2400, 2600, 2800, 3000],
}

import os

with open("inputs/NMSSM_XToYH_MX_MY_HTo2bYTo2W_hadronicDecay_cfg.py") as f:
    template = f.read()
    
for mX in massX_dict[username]:
    for mY in massY:
        if mY < mX+125:
            with open("inputs/NMSSM_XToYH_MX%i_MY%i_HTo2bYTo2W_hadronicDecay_cfg.py"%(mX,mY),"w") as f:
                f.write(template.format(mxx=mX, myy=mY))

            cmd = f'python multi_crab_submit_onestep.py --name NMSSM_XToYH_MX{mX}_MY{mY}_HTo2bYTo2W_hadronicDecay'
            cmd += f' --config NMSSM_XToYH_MX{mX}_MY{mY}_HTo2bYTo2W_hadronicDecay_cfg  --begin-seed 0'
            cmd += f' --eosdir {eosdir} --site T3_US_FNALLPC' 
            os.system(cmd)
