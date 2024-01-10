class partition_into_k_buckets:
	"""
	Module to wrap relevant methods along with other utility functions
	
    Attributes
    ----------
	array(list)		 		:	the records per categories
	categories(list) 		:	the index/mapper for each array element i.e records
	k(int)			 		:	number of partition or buckets
	n(int)			 		:	length of the array
	cat2records_mapper(dict): 	one to one mapping with category list with records list  
	   
    """

	def __init__(self, array:list, categories:list, k:int,is_sort=True):
		self.array=array
		self.categories=categories
		self.k=k
		self.n=len(self.array)
		self.cat2records_mapper = {cat:records for cat,records in zip(self.categories,self.array)}
		if is_sort:
			self.sort_the_records()

	def dummy(self):
		return True

	def dummy2(self):
		return False
		
	def sort_the_records(self):
		'''
		sort the array of records keeping its index i.e categories variable intact.
		'''
		self.array,self.categories=list(zip(*sorted(zip(self.array,self.categories),key=lambda x: x[0])))


	def is_possible(self,mid:float):
		'''
		Function to find maximum subarray sum which is minimum

		Args:
			mid (float): the maximum current bucket size 

		Returns:
		    bool: a boolean value based on condition
		'''

		count = 0
		sum_ = 0

		# iterate over all the records
		for record in self.array:

			# see if the current record is more than the curr mid
			if (record > mid):
				return False

			# Increase sum of current sub-array
			sum_ += record

			# If the sum is greater than mid, increase count
			if (sum_ > mid):
				count += 1
				sum_ = record

		count += 1

		# count should be less than or equal to k
		if (count <= self.k):
			return True
		return False


	def get_optimal_partition_size(self):
		'''
		Function to find maximum subarray sum which is minimum

		Args: None

		Returns:
		    int: the optimal bucket size [i.e the maximum records we can have in a bucket] such that it is minimum.
		'''

		# taking the extreme ends
		start = max(self.array) #if k == n,
		end = sum(self.array) # if k==1

		# answer stores the maximum sub-array sum such that it is minimum
		answer = start
		while start <= end:
			mid = (start + end) // 2

			if (self.is_possible(mid)):
				answer = mid
				end = mid - 1
			else:
				start = mid + 1
		return answer


	def get_bucket_dict(self, bucket_names:list):
		'''
		function to partition the given records into k-subarray

		Args:
			bucket_names (list): name of the individual bucket

		Returns:
		    dict: dictionary containing the partitioned records.
		'''

		assert len(bucket_names) == self.k, 'bucket size should be equal to k'

		# intitialize the dictionary
		buckets_dict={bucket : [] for bucket in bucket_names}

		#create a utility dict to map the id to bucket name
		idx2bucket = {idx:bucket for idx,bucket in zip(range(len(bucket_names)),bucket_names)}

		# calls the get_optimal_partition_size() function to get the optimal value[the optimal sum of each bucket]
		optimal_records_per_buckets=int(self.get_optimal_partition_size())

		# assign all the records into k buckets such that the sum of each bucket doesn't exceed the optimal bucket size
		sum_till_now=0
		curr_bucket_id=0
		for i in range(self.n):
			sum_till_now+=self.array[i]
			if sum_till_now > optimal_records_per_buckets:
				sum_till_now = self.array[i]
				curr_bucket_id+=1
			buckets_dict[idx2bucket[curr_bucket_id]].append(self.categories[i])

		return buckets_dict

	
	def get_best_k(self, min_bucket_no:int, max_bucket_no:int):
		'''
		a utility function to get the best k value

		Args:
			min_bucket_no (int):
			max_bucket_no (int):

		Returns:
		    int : best bucket no.
		'''
		assert max_bucket_no<=self.n, 'maximum no of bucket is more than the size[array]'
		assert min_bucket_no>=1, "minimum bucket size should be postive value"

		min_val=float('inf')
		best_k=1
		cache_k=self.k
		for n_bucket in range(min_bucket_no,max_bucket_no+1):
			self.k=n_bucket
			optimal_val=int(self.get_optimal_partition_size())
			if optimal_val<min_val:
				min_val=optimal_val
				best_k=self.k

		self.k=cache_k
		return best_k
	
	def foobar(self,a):
		if a==1:
			return 1
		elif a==0:
			return 0
		else:
			return 2
