import sys
from src.wm_flow_creation import partition_into_k_buckets

# from wm_flow_creation import partition_into_k_buckets
records_per_cat = [1, 2, 3, 4]
categories = ["cat-1", "cat-2", "cat-3", "cat-4"]
buckets_name = ["A", "B", "C"]
k = len(buckets_name)

partitioner = partition_into_k_buckets(records_per_cat, categories, k)


# should skip this test component
def skip_test_foo():
    assert 1==2

def test_dummy():
    partitioner.dummy()==True

def test_failed():
    assert 3!=3

def test_get_bucket_dict():
    bucket_dict = partitioner.get_bucket_dict(buckets_name)
    assert {'A': ['cat-1', 'cat-2'], 'B': ['cat-3'], 'C': ['cat-4']}==bucket_dict

def test_get_best_k():
    val = partitioner.get_best_k(min_bucket_no=2, max_bucket_no=4)
    assert val==3

def test_is_possible():
# 4 or greater should return True
# 3 or lesser should return False
    assert partitioner.is_possible(4)==True
    assert partitioner.is_possible(3)==False

def test_get_optimal_partition_size():
# optimal bucket size should be 4
    assert partitioner.get_optimal_partition_size()==4

def test_foobar():
    assert partitioner.foobar(0)==1
