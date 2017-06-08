from __future__ import print_function, division
import numpy as np

def _make_array(array):
	return np.array(array)

def _enforce_dim(array, name, dim):
	array = _make_array(array)
	assert array.ndim == dim, 'Parameter {} must be of dimensionality {}, got array of shape {}'.format(name, dim,
	                                                                                                    array.shape)
	return array