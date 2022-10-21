import numpy as np

def calculate(list):
  #check list length
  if(len(list) <9):
    raise ValueError('List must contain nine numbers.')
  
  # convert to 3x3 array
  arr = np.array(list[:9]).reshape(3, 3)
  # dict with required methods
  methods = {
    'mean': np.mean,
    'variance': np.var,
    'standard deviation': np.std,
    'max': np.max,
    'min': np.min,
    'sum': np.sum
  }
  # and a simple function to apply for all axis
  def allAxis(arr, method):
    return [method(arr, ax).tolist() for ax in [0, 1, None]]
  
  # then map methods to all axis and return result
  return {key: allAxis(arr, value) for key, value in methods.items()}