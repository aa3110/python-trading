import io
from PIL import Image

def plt_io_image(plt=''):
  buf = io.BytesIO()
  plt.savefig(buf, format='png')  
  im = Image.open(buf)
  return im

# plt_io_image.show()
  
# img_buf.close()


def pltSaveFigToBytes(plt):    
    buf = io.BytesIO();plt.savefig(buf, format='png')
    buf.seek(0)
    return buf
  
# Image.open(buf).show()  
  
