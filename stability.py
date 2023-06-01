import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':20})

# DEVICE U2 in first sample
#dir_path1 = 'Data\\4. Stability\\230517_pg3t_patterned_IV\\U2_m02_ID2-1.txt'
#dir_path2 = 'Data\\4. Stability\\230517_pg3t_patterned_bioprobe\\U2_m01_stability1-1.txt'
#dir_path3 = 'Data\\4. Stability\\230519_pg3t+SSE_patterned_IV\\U2_m01_ID2-1.txt'
#dir_path4 = 'Data\\4. Stability\\230519_pg3t+SSE_patterned_bioprobe\\U2_m02_stability1-1.txt'

#title1 = "Patterned p(g3T2-T) in GB"#_23.03.20"
#title2 = "Patterned p(g3T2-T) in air"
#title3 = "Patterned p(g3T2-T) + SSE in GB"
#title4 = "Patterned p(g3T2-T) + SSE in air"

# DEVICE D5 in first sample
#dir_path1 = 'Data\\4. Stability\\230522_pg3t+SSE_bioprobe_only\\D5_m01_stability1-1.txt'
#dir_path2 = 'Data\\4. Stability\\230522_pg3t+SSE_IV_afterbio\\D5_m01_ID2-1.txt'
#dir_path3 = 'Data\\4. Stability\\230522_pg3t+SSE_IV_afterbio+IV+transfer\D05_01_ID2-1.txt'
#dir_path4 = 'Data\\4. Stability\\230519_pg3t+SSE_patterned_bioprobe\\U2_m02_stability1-1.txt'

#title1 = "Patterned p(g3T2-T) + SSE in air first"#_23.03.20"
#title2 = "Patterned p(g3T2-T) + SSE in GB after air"
#title3 = "Patterned p(g3T2-T) + SSE in GB after measuring transfer curves"
#title4 = "Patterned p(g3T2-T) + SSE in air"

# UNPATTERN AND DEVICE U1,U2 in second sample
#dir_path1 = 'Data\\4. Stability\\230516_pg3t_unpatterned_IV\\D6_pg3t_unpatterned_2_ID2-1.txt'
#dir_path2 = 'Data\\4. Stability\\230516_pg3t_unpatterned_bioprobe\\D6_stability_stability1-1.txt'
#dir_path3 = 'Data\\4. Stability\\230523_new_pg3t+SSE\\U01_m01_ID2-1.txt'
#dir_path4 = 'Data\\4. Stability\\230523_new_pg3t+SSE\\U02_m01_ID2-1.txt'
#dir_path5 = 'Data\\4. Stability\\230523_new_pg3t+SSE+Ag\\U01_m02_ID2-1.txt'

#title1 = "Unpatterned p(g3T2-T) in GB"#_23.03.20"
#title2 = "Unpatterned p(g3T2-T) in air after GB"
#title3 = "Patterned p(g3T2-T) + SSE in GB (U1)"
#title4 = "Patterned p(g3T2-T) + SSE in GB, device U2 next to the previous"
#title5 = "Patterned p(g3T2-T) + SSE + Ag/AgCl gate non biased"

## Solid devices

dir_path1 = 'Data\\4. Stability\\230530_pg3t_printedSSE\\D5_m01_ID2-1.txt'
dir_path2 = 'Data\\4. Stability\\230531_pg3t+printedSSE_gatededoping\\D5_m01_Dedoping3-1.txt'
dir_path3 = 'Data\\4. Stability\\230531_pg3t+printedSSE_gatededoping\\D5_m02_Dedoping3-1.txt'

## IL device
dir_path4 = 'Data\\4. Stability\\230531_newpg3t+SSE_gatededoping\\U2_m01_Dedoping3-1.txt'
dir_path5 = 'Data\\4. Stability\\230531_newpg3t+SSE_gatededoping\\U7_m01_Dedoping3-1.txt'

title1 = "Solid Device (D5), non gate-biased"#_23.03.20"
title2 = "Solid Device (D5), +1V gate-biased"
title3 = "Solid Device (D5), +1V gate-biased part 2"

title4 = "Liquid Electrolyte (U2), +1V gate-biased"
title5 = "Liquid Electrolyte (U7), +1V gate-biased"

## Store files
#transfer1, stab1 = read_directory_bioprobe(dir_path1)
#transfer2, stab2 = read_directory_bioprobe(dir_path2)

stability(dir_path1, title1)#, log=False)
stability(dir_path2, title2)#, log=False)
stability(dir_path3, title3)#, log=False)
stability(dir_path4, title4)#, log=False)
stability(dir_path5, title5)#, log=False)
 
plt.show()