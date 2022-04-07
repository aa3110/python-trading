import matplotlib.pyplot as plt
import path_def.pat1

from f__init__ import file_read
from p__init__ import plot2,col_plot,plot_aroon1,plot_scatter_line,plot_fit_line,plot_fit_p,plot_fit_lin_channel,plot_fit_p_channel,plot_bb
from p__init__ import stock2

df=file_read(stock2)

# for it in bb_pict:
#   plot2(it,df)
# plt.show()

# for it in sma1_pict:
#   col_plot(it,it+'_r',df)
# plt.show()

# for it in gap1_pict:
#   plot2(it,df)
# plt.show()

# for it in aroon1_pict:
#   plot_aroon1('Close_CCI',it,'Close',df)
# plt.show() 

y1=plot2('Closen',df)
plot2('Open',df)

# plot_scatter_line('Closen',200,500,df)
# plot_scatter_line('Close_rp',230,500,df)
# plot_scatter_line('Close',230,500,df)
# plot_fit_line('Closen_fp',230,330,df)
# plot_fit_line('Closen_fp',330,400,df)
# plot_fit_p('Closen_fp',225,500,10,df)
# plot_fit_p('Closen_rp',200,400,10,df)
# plot_fit_line('Closen_rp',330,400,df)
# plot_fit_line('Closen_rp',260,330,df)
# plot_fit_lin_channel('Closen_rp',260,330,df)
# plot_fit_lin_channel('Closen_rp',330,400,df)
# plot_fit_lin_channel('Closen',300,400,df)

# plot_fit_p_channel('Close',300,400,10,df)
# plot_scatter_line('Close',300,400,df)

# plt.show()

# plot2('Close_204',df)
# plot2('Closen',df)
# plot2(['bbm','bbh','bbl','Closen'],df)


#+++++
# plot_bb('Close','bbm','bbh','bbl',df)
# plot_bb('Closen','bbm','bbh','bbl',df)

# plot_bb('Close','bbm','rmin','rmax',df)
# plot_bb('Closen','bbm','rmin','rmax',df)

# plot_aroon1('CCI','Close_ah','Close',df)
# plot_aroon1('CCI','Close_al','Close',df)
#+++++



# plot_aroon1('CCI','CloseOpen_g','Close',df)


# plt.show()