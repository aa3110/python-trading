import matplotlib.pyplot as plt
import path_def.pat1
from f__init__ import file_read
from p__init__ import plot_scatter,plot_scatter_line,plot2,plot_aroon1

df=file_read('SIE_inp2')

plot_scatter_line('qty',0,20,df)
plot_scatter_line('qty_sum',0,20,df)
plt.show()

plot_scatter_line('invest',0,20,df)
plot_scatter_line('market_value',0,20,df)
plt.show()

plot_scatter_line('tax',0,20,df)
plot_scatter_line('tax_sum',0,20,df)
plot_scatter_line('broker_sum',0,20,df)
plot_scatter_line('cost_sum',0,20,df)
plt.show()

# plot_aroon1('rendite','qty_sum','market_value',df)
# plot_aroon1('rendite%','qty_sum','market_value',df)
# plot_aroon1('invest','market_value','rendite%',df)
# plot_aroon1('cash','depot','profit',df)

# plot_aroon1('qty','buy','value',df)