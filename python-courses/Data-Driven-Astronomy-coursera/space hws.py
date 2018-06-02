# Write your calc_stats function here.
import numpy as np
import os
os.chdir(r'C:\Users\wainman\Desktop\tw\classes\python\online py_sql_data-driven-astronomy-coursera')

def calc_stats(csvf):
  data = []
  for line in open(csvf):
    data.append(line.strip().split(','))
  
  data = np.asarray(data, float)
 
  #could also have done the below
  #data = np.loadtxt('data.csv', delimiter = ',')
  
  data = np.sort(data)
 
  flat_list = []
  for sublist in data:
    for item in sublist:
        flat_list.append(item)
  
  mean = sum(flat_list) / len(flat_list)

  mid_pt = int(np.size(flat_list)//2.)
  
#  if len(flat_list) % 2:
#    median = flat_list[mid_pt]
#  else:
#    median = flat_list[mid_pt-1: mid_pt+1] / 2.
  median = np.median(flat_list)
  
  return (np.round(mean, 1), np.round(median, 1))

  
  #return flat_list


### mean of a set of signals
# Write your mean_datasets function here
import numpy as np

# see the arrays from each
#first_csvs_data = np.loadtxt('data1.csv', delimiter=',')
#second_csvs_data = np.loadtxt('data2.csv', delimiter=',')
#storage = [first_csvs_data, second_csvs_data]
#print(first_csvs_data + second_csvs_data / len(first_csvs_data))

def mean_datasets(list_of_files):
  '''
  assumes that all csvfiles have same shape/dimensions'''
  
  n = len(list_of_files)
  if n > 0:
    # takes the first csvs data
    each_csvs_data = np.loadtxt(list_of_files[0], delimiter = ',')
    
    # 2nd thru rest of csvs, add them into the 1st
    for i in range(1, n):
      each_csvs_data += np.loadtxt(filenames[i], delimiter = ',')
      
    # get the mean
    data_mean = each_csvs_data / n
    
    return np.round(data_mean, 1)

### tried below - close but gave up
  # one_list_of_csv_arrays = []
  # each_csvs_data = []
  # add_each_together = []
  # add_each_together - np.empty(np.shape())
  # add_each_together = np.array(add_each_together)

  
  #for file in list_of_files:
   # each_csvs_data = np.loadtxt(file, delimiter=',')
    #one_list_of_csv_arrays.append(each_csvs_data)
    #add_each_together = add_each_together + each_csvs_data
  
  #return add_each_together/len(one_list_of_csv_arrays)
    ## below is if not using numpy
    #data = []
    #for line in open(file):
      #data.append(line.strip().split(','))
      


### FITS files
## image is stored in a numerical array
## headers store metadata
from astropy.io import fits

## open a FITS file and print out header info
hdulist = fits.open(r'data/fits_images_mean/image0.fits')
hdulist.info()

## hddu or header data unit is a list
## each stores headers and image data

## header contains metadata about the hdu object (dimensions/data type)

## every hdu can contain img data
## 1st hdu is the primary HDU

## to access individual hdus, index the HDU list object returned by fits.open
## its stored in a np array, can operate on it
data = hdulist[0].data
data.shape

## to vizualize the img data stored in FITS files, matplotlib
import matplotlib.pyplot as plt
## plot the 2d array
plt.imshow(data, cmap = plt.cm.viridis)
plt.xlabel('x-pixels (RA)')
plt.ylabel('y-pixels (Dec)')
plt.colorbar()
plt.show()

## load_fits fxn that loads in a FITS file
## and finds the position of the brightest pixel (max value)
## pass name of FITS file as argument
## should return a x,y coord like 100,100

# returns highest value in an array
data.argmax()

# takes a fits file, returns pt thats brightest
def load_fits(fits_file_name):
    # list that stores each files headers and data pts
    hdulist = fits.open(fits_file_name)
    data = hdulist[0].data

    brightest_point = np.argmax(data)
  
    # to get the position, feed the data and the shape of the array
    brightest_position = np.unravel_index(brightest_point, data.shape)
    return brightest_position

## each file may or may not have a pulsar in it
## avg them out, see a clear detection
## calculate the mean of a stack of FITS files

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

fitsdata  = mean_fits(['data/fits_images_mean/image0.fits', 
'data//fits_images_mean/image1.fits', 'data//fits_images_mean/image2.fits'])

## 2a - calculating the median stack
## that py data manipulation and FITS files, a common astronomy data format
## calculated mean stack of a set of astronomy images

## now do same for median - considered better, more robust to outliers
## but a naive implementation can be inefficient in large dataset
## diff strategies to calc median
## think about much cpu time and memory diff algos require

## ex - youve measured fluxes and calculate their mean
from statistics import mean
fluxes = [17.3, 70.1, 22.3, 16.2, 20.7]
m = mean(fluxes); m

## most of the nums are near 20, so 29 isnt that representative
## if u take out 70, mean of 19 is better

## median instead
from statistics import median
m = median(fluxes); m
## 20.7 is closer, better. outliers less effect

## calculate median without using module
## dont need to assign to self
fluxes.sort()

##if odd, gets the middle one
mid = len(fluxes) // 2; mid

##if even, gets the one AFTER the midpoint
f6  = [17.3, 70.1, 22.3, 16.2, 20.7, 19.3]
f6mid = len(f6)//2; f6mid

## so to get the true middle for an even one, 
## avg this mid -1 and the mid
even_median = (fluxes[f6mid - 1] + fluxes[f6mid])/2
even_median

## write list_states(list_of_nums) -> (median, mean)
## cannot use statistics module or numpy or pandas
## for len 1, just ret that num in both

def list_stats(list_of_nums):
    '''returns tuple containing med, mean'''
    length = len(list_of_nums)
    
    list_of_nums.sort()
    midpt = (length)//2
    
    # if odd, ez, take middle one
    if length % 2 == 1:
        median = list_of_nums[midpt]
    # if 1, just take that num
    elif length == 1:
        median = list_of_nums[0]
    # if even, take the middle 2
    else:
        median = (list_of_nums[midpt - 1] + list_of_nums[midpt])/2

    if length > 0:
        data = list_of_nums[0]       
        
    for i in range(1, length):
        data += list_of_nums[i]
    
    mean = data / length
    
    return (median, mean)

list_stats(fluxes)



## edge cases, or want speed + better memory ussage
## how can we judge which implementations/solutions are best
## one way is by speed testing both fxns
## perf_counter uses most accurate counter on your device
## to measure the elapsed time
import time
start = time.perf_counter()
end = time.perf_counter() - start

## example
## find mean of large array using our code and numpy.mean
## np is optimized for numerical computation, doesnt work on strings, other dtypes

## create random inteers in a large range np.random.randn(number_of_fakes_to_make)
## can make substitututions strings with 'sfsdsd{:.2f}sdf'.format(variable)

n = 10**7
data = np.random.randn(n)
start = time.perf_counter()
mean = sum(data)/len(data)
seconds = time.perf_counter() - start
print('for 10**7 len list, sum(data) / len(data) took {:.2f} seconds.'.format(seconds))
print('\n')

start = time.perf_counter()
mean = np.mean(data)
seconds = time.perf_counter() - start
print('for 10**7 len list, sum(data) / len(data) took {:.2f} seconds.'.format(seconds))
print('\n')

## have to do it a 2nd time, not sure why
from statistics import mean
## write a time_stat to time our statistical implementations
def time_stat(fxn, size_of_array, n_repeats):
    data = np.random.randn(size_of_array)
    agg_seconds = 0
    for i in range(n_repeats):
        start = time.perf_counter()
        fxn(data)
        seconds = time.perf_counter() - start
        agg_seconds += seconds
    mean_sec = agg_seconds / n_repeats
    return mean_sec

# this prints the seconds for each fxn
print('{:.6f}s for statistics.mean'.format(time_stat(mean, 10**5, 10)))
print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))

# this works after importing mean a 2nd time
mean(np.random.randn(1))



## also want to measure memory usage - understand how py uses it
## look at how much memory 32-bit py needs to store some objects
## 28, 24, 80 and 64 bytes
## list holds references to other objects in memory
## also added element 2 an empty list - added 22 bytes, expected 28

import sys
a = 3
b = 3.123
c = [a,b]
d = []
for obj in [a,b,c,d]:
    print(obj, sys.getsizeof(obj))
e = []
print (e, sys.getsizeof(e))
e.append(a)
print (e, sys.getsizeof(e))

## numpy arrays are more compact, but there is some overhead to using
##array has nbytes attribute to get datas memory usage
## empty has 0, 3 has 12, large has about 10**6
## getsizeof is supposed to be larger, but isnt for me

a = np.array([])
b = np.array([1, 2, 3])
c = np.zeros(10**6)
for obj in [a, b, c]:
  print('sys:', sys.getsizeof(obj), 'np:', obj.nbytes)
a = np.zeros(5, dtype=np.int32)
b = np.zeros(5, dtype=np.float64)

for obj in [a, b]:
  print('nbytes         :', obj.nbytes)
  print('size x itemsize:', obj.size*obj.itemsize)

## see what the 4 images of 200x200 pixels take up - 160k
## each element is a float32 (for 32 bits)
## these elements require 4 bits of energy so
## 160k / 1024 = 156.25 kb
## if got to 1k or 10k arrays, would mean 7.5 mb, 75mb
200*200*4


def median_fits(list_of_fits_files):
    '''
    loads_fits_files is a single array sized 200x200
    nums represent a sum of brightness
    calculates the median image out of all the images
    where each pixel is the median of that pixel over all imgs
    return (median array, time_to_run, memory_used)
    '''
    ## 1. get the time_to_run
    start = time.perf_counter()
    agg_seconds = 0

    ## 2. load the files saved into a list
    list_containing_arrays_of_brightness_by_pixel = []
    
    for fitsfilename in list_of_fits_files:
        
        ## list that stores the header data
        hdulist = fits.open(fitsfilename)
        
        ## hdulist[0] gets the first file, then . data gets its data
        list_containing_arrays_of_brightness_by_pixel.append(hdulist[0].data)
        
        ## close it out so can open the 2nd,3rd,etc
        hdulist.close()
        
        ## now turn list of arrays into an object that has 3 dimensions
        fits_stack = np.dstack(list_containing_arrays_of_brightness_by_pixel)
        
    ## can now easily get the median
    median = np.median(fits_stack, axis=2)
    
    ## calculate the memory consumed specifically by the 3d stack
    ## when calculating just 1 objects num bytes, use nbytes not sys.getsizeof
    ## this can also be calculated by
    # memory = 200*200 * len(list_of_fits_files) * fits_stack.itemsize
    memory = fits_stack.nbytes

    ## convert bytes to kB
    memory /= 1024
        
    ## count seconds
    seconds = time.perf_counter() - start

    return (median, seconds, memory)

### failed attempt    
##    n_files = len(list_of_fits_files)
##    if n_files > 0:
##        # for reference - first line takes the first fits hdulist
##        # need to open the 1st of it, and the data in it
##        each_hdulist = fits.open(list_of_fits_files[0])
##        each_fits_data = fits.open(list_of_fits_files[0])[0].data
##        
##    # 2nd thru rest of csvs, add them into the 1st
##    for i in range(1, n_files):
##        each_fits_data += fits.open(list_of_fits_files[i])[0].data
#
#    ## get median
#    each_fits_data.sort()
#    n_pts = len(each_fits_data)
#    midpt = (n_pts)//2
#    
#    # if odd, ez, take middle one
#    if n_pts % 2 == 1:
#        median = each_fits_data[midpt]
#    # if 1, just take that num
#    elif n_pts % 2 == 1:
#        median = each_fits_data[0]
#    # if even, take the middle 2
#    else:
#        median = (each_fits_data[midpt - 1] + each_fits_data[midpt])/2
#
#    ## get the memory usage of file
#    memory_data_takes = sys.getsizeof(each_fits_data)
#
#    ## at end, count seconds
#    seconds = time.perf_counter() - start
#    
#    
#    
#    return (median, seconds, memory_data_takes)


## ex of using it
result = median_fits(['data/fits_images_median/image0.fits', 'data/fits_images_median/image1.fits'])
result[0][100, 100]
result[1]
result[2]
## 0.0123380571604 0.015657663345336914, 625.0
#result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
#print(result[0][100, 100], result[1], result[2]) 



# last of week 1
## refer to space hw and notes - HW 1.2 median stack
import numpy as np
## testing
#list_of_values = [1, 5, 7, 7, 3, 6, 1, 1]; num_bins = 4

#def median_bins(list_of_values, num_bins):
#    ''' 
#    input: a list of nums, and a num of bins in our histogram
#    output: the mean, the sd, and the bins (a list of lists containing nums)
#    
#    >>> median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4)
#    (3.875, 2.521780125229002, 3, array([ 0.,  1.,  1.,  1.]))    
#    '''
#    #1 - from list of values, calc mean and sd
#    array_of_values = np.array(list_of_values)
#    mean = array_of_values.mean()
#    sd = array_of_values.std()
#    ## faster
##    mean = np.mean(values)
##    std = np.std(values)
#
#    #2 - set the bounds
#    minval = mean - sd
#    maxval = mean + sd
#    
#    count_values_in_first_bin = 0
#    ## creates 1 array, with B or 4 0s in it
#    array_of_bins = np.zeros(num_bins)
#    
#    #3 - set bin width
#    bin_width = 2*sd / num_bins
#
#    #4 - make 1st bin an ignore one - all less than 1sd less than mean
#    ## go thru all values, decide which bin (of 4) they belong in
#    for num in list_of_values:
#        if num < minval:
#            #6 - count num of values that fall into each bin
#            #7 - starting from 1st/ignore bin, sum counts in each bin untul total>=n+1/2
#            count_values_in_first_bin += 1
#        elif num > maxval:
#            ## bins have to be equally spaced, this adds num of bins necessary
#            ## int gets the floor of the float and lets us use it as an index
#            #5 - make B bins for counting 1st and last bins    
#            num_of_bin_widths_above_maxval = int((num - minval)/bin_width)
#            array_of_bins[num_of_bin_widths_above_maxval] += 1
#            
#    #8 - return midpt of the bin that exceeded n+1/2
#    return mean, sd, count_values_in_first_bin, array_of_bins
#
#median_bins([1, 1, 3, 2, 2, 6], 3)
##(2.5, 1.707825127659933, 0, array([ 2.,  3.,  0.]))
#
#median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4)
##(3.875, 2.521780125229002, 3, array([ 0.,  1.,  1.,  1.]))
#
#
#
#
#
#
#
#def median_approx(list_of_values, num_bins):
#    '''
#    input: list of nums, and num of bins in histogram
#    output: approx median using the median_bins fxn to calculate the bins
#    
#    >>> median_approx([1,1,3,2,2,6], 3)
#    2.5
#    '''
#    ## call median_bins to calc mean, sd, count of nums in first large bin, num_bins to use
#    mean, sd, count_values_in_first_bin, array_of_bins = \
#    median_bins(list_of_values, num_bins)
#
#    ## get the position of the middle most element
#    count_of_values = len(list_of_values)
#    midpt = (count_of_values + 1)/2
#    
#    ## set the counter_of_these_values = count_values_in_first_bin
#    counter_until_mid = count_values_in_first_bin
#    
#    for b, values_in_bin in enumerate(array_of_bins):
#        counter_until_mid += values_in_bin
#        if counter_until_mid >= midpt:
#            break
#    
#    ## width of each bin is 2*sd / numbins
#    width = 2*sd / num_bins
#    
#    ## median goes in 1st bin + go haveway up the total num bins
#    ## width*(b + .5)
#    median = mean - sd + width*(b + .5)
#    
#    return median
#
#median_approx([1,1,3,2,2,6], 3)
##2.5
#
#median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4)
##4.50544503130725
#
###binapprox is a bad approx in these cases
##>>> median_bins([0, 1], 5)
##(0.5, 0.5, 0, array([ 1.,  0.,  0.,  0., 0.]))
##>>> median_approx([0, 1], 5)
##0.90000000000000002




## 2b - look at AGN at wavelength1, wavelength2; then compare data
# see notes

## 2b - declination
def convert_degrees_arcmin_arcsec_to_decimal_degrees(degrees, arcmin, arcsec):
    if degrees >= 0:
        return(degrees + arcmin/60 + arcsec/(60*60))

    else:
        return(-1*(-degrees + arcmin/60 + arcsec/(60*60)))

def hms2dec(hours,minutes,seconds):
    return(15*(hours + minutes/60 + seconds/(60*60)))

convert_degrees_arcmin_arcsec_to_decimal_degrees(73,21,14.4)
convert_degrees_arcmin_arcsec_to_decimal_degrees(-5, 31, 12)
hms2dec(23,12,6)

def angular_dist(ra1, dec1, ra2, dec2):
    '''
     to crossmatch 2 catalogs, need to compare angular dist b/w 
     objects on the celestial sphere
     the projected angle bw objects as seen from earth
     if object on celestial sphere has right ascension and declination ra1, decl1
     then angular dist to another oject with ra2, decl2
     
     inputs can be individ nums or arrays
     
     first it converts the ra and dec to radians
     breaks into 2 parts-
     a is sin**2 ra1 - ra2 / 2
     b is cos ra1 cos ra 2 sin **2 (ra1 - ra2)/2 
    '''
    ra1 = np.radians(ra1)
    dec1 = np.radians(dec1)
    ra2 = np.radians(ra2)
    dec2 = np.radians(dec2)

    a = np.sin(np.abs(dec1 - dec2)/2)**2    
    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
    
    angle = 2*np.arcsin(np.sqrt(a+b))
    return np.degrees(angle)

ra1, dec1 = 21.07, 0.1
ra2, dec2 = 21.15, 8.2
angular_dist(ra1, dec1, ra2, dec2) 
angular_dist(10.3, -3, 24.3, -29)

## before we can crossmatch 2 catalogs, import raw data

## at20g bright source survey sample
## file is table2.dat from 
## http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775
## will call it bss.dat
## has 320 objects

## we only care about the first 7 columns, not 8+ yet
## loadtxt wouldnt work for fixed-width cols if any vals missing
## since all IDs, RA and dec values there, it works
bss = np.loadtxt('data/bss.dat', usecols=range(1, 7))

## 2 - supercosmos all-sky catalog visual light
## 8 gb!
## http://ssa.roe.ac.uk/allSky

## csv of RA in decimal degrees, dec in decimal degrees
## magnitude, apparent shape, read by skipping header and comma delimit
#cosmos = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])

### NEED BIG DATA HERE ####
