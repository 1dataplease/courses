import numpy as np
from astropy.io import fits

# Write your mean_fits function here:
def mean_fits(list_of_fits_files):
  n = len(list_of_fits_files)
    
  if n > 0:
    # takes the first fits hdulist
    each_hdulist = fits.open(list_of_fits_files[0])
    each_fits_data = fits.open(list_of_fits_files[0])[0].data
        
    # 2nd thru rest of csvs, add them into the 1st
  for i in range(1, n):
    each_fits_data += fits.open(list_of_fits_files[i])[0].data

  # eventually want to get the mean brightness across pictures in each pt of 200x200 picture
  ## all this does though is gets the mean brightness of all 200x200 pts
  ## can access a specific x,y coord by adding [100,100] to end like: mean_fits(fits_files)[100,100]
  data_mean = each_fits_data / n
    
  return data_mean


if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()