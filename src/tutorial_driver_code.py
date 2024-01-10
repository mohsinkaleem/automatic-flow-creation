# import the flow creation module
from wm_flow_creation import partition_into_k_buckets

# initializing the records corresponding to the a nominal array[can be any type of categories]
# that we are trying to partition
records_per_cat = [1, 2, 3, 4]
categories = ["cat-1", "cat-2", "cat-3", "cat-4"]


# initialize the name of buckets, where k is the no of buckets/split
buckets_name = ["A", "B", "C"]
k = len(buckets_name)


"""
the  'partition_into_k_buckets' class has following attributes

array(list)		 		:	the records per categories
categories(list) 		:	the index/mapper for each array element i.e records
k(int)			 		:	number of partition or buckets
n(int)			 		:	length of the array
cat2records_mapper(dict): 	one to one mapping with category list with records list
"""

# instantiate the module
partitioner = partition_into_k_buckets(records_per_cat, categories, k)


bucket_dict = partitioner.get_bucket_dict(buckets_name)
print("bucket contents : ", bucket_dict)
# [Output] bucket contents :  {'A': ['cat-1', 'cat-2'], 'B': ['cat-3'], 'C': ['cat-4']}


# Note: the max_bucket_no should be less than some threshold maybe <10
#       we can't afford to create that many flow/bucket due to resource budget
print(
    "best k in the given range = ",
    partitioner.get_best_k(min_bucket_no=2, max_bucket_no=4),
)
# [Output] best k in the given range = 3
