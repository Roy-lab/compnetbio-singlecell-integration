from bignmf.models.jnmf.jnmf_base import JnmfBase
import numpy as np

class IntegrativeJnmf(JnmfBase):
	"""Integrative Joint NMF class.

	Integrative NMF is a variation of the standard Joint NMF algorithm that enforces stronger correlation between the matrices.
	For more detailed information on the algorithm, here's the reference to the original paper.

		Chalise P, Fridley BL (2017) Integrative clustering of multi-level ‘omic data based on non-negative matrix factorization algorithm.
		PLoS ONE 12(5): e0176278. 
	"""

	def __init__(self, x: dict, k: int, lamb: float, seed: int):
		"""Initializes the class with Integrative NMF algorithm parameters
		
		Args:
			x (dict): Input matrices on which we have to do NMF. Dictionary containing the input matrices as DataFrames. 
					  The common dimension between the matrices should be the row.
			k (float): Rank for factorization
			lamb (int): Hyper-parameter for the Integrative NMF algorithm that controls the rate of learning
		"""
		super().__init__(x, k)
		self.lamb = lamb
		self.slamb = None
		self.seed = seed

	def initialize_wh(self):
		"""Initializes the model variables
			
			Model Variables:
				W: Common submatrix 
				H: Dictionary of submatrices for each of the individual datasets with the same keys as the input dictionary 
				V: An integrative NMF variable with dimensions the same as ``H``
		"""
		number_of_samples = list(self.x.values())[0].shape[0]
		rng = np.random.RandomState(self.seed)
		self.w = rng.rand(number_of_samples, self.k)

		self.v = {}
		self.h = {}
		for key in self.x:
			self.h[key] = rng.rand(self.k, self.x[key].shape[1])
			self.v[key] = rng.rand(number_of_samples, self.k)

	def calc_error(self):
		"""Calculates the euclidean distance error with the following formulae."""
		self.error = 0
		for key in self.x:
			self.error += np.mean(np.abs(self.x[key] - np.dot(self.w+self.v[key], self.h[key])))


	def update_weights(self):
		"""Updates the model variables so that they converge towards :math:`W.H = X`"""
		
		w = self.w
		numerator = np.zeros(w.shape)
		denominator = np.zeros(w.shape)
		for key in self.x:
			x = self.x[key]
			h = self.h[key]
			v = self.v[key]	
			numerator = numerator + np.dot(x, h.T)
			denominator = denominator + np.dot(w+v, np.dot(h, h.T))
		self.w = self.w * numerator / denominator
		w = self.w
	
		for key in self.x:
			self.h[key] = ( self.h[key] * 
				np.dot((self.w + self.v[key]).T, self.x[key]) / 
				(np.dot(np.dot((self.w+self.v[key]).T, 
						self.w+self.v[key]), self.h[key]) 
				+ self.lamb * np.dot(self.v[key].T, 
						np.dot(self.v[key], self.h[key]))) )
			self.v[key] = ( self.v[key] * 
				np.dot(self.x[key], self.h[key].T) / 
				(np.dot(self.w+self.v[key], 
					np.dot(self.h[key], self.h[key].T)) 
				+ self.lamb * np.dot(self.v[key], 
						np.dot(self.h[key], self.h[key].T))) )

		self.calc_error()
